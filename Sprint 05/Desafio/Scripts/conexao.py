import pandas as pd
import boto3
from io import StringIO

# Conexão com o S3
conexao_s3 = boto3.client('s3')

nome_bucket = 'sprint-05-desafio'
nome_do_arquivo = "Tabela 2 - Tributo e Competência.csv"

# Faz o download do arquivo
acesso_csv_s3 = conexao_s3.get_object(Bucket=nome_bucket, Key=nome_do_arquivo)

# Lê o conteúdo do arquivo CSV
ler_csv = acesso_csv_s3['Body'].read().decode('utf-8')

# Carrega o CSV no DataFrame
df = pd.read_csv(StringIO(ler_csv), delimiter=';')


# Criando a função de data
def transformar_ano_em_data(df, coluna_ano):
    df[coluna_ano] = pd.to_datetime(
        df[coluna_ano].astype(str).str[:4] + '-01-01')

    return df


df = transformar_ano_em_data(df, 'Ano-calendário')


# Criando a função de conversão
def converter_para_numerico(df, coluna):
    # Remover vírgulas e converter para numérico
    df[coluna] = df[coluna].str.replace(',', '.').astype(float)
    return df


# Usando a função para converter as colunas 'Valor da Receita Tributária' e 'Percentual do PIB'
df = converter_para_numerico(df, 'Valor da Receita Tributária')
df = converter_para_numerico(df, 'Percentual do PIB')


# Criando a função de string
def converter_para_maiusculas(df, descricao):
    df[descricao] = df[descricao].str.upper()

    return df


df = pd.DataFrame(df)
df = converter_para_maiusculas(df, 'Descrição')


# Criando a função condicional
def classificar_receita_por_pib(df):
    # Aplicando uma condição ao DataFrame pra criar umaa nova coluna 'Classificação Receita'
    df['Classificação Receita'] = df['Percentual do PIB'].apply(
        lambda x: 'Alta' if x > 0.25 else 'Baixa')
    return df


df = classificar_receita_por_pib(df)


# Clausula com dois operadores lógicos
filtro = (df['Ano-calendário'] ==
          '2002-01-01') & (df['Percentual do PIB'] > 0.05)

# Aplicando o filtro ao DataFrame
df_filtrado = df[filtro]


def agrega_por_ano(df):
    df['Ano-calendário'] = df.index // 46 + 2002  # ano inicial = 2002
    # Agrupa por ano somando a receita tributária e calculando a média do percentual do PIB
    agregacao_ano = df.groupby('Ano-calendário').agg({
        'Valor da Receita Tributária': 'sum',
        'Percentual do PIB': 'mean'
    }).reset_index()
    return agregacao_ano


def agrega_por_classificacao(df):
    # Agrupa por classificação da receita somando a receita tributária e calculando a média do percentual do PIB
    agregacao_classificacao = df.groupby('Classificação Receita').agg({'Valor da Receita Tributária': 'sum',
                                                                       'Percentual do PIB': 'mean'}).reset_index()
    return agregacao_classificacao


agregado_ano = agrega_por_ano(df)
agregado_classificacao = agrega_por_classificacao(df)

print(df)
print(df_filtrado)
print(agregado_ano)
print(agregado_classificacao)

# Subindo os arquivos CSV resultantes do codigo e salvando localmente.
# df_filtrado
df_filtrado.to_csv('df_filtrado.csv', index=False, sep=';')
conexao_s3.upload_file('df_filtrado.csv', nome_bucket, 'df_filtrado.csv')

#
df.to_csv('df.csv', index=False, sep=';')

# Subindo o csv do df para o S3
conexao_s3.upload_file('df.csv', nome_bucket, 'df.csv')

# agregado_ano
agregado_ano.to_csv('agregado_ano.csv', index=False, sep=';')
conexao_s3.upload_file('agregado_ano.csv', nome_bucket, 'agregado_ano.csv')

# agregado_classificacao
agregado_classificacao.to_csv(
    'agregado_classificacao.csv', index=False, sep=';')
conexao_s3.upload_file('agregado_classificacao.csv',
                       nome_bucket, 'agregado_classificacao.csv')
