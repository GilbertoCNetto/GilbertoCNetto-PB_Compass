import boto3

cliente_s3 = boto3.resource('s3')

nome_bucket = 'sprint-05-desafio'

cliente_s3.create_bucket(Bucket=nome_bucket)

caminho_arquivo = r"D:\Gilberto\Gilberto Pb - Compass\CSV sprint 5\chegadas_2023.csv"

nome_do_arquivo = "chegadas_2023.csv"

cliente_s3.Bucket(nome_bucket).upload_file(caminho_arquivo, nome_do_arquivo)

print(f'Bucket {nome_bucket} criado e arquivo {
      nome_do_arquivo} carregado com sucesso.')
