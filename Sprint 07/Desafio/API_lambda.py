import requests
import json
import os
from datetime import datetime
import boto3


# Função para buscar séries de drama
def series_de_drama_durante_os_anos(api_key, ano_inicial, ano_final, page=1):
    url_padrao = "https://api.themoviedb.org/3"
    url_series = "discover/tv"
    url_final = f"{url_padrao}/{url_series}"

    params = {
        "api_key": api_key,
        "with_genres": "18",  # ID do gênero Drama
        "first_air_date.gte": f"{ano_inicial}-01-01",
        "first_air_date.lte": f"{ano_final}-12-31",
        "page": page,
        "language": "pt-BR"
    }

    try:
        response = requests.get(url_final, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao chamar à API: {e}")
        return None


# Função para buscar detalhes de cada série
def detalhes_das_series(api_key, series_id):
    url_padrao = "https://api.themoviedb.org/3"
    url_details = f"tv/{series_id}"
    url_final = f"{url_padrao}/{url_details}"

    params = {
        "api_key": api_key,
        "language": "pt-BR"
    }

    try:
        response = requests.get(url_final, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar detalhes da série {series_id}: {e}")
        return None


# Função principal que vai ser executada no AWS Lambda
def lambda_handler(event, context):
    # Obtendo a chave da API de variáveis de ambiente
    api_key = os.getenv("TMDB_KEY")
    ano_inicial = event.get('ano_inicial', 2000)  # Ano inicial
    ano_final = event.get('ano_final', 2020)  # Ano final
    limite_de_series = event.get('limite_de_series', 300)  # Limite de séries
    total_series = 0
    pagina_atual = 1
    todas_series = []
    file_index = 1

    # Definir a data atual
    data_atual = datetime.now()
    ano = data_atual.year
    mes = data_atual.month
    dia = data_atual.day

    # Nome do bucket S3
    s3_bucket = "data-lake-do-gilberto"

    # Cliente S3
    s3_client = boto3.client('s3')

    while total_series < limite_de_series:
        data = series_de_drama_durante_os_anos(
            api_key, ano_inicial, ano_final, pagina_atual)

        if data:
            resultados = data.get("results", [])
            falta_para_300 = limite_de_series - total_series

            # Limitar os resultados que faltam para 300
            resultados = resultados[:falta_para_300]

            # Buscar mais detalhes de cada série
            for serie in resultados:
                series_id = serie['id']
                detalhes = detalhes_das_series(api_key, series_id)

                if detalhes:
                    serie['status'] = detalhes.get('status', 'Desconhecido')
                    serie['seasons'] = detalhes.get('seasons', [])

            todas_series.extend(resultados)
            total_series += len(resultados)

            if pagina_atual >= data.get("total_pages", 1):
                break
        else:
            print("Erro ou fim dos resultados.")
            break

        pagina_atual += 1

    # Salva as séries em arquivos JSON e enviar para o S3
    while len(todas_series) > 0:
        nome_do_arquivo = f"RAW/TMDB/JSON/{ano}/{mes:02d}/{
            dia:02d}/series_de_drama_2000_a_2020_{file_index}.json"
        registros_para_salvar = todas_series[:100]

        # Convertendo para JSON
        json_data = json.dumps(registros_para_salvar,
                               ensure_ascii=False, indent=4)

        # Enviar para o S3
        s3_client.put_object(
            Bucket=s3_bucket,
            Key=nome_do_arquivo,
            Body=json_data,
            ContentType='application/json'
        )

        print(f"{len(registros_para_salvar)
                 } registros salvos em {nome_do_arquivo}")

        # Remover as séries já salvas
        todas_series = todas_series[100:]
        file_index += 1

    return {
        'statusCode': 200,
        'body': json.dumps({"message": "Processamento completo"})
    }
