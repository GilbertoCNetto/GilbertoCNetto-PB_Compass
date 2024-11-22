import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, upper

args = getResolvedOptions(
    sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df = spark.read.csv(args['S3_INPUT_PATH'], header=True, inferSchema=True)

df = df.withColumn('nome', upper(col('nome')))

df = df.orderBy(col('ano').desc())

feminino = df.filter(df.sexo == 'F').groupBy(
    'nome', 'ano').count().orderBy(col('count').desc()).first()
if feminino:
    print(f"O nome feminino com mais registros foi '{
          feminino['nome']}' no ano de {feminino['ano']}.")

masculino = df.filter(df.sexo == 'M').groupBy(
    'nome', 'ano').count().orderBy(col('count').desc()).first()
if masculino:
    print(f"O nome masculino com mais registros foi '{
          masculino['nome']}' no ano de {masculino['ano']}.")

output_path = args['S3_OUTPUT_PATH']
if not output_path.endswith('/'):
    output_path += '/'
output_path = f"{output_path}frequencia_registro_nomes_eua/"

try:
    test_df = spark.createDataFrame([{"coluna": "teste"}])
    test_df.write.mode('overwrite').json(f"{output_path}teste/")
except Exception as e:
    print(f"Erro ao testar gravação no S3: {e}")
    job.commit()
    sys.exit(1)

df.write.mode('overwrite').partitionBy('sexo', 'ano').json(output_path)

job.commit()
