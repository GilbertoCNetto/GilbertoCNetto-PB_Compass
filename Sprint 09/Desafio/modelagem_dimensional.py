# importando as bibliotecas que achei necessárias.
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import to_date
from datetime import datetime

# Defini os parâmetros.
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Peguei o caminho do arquivo parquet, com as séries em comum dos arquivos da sprint passada.
serie_comum_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={
        "paths": ["s3://data-lake-do-gilberto/STAGING AREA/PARQUET/"]},
    format="parquet"
).toDF()

# Nessa parte, converti a coluna 'first_air_date' para data, pois estava como string
serie_comum_df = serie_comum_df.withColumn(
    "first_air_date", to_date("first_air_date", "yyyy-MM-dd"))

# Criei uma temp view
serie_comum_df.createOrReplaceTempView("serie_comum")

# A partir daqui, criei as colunas, usando uma função do spark, que me permite digitar os códigos todos em SQL, e utilizei o 'monotonically_increasing_id' para criação dos ids
# Na dim_origem, puxei as colunas que considerei que tinham a ver com a origem das séries, como 'original_name' e 'original_country'
dim_origem_df = spark.sql("""
    SELECT
        monotonically_increasing_id() AS id_origem,
        original_name,
        origin_country,
        original_language
    FROM serie_comum
    GROUP BY
        original_name, origin_country, original_language
""").distinct()

# Na dim_serie eu selecionei as colunas mais gerais das séries.
dim_serie_df = spark.sql("""
    SELECT
        id,
        name,
        season_count,
        status,
        genre,
        popularity
    FROM serie_comum
    GROUP BY
        id, name, season_count, status, genre, popularity
""").distinct()

# Na dim_votos, apenas selecionei as colunas relacionadas aos votos.
dim_votos_df = spark.sql("""
    SELECT
        monotonically_increasing_id() AS id_votos,
        vote_average,
        vote_count
    FROM (
        SELECT DISTINCT vote_average, vote_count
        FROM serie_comum
    )
""").distinct()

# Na dim_tempo selecionei a coluna 'first_air_date' e também criei separações para ter colunas de ano, mes e dia.
dim_tempo_df = spark.sql("""
    SELECT
        monotonically_increasing_id() AS id_data,
        first_air_date AS data,
        YEAR(first_air_date) AS ano,
        MONTH(first_air_date) AS mes,
        DAY(first_air_date) AS dia
    FROM (
        SELECT DISTINCT first_air_date
        FROM serie_comum
    )
""").distinct()

# Para tabelas fato_series, apenas adicionei os ids das outras tabelas.
fato_series_df = spark.sql("""
    SELECT
        s.id AS id_serie,
        v.id_votos,
        t.id_data,
        o.id_origem
    FROM serie_comum sc
    JOIN (
        SELECT id, name
        FROM serie_comum
        GROUP BY id, name
    ) s ON sc.id = s.id
    JOIN (
        SELECT vote_average, vote_count, monotonically_increasing_id() AS id_votos
        FROM serie_comum
        GROUP BY vote_average, vote_count
    ) v ON sc.vote_average = v.vote_average AND sc.vote_count = v.vote_count
    JOIN (
        SELECT first_air_date, monotonically_increasing_id() AS id_data
        FROM serie_comum
        GROUP BY first_air_date
    ) t ON sc.first_air_date = t.first_air_date
    JOIN (
        SELECT original_name, monotonically_increasing_id() AS id_origem
        FROM serie_comum
        GROUP BY original_name
    ) o ON sc.original_name = o.original_name
""")

dim_serie_dynamic_frame = DynamicFrame.fromDF(
    dim_serie_df, glueContext, "dim_serie_dynamic_frame")
dim_votos_dynamic_frame = DynamicFrame.fromDF(
    dim_votos_df, glueContext, "dim_votos_dynamic_frame")
dim_origem_dynamic_frame = DynamicFrame.fromDF(
    dim_origem_df, glueContext, "dim_origem_dynamic_frame")
dim_tempo_dynamic_frame = DynamicFrame.fromDF(
    dim_tempo_df, glueContext, "dim_tempo_dynamic_frame")
fato_series_dynamic_frame = DynamicFrame.fromDF(
    fato_series_df, glueContext, "fato_series_dynamic_frame")

# Passando o path de onde eu queria salvar os arquivos da modelagem dimensional
path_dim_serie = f"s3://data-lake-do-gilberto/REFINED/dim_serie/"
path_dim_origem = f"s3://data-lake-do-gilberto/REFINED/dim_origem/"
path_dim_votos = f"s3://data-lake-do-gilberto/REFINED/dim_votos/"
path_dim_tempo = f"s3://data-lake-do-gilberto/REFINED/dim_tempo/"
path_fato_series = f"s3://data-lake-do-gilberto/REFINED/fato_series/"

# E aqui fiz um código para escrever as tabelas dimensionais e de fatos em formato Parquet
glueContext.write_dynamic_frame.from_options(
    frame=dim_serie_dynamic_frame,
    connection_type="s3",
    connection_options={"path": path_dim_serie},
    format="parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame=dim_votos_dynamic_frame,
    connection_type="s3",
    connection_options={"path": path_dim_votos},
    format="parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame=dim_origem_dynamic_frame,
    connection_type="s3",
    connection_options={"path": path_dim_origem},
    format="parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame=dim_tempo_dynamic_frame,
    connection_type="s3",
    connection_options={"path": path_dim_tempo},
    format="parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame=fato_series_dynamic_frame,
    connection_type="s3",
    connection_options={"path": path_fato_series},
    format="parquet"
)

job.commit()
