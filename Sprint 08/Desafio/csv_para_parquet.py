import sys
from datetime import datetime
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, lit

# Passando os Argumentos do Job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

csv_path = "s3://data-lake-do-gilberto/RAW/Local/CSV/Series/2024/11/08/series.csv"

# Aqui eu defini o delimitador do arquivo CSV que no caso é o pipe
raw_df = spark.read.option("header", "true").option(
    "delimiter", "|").csv(csv_path)

# Nessa parte eu renomeei a coluna de 'tituloPincipal' para 'tituloPrincipal'
raw_df = raw_df.withColumnRenamed("tituloPincipal", "tituloPrincipal")

# Também transformei as colunas seguintes de string para numérico
raw_df = raw_df.withColumn("anoLancamento", col("anoLancamento").cast("int")) \
               .withColumn("anoTermino", col("anoTermino").cast("int")) \
               .withColumn("tempoMinutos", col("tempoMinutos").cast("int")) \
               .withColumn("notaMedia", col("notaMedia").cast("float")) \
               .withColumn("numeroVotos", col("numeroVotos").cast("int"))

# Adicionando coluna de gênero com 'Drama' para todos os registros
raw_df = raw_df.withColumn("genero", lit("Drama"))

# Selecionando apenas as colunas que considerei necessárias para minha análise
selected_columns = raw_df.select(
    "id", "tituloPrincipal", "tituloOriginal", "anoLancamento", "anoTermino", "tempoMinutos", "notaMedia", "numeroVotos"
).dropDuplicates(["id"])

# Puxando a data atual, com o mesmo formato das sprints anteriores
current_date = datetime.now()
year = current_date.strftime("%Y")
month = current_date.strftime("%m")
day = current_date.strftime("%d")

trusted_path = f"s3://data-lake-do-gilberto/TRUSTED/CSV/{year}/{month}/{day}/"

# Gravando os dados na zona Trusted em formato PARQUET
selected_columns.write.mode("overwrite").parquet(
    trusted_path, compression="snappy")

job.commit()
