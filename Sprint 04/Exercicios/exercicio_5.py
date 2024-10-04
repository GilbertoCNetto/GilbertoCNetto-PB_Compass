import csv

def processar_notas():
    with open('estudantes.csv', 'r') as arquivo_csv:
        ler_csv = csv.reader(arquivo_csv)
        estudantes = []
        for linha in ler_csv:
            nome = linha[0]
            notas = list(map(int, linha[1:]))
            maiores_notas = sorted(notas, reverse=True)[:3]
            media_geral = round(sum(maiores_notas) / 3, 2)
            estudantes.append((nome, maiores_notas, media_geral))

        estudantes_ordenados = sorted(estudantes, key=lambda x: x[0])
        for estudante in estudantes_ordenados:
            nome, maiores_notas, media_geral = estudante
            print(f"Nome: {nome} Notas: {maiores_notas} Média: {media_geral}")

processar_notas()
