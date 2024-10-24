import pandas as pd
import boto3
from io import StringIO


conexao_s3 = boto3.client('s3')

nome_bucket = 'sprint-05-desafio'
nome_do_arquivo = "chegadas_2023.csv"

acesso_csv_s3 = conexao_s3.get_object(Bucket=nome_bucket, Key=nome_do_arquivo)
ler_csv = acesso_csv_s3['Body'].read().decode('latin1')


df = pd.read_csv(StringIO(ler_csv), delimiter=';')


# 1. Classificação condicional com base nas Chegadas
def classificar_chegadas(row):
    if row['Chegadas'] >= 100:
        return 'Alta'
    elif row['Chegadas'] > 0:
        return 'Média'
    else:
        return 'Baixa'


df['Classificação'] = df.apply(classificar_chegadas, axis=1)


def processar_dataframe(df):
    # Substituir NaN na coluna 'UF'
    ufs = {
        'Acre': 'AC',
        'Alagoas': 'AL',
        'Amapá': 'AP',
        'Amazonas': 'AM',
        'Bahia': 'BA',
        'Ceará': 'CE',
        'Distrito Federal': 'DF',
        'Espírito Santo': 'ES',
        'Goiás': 'GO',
        'Maranhão': 'MA',
        'Mato Grosso': 'MT',
        'Mato Grosso do Sul': 'MS',
        'Minas Gerais': 'MG',
        'Pará': 'PA',
        'Paraíba': 'PB',
        'Paraná': 'PR',
        'Pernambuco': 'PE',
        'Piauí': 'PI',
        'Rio de Janeiro': 'RJ',
        'Rio Grande do Norte': 'RN',
        'Rio Grande do Sul': 'RS',
        'Rondônia': 'RO',
        'Roraima': 'RR',
        'Santa Catarina': 'SC',
        'São Paulo': 'SP',
        'Sergipe': 'SE',
        'Tocantins': 'TO'
    }

    # 2. Mapeamento das UFs e substituição dos NaN
    df['Sigla_UF'] = df['UF'].map(ufs)
    df['Sigla_UF'] = df['Sigla_UF'].fillna('Outros')

    # 3. Conversão das strings e formatação
    df['Continente'] = df['Continente'].str.upper()
    df['País'] = df['País'].str.title()
    df['Classificação'] = df['Classificação'].str.strip()

    # 4. Criação de uma coluna para data
    df['Data'] = pd.to_datetime(df['ano'].astype(
        str) + '-' + df['cod mes'].astype(str) + '-01')

    # 5. Aplicação do filtro para ano > 2022 e Chegadas >= 1
    df_filtrado = df[(df['ano'] > 2022) & (df['Chegadas'] >= 1)]

    # 6. Primeira agregação: A Soma e a média das chegadas por Continente e País
    df_soma_e_media = df.groupby(['Continente', 'País'])[
        'Chegadas'].agg(['sum', 'mean'])
    df_soma_e_media = df_soma_e_media.rename(
        columns={'sum': 'soma', 'mean': 'média'})

    # Segunda agregação: A Contagem e o valor máximo de chegadas por Continente
    df_contagem = df.groupby(
        ['Continente'])['Chegadas'].agg(['count'])
    df_contagem = df_contagem.rename(
        columns={'count': 'contagem'})

    return df_filtrado, df_soma_e_media, df_contagem, df


df_filtrado, df_soma_e_media, df_contagem, df_processado = processar_dataframe(
    df)

# Exibindo as tabelas
# filtrado por número de chegadas maior que 0
print(df_filtrado)

print(df_soma_e_media)

print(df_contagem)

print(df_processado)

# 1. df_filtrado
# Salvar o CSV do df_filtrado localmente
df_filtrado.to_csv('df_filtrado.csv', index=False, sep=';')

# Subindo o csv do df_filtrado para o S3
conexao_s3.upload_file('df_filtrado.csv', nome_bucket, 'df_filtrado.csv')

# 2. tabelas de agregação
# Salvar o CSV do df_soma_e_media localmente
df_soma_e_media.to_csv('df_soma_e_media.csv', index=False, sep=';')

# Subindo o csv do df_soma_e_media para o S3
conexao_s3.upload_file('df_soma_e_media.csv',
                       nome_bucket, 'df_soma_e_media.csv')

# Salvar o CSV do df_contagem localmente
df_contagem.to_csv('df_contagem.csv', index=False, sep=';')

# Subindo o csv do df_contagem para o S3
conexao_s3.upload_file('df_contagem.csv', nome_bucket, 'df_contagem.csv')

# 3. df_processado
# # Salvar o CSV do df_processado localmente
df_processado.to_csv('df_processado.csv', index=False, sep=';')

# Subindo o csv do df_processado para o S3
conexao_s3.upload_file('df_processado.csv', nome_bucket, 'df_processado.csv')

print('Os arquivos csv foram criados e upados para o s3 com sucesso!')
