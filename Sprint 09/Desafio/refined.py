# importando as bibliotecas que achei necessárias.
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from datetime import datetime
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

# Defini os parâmetros.
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Carregando os dados Parquet derivados do json e csv.
df_json = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://data-lake-do-gilberto/TRUSTED/JSON/"]},
    format="parquet"
)

df_csv = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://data-lake-do-gilberto/TRUSTED/CSV/"]},
    format="parquet"
)

# Converti DynamicFrames para DataFrames para facilitar a manipulação.
df_json_spark = df_json.toDF()
df_csv_spark = df_csv.toDF()

# Colunas chave para comparação dos arquivos, para achar as séries em comum.
key_column_json = 'original_name'
key_column_csv = 'titulooriginal'

# Filtrando as séries comuns com base nas colunas chave.
common_series_json = df_json_spark.filter(df_json_spark[key_column_json].isin(
    df_csv_spark.select(key_column_csv).rdd.flatMap(lambda x: x).collect()))

# Nessa parte adicionei coluna 'id' com auto incremento.
window_spec = Window.orderBy("original_name")
common_series_json = common_series_json.withColumn(
    "id", row_number().over(window_spec))

# Deixando o Id na primeira posição das colunas.
columns = ['id'] + [col for col in common_series_json.columns if col != 'id']
common_series_json = common_series_json.select(*columns)

# Puxei data atual para nome do diretório
current_date = datetime.now()
year = current_date.strftime("%Y")
month = current_date.strftime("%m")
day = current_date.strftime("%d")

# Caminho para salvar os dados refinados
output_path = f"s3://data-lake-do-gilberto/STAGING AREA/PARQUET/2024/12/05/"

# Convertendo os dados de volta para DynamicFrame
common_series_dynamic_frame = DynamicFrame.fromDF(
    common_series_json, glueContext, "common_series_dynamic_frame")

# Escrevendo os dados refinados em formato Parquet na camada 'staging area'
glueContext.write_dynamic_frame.from_options(
    frame=common_series_dynamic_frame,
    connection_type="s3",
    connection_options={"path": output_path},
    format="parquet"
)

job.commit()
