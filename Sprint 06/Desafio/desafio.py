import boto3
from datetime import datetime

cliente_s3 = boto3.client('s3')

nome_bucket = 'data-lake-do-gilberto'

cliente_s3.create_bucket(Bucket=nome_bucket)

caminho_arquivo_1 = r"/app/series.csv"

caminho_arquivo_2 = r"/app/movies.csv"

nome_do_arquivo_1 = "series.csv"

nome_do_arquivo_2 = "movies.csv"

data = datetime.now().strftime('%Y/%m/%d')

path_series = f"RAW/Local/CSV/Series/{data}/{nome_do_arquivo_1}"
path_movies = f"RAW/Local/CSV/Movies/{data}/{nome_do_arquivo_2}"

cliente_s3.upload_file(caminho_arquivo_1, nome_bucket, path_series)
cliente_s3.upload_file(caminho_arquivo_2, nome_bucket, path_movies)

print('Conexão feita com sucesso')
