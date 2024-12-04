# Comecei importando as bibliotecas
import sys
from datetime import datetime
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, size, to_date, lit, when, explode

# Passando os Argumentos do Job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


json_path = "s3://data-lake-do-gilberto/RAW/TMDB/JSON/2024/11/21/"

# Aqui eu fiz a leitura dos arquivos json
raw_data = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [json_path]},
    format="json"
)

# Converti para DynamicFrame para DataFrame para manipulação com Spark
raw_df = raw_data.toDF()

# Fiz essa linha para poder lidar com cada série individualmente, pois estavam as temporadas detalhadas, e isso estava dando problema na criação do parquet
exploded_df = raw_df.withColumn("season", explode(col("seasons")))

# Filtrei as temporadas, pois haviam algumas como "Especiais" e com 'air_date' nulo, pois ainda não haviam sido lançadas, então as removi, para contar corretamente o número de temporadas
filtered_seasons_df = exploded_df.filter(
    ~col("season.name").like("%Especiais%") & col(
        "season.air_date").isNotNull()
)

# Contei somente as temporadas válidas após a filtragem
grouped_df = filtered_seasons_df.groupBy(
    "id", "original_name", "name", "first_air_date", "status", "vote_average", "vote_count",
    "origin_country", "popularity", "original_language"
).count().withColumnRenamed("count", "season_count")

# Nesta parte converti a coluna de data de string para datetime e filtrando registros com 'null' em 'first_air_date' para remover séries que ainda não foram ao ar
grouped_df = grouped_df.withColumn("first_air_date", to_date(col("first_air_date"), "yyyy-MM-dd")) \
                       .filter(col("first_air_date").isNotNull())

# Adicionando coluna de gênero com 'Drama' para todos os registros, pois achei melhor de visualizar, já que todas as séries são de drama
grouped_df = grouped_df.withColumn("genre", lit("Drama"))

# Selecionei apenas as colunas necessárias para minha análise
selected_columns = grouped_df.select(
    "original_name", "name", "first_air_date", "season_count", "status", "vote_average",
    "vote_count", "genre", "origin_country", "popularity", "original_language"
).dropDuplicates()

# Converti de volta para DynamicFrame
final_data = DynamicFrame.fromDF(selected_columns, glueContext, "final_data")

# Puxando a data atual, com o mesmo formato das sprints anteriores
current_date = datetime.now()
year = current_date.strftime("%Y")
month = current_date.strftime("%m")
day = current_date.strftime("%d")

trusted_path = f"s3://data-lake-do-gilberto/TRUSTED/JSON/{year}/{month}/{day}/"

# Gravando os dados na zona Trusted em formato PARQUET
glueContext.write_dynamic_frame.from_options(
    frame=final_data,
    connection_type="s3",
    connection_options={"path": trusted_path},
    format="parquet",
    format_options={"compression": "snappy"}
)

job.commit()
