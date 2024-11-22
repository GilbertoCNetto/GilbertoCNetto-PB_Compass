import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TMDB_KEY")


def series_de_drama_durante_os_anos(api_key, ano_inicial, ano_final, page=1):
    """Busca séries de TV do gênero Drama entre os anos de 2000 e 2020 no idioma pt-BR."""
    url_padrao = "https://api.themoviedb.org/3"
    url_series = "discover/tv"
    url_final = f"{url_padrao}/{url_series}"

    # Parâmetros para filtro por gênero, período e idioma
    params = {
        "api_key": api_key,
        "with_genres": "18",  # ID do gênero Drama
        "first_air_date.gte": f"{ano_inicial}-01-01",  # Data de início
        "first_air_date.lte": f"{ano_final}-12-31",  # Data de término
        "page": page,
        "language": "pt-BR"  # Idioma dos resultados
    }

    try:
        response = requests.get(url_final, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao chamar à API: {e}")
        return None


def detalhes_das_series(api_key, series_id):
    """Busca detalhes adicionais de uma série, incluindo status e número de temporadas."""
    url_padrao = "https://api.themoviedb.org/3"
    url_details = f"tv/{series_id}"
    url_final = f"{url_padrao}/{url_details}"

    # Parâmetros para obter detalhes da série
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


def salvar_series_para_json(series_data, file_name):
    """Salva as séries em um arquivo JSON."""
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(series_data, f, ensure_ascii=False, indent=4)
    print(f'{len(series_data)} registros salvos em {file_name}')


def selecionar_series(api_key, ano_inicial, ano_final, limite_de_series=300):
    """Função principal que busca todas as séries e as salva em arquivos JSON."""
    total_series = 0
    pagina_atual = 1
    todas_series = []
    file_index = 1

    while total_series < limite_de_series:
        # Buscar séries por página
        data = series_de_drama_durante_os_anos(
            api_key, ano_inicial, ano_final, pagina_atual)

        if data:
            resultados = data.get("results", [])
            falta_para_300 = limite_de_series - total_series

            # Limita os resultados ao que ainda falta coletar
            resultados = resultados[:falta_para_300]

            # Buscar detalhes de cada série
            for serie in resultados:
                series_id = serie['id']
                detalhes = detalhes_das_series(api_key, series_id)

                if detalhes:
                    # Adiciona o status da série
                    serie['status'] = detalhes.get('status', 'Desconhecido')
                    serie['seasons'] = detalhes.get('seasons', [])

            todas_series.extend(resultados)  # Adiciona os resultados à lista
            # Atualiza o contador de séries coletadas
            total_series += len(resultados)

            # Salvar em arquivo quando atingir o limite de 100 registros por arquivo
            while len(todas_series) >= 100:
                nome_do_arquivo = f"series_de_drama_2000_a_2020_{
                    file_index}.json"
                salvar_series_para_json(todas_series[:100], nome_do_arquivo)

                # Remove as séries já salvas da lista
                todas_series = todas_series[100:]
                file_index += 1

            # Verifica se já percorremos todas as páginas disponíveis
            if pagina_atual >= data.get("total_pages", 1):
                break
        else:
            print("Erro ou fim dos resultados.")
            break

        pagina_atual += 1

    # Salvar séries restantes (menos de 100 registros) no último arquivo
    if todas_series:
        nome_do_arquivo = f"series_de_drama_2000_a_2020_{file_index}.json"
        salvar_series_para_json(todas_series, nome_do_arquivo)

    print(f"\nTotal de séries coletadas: {total_series}")


if __name__ == "__main__":
    # Definir intervalo de datas (2000 a 2020)
    ano_inicial = 2000
    ano_final = 2020

    # Limite total de séries a buscar
    selecionar_series(api_key, ano_inicial, ano_final, limite_de_series=300)
