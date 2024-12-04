## Etapas do Desafio:
### Preciso dizer que tive etapas bem parecidas para criação do parquet tanto do CSV quanto do Json, com algumas pequenas diferençãs no Job feito no Glue de cada um, com isso dito

## Etapa 1
### Comecei o desafio criando os jobs tanto pro csv quanto pro json
### CSV:
![passo_1_csv](../../Sprint%2008/Evidencias/parquet-csv/passo_01_job_csv_criado.png)
### Json:
![passo_1_json](../../Sprint%2008/Evidencias/parquet-json/passo_01_job_json_criado.png)
##

## Etapa 2
### Após a criação dos Jobs no glue, alterei os "job details" para ambos
### CSV:
![passo_2_csv](../../Sprint%2008/Evidencias/parquet-csv/passo_02_alterando_os_job_details.png)
### Json:
![passo_2_json](../../Sprint%2008/Evidencias/parquet-json/passo_02_alterando_os_detalhes_do_jog.png)
##

## Etapa 3
### Na terceira etapa, comecei a criar o script de ambos os jobs, importando as bibliotecas necessárias:
### CSV:
![passo_3_csv](../../Sprint%2008/Evidencias/parquet-csv/passo_03_import_das_bibliotecas.png)
### Json:
![passo_3_json](../../Sprint%2008/Evidencias/parquet-json/passo_03_import_das_bibliotecas.png)
##

## Etapa 4
### Após isso, passei os argumentos
### CSV:
![passo_4_csv](../../Sprint%2008/Evidencias/parquet-csv/passo_04_passando_argumentos.png)
### Json:
![passo_4_json](../../Sprint%2008/Evidencias/parquet-json/passo_04_passando_argumentos.png)
##

## Etapa 5
### Nesta etapa, os códigos ainda estavam bastante similares, então depois de passar os argumentos, passei o caminho de leitura de ambos, porém no arquivo Json, fiz uma conversão para dynamicFrame, pois estava dando erro na leitura do Json, apenas com o Spark.
### CSV:
![passo_5_csv](../../Sprint%2008/Evidencias/parquet-csv/passo_05_caminho_e_leitura_do_csv.png)
### Json:
![passo_5_json](../../Sprint%2008/Evidencias/parquet-json/passo_05_caminho_e_leitura_do_json_e_conversao.png)
##

## Etapa 6
### Na proxima parte foi onde mais tive diferenças entre os códigos, pois para cada arquivo eu precisei fazer alterações específicas, então vou explicar um de cada vez
### CSV:
### Para o CSV, eu removi diversas colunas da minha seleção, pois não iria utiliza-las, como por exemplo, qualquer coluna relacionada aos artistas, eu decidi por não puxar para a criação do parquet, pois não vou ter uso para elas nas análises que pretendo fazer.
### Além da seleção de colunas específicas, também corrigi o nome de uma coluna, que estava como "tituloPincipal", então corrigi para "tituloPrincipal", também fiz a transformação de algumas que colunas que estavam no formato de string para int, e a das notas médias para float.
![passo_6_csv](../../Sprint%2008/Evidencias/parquet-csv/passo_06_tratando_alguns_dados_e_colunas_selecionadas.png)
##

### Json:
### Já para o Json, tive mais tratamentos a serem feitos, pois na etapa Raw ele puxou as seasons(temporadas), detalhadamente, e eu só desejava o número de temporadas.
### Comecei escrevendo uma linha para lidar com cada série individualmente, pois as temporadas estavam aninhadas, e na hora da criação do parquet e na visualização das tabelas estava tendo alguns problemas. 
### Após isso escrevi algumas linhas para não puxar as temporadas onde não havia data de lançamento(air_date estava 'null'), pois eram temporadas que ainda não haviam sido lançadas, portanto não as contei, também não considerei temporadas que estavam com nomes de "Especial", pois não são temporadas em sí e não queria considerar isso como temporada para minhas análises, para verificar se o número de temporadas estavam corretas, pesquisei algumas séries no google e em serviços de streaming, e vi que batiam os números apresentados nas tabelas, com as pesquisas que fiz no google ou em serviços de streaming que tenho acesso.
### Na linha de codigo seguinte, também removi as séries que ainda não foram ao ar.
### Selecionei as colunas que desejava para minha análise e para coluna gênero defini todos como drama, já que todas elas tem a classificação de drama.
### E para finalizar essa etapa de código, removi as duplicatas.
![passo_6_json](../../Sprint%2008/Evidencias/parquet-json/passo_06_tratando_os_arquivos.png)
##

## Etapa 7
### Após o código de seleção das colunas e tratamento e transformação dos dados, eu escrevi algumas linhas para passar o caminho onde desejava que os arquivos parquet fossem salvos.
### Para ambos eu fiz um código puxando o datetime e passando o caminho pra cada arquivo, a diferença ficou na parte que tive que usar o glue context para o arquivo Json, por ter utilizado o dynamicFrame.
### CSV:
![passo_7_csv](../../Sprint%2008/Evidencias/parquet-csv/passo_07_data_e_caminho_para_salvar_o_parquet.png)
## 
![passo_8_csv](../../Sprint%2008/Evidencias/parquet-csv/passo_08_salvando_para_parquet_e_job_commit.png)
### Json:
![passo_7_json](../../Sprint%2008/Evidencias/parquet-json/passo_07_conversao_e_caminho_para_salvar_em_parquet.png)
##

## Etapa 8
### Com o código todo feito, rodei o job, claro que não acertei o script de primeira, então tive que ir fazendo alterações, mas ambos rodaram com sucesso, com os scripts apresentados acima, e aqui estão as evidências do job executado:
### CSV:
![passo_9_csv](../../Sprint%2008/Evidencias/parquet-csv/passo_09_job_executado_com_sucesso.png)
### Json
![passo_8_json](../../Sprint%2008/Evidencias/parquet-json/passo_08_job_rodou_com_sucesso.png)
##

## Etapa 9
### Após a execução dos jobs, rodei o crawler para criar as tabelas dos arquivos parquet de cada um dos arquivos originais, também rodaram com sucesso, como podem ver a seguir:
### CSV:
![passo_10_csv](../../Sprint%2008/Evidencias/parquet-csv/passo_10_rodando_o_crawler_para_executar_a_tabela_csv.png)
### Json:
![passo_9_json](../../Sprint%2008/Evidencias/parquet-json/passo_09_rodando_o_crawler_para_criar_as_tabelas.png)
##

## Etapa 10
### Confirmando que as tabelas tinham sido criadas corretamente.
### CSV:
![passo_11_csv](../../Sprint%2008/Evidencias/parquet-csv/passo_11_tabela_gerada_pelo_crawler_csv.png)
### Json:
![passo_10_json](../../Sprint%2008/Evidencias/parquet-json/passo_10_tabela_gerada_pelo_crawler_json.png)
##

## Etapa 11
### Com a confirmação das tabelas criadas, resolvi rodar uma query para verificar os resultados no AWS Athena, e ver se estava tudo de acordo com o que eu queria.
### CSV:
![passo_12_csv](../../Sprint%2008/Evidencias/parquet-csv/passo_12_tabela_verificada_no_AWS_Athena.png)
### Json:
![passo_11_json](../../Sprint%2008/Evidencias/parquet-json/passo_11_tabela_verificada_no_AWS_Athena.png)
##

## Etapa 12
### Após tudo isso, tendo feito todas as verificações necessárias, e o desafio ter sido concluído com sucesso, só me restou confirmar que os caminhos estavam corretos, e estavam conforme podem ver a seguir:
### CSV
![passo_13_csv](../../Sprint%2008/Evidencias/parquet-csv/passo_13_caminho_resultante_parquet-csv.png)
### Json:
![passo_12_json](../../Sprint%2008/Evidencias/parquet-json/passo_12_caminho_resultante_parquet-json.png)
##

## Minha Análise:
### Minhas análises se mantém inalteradas desde a ultima sprint.

## E esse foi o meu desafio da Sprint 8!