## Etapas do Desafio:
##

## Etapa 1
### Comecei o desafio criando um arquivo para um tipo de staging area, onde iria criar um arquivo que puxaria somente as séries em comum dos arquivos parquet da camada trusted.
### Iniciei o script, importando as bibliotecas necessárias, e passando os parâmetros do job.
![passo](../../Sprint%2009/Evidencias/series_em_comum/passo_01_import_das_biblio_e_parametros.png)
##

## Etapa 2
### Puxando os arquivos parquet da camada trusted, para filtrar somente as séries em comum.
![passo](../../Sprint%2009/Evidencias/series_em_comum/passo_02_puxando_os_arquivos_da_trusted.png)
##

## Etapa 3
### Transformando os arquivos em dynamic frame e selecionando as colunas que foram comparadas para achar as séries em comum.
![passo](../../Sprint%2009/Evidencias/series_em_comum/passo_03_conversao_e_colunas_chave.png)
##

## Etapa 4
### Nesta etapa fiz a filtragem a partir das colunas definidas como key acima, e também criei um id com auto-incremento pois não puxei na api do tmdb, e também tratei para que o id ficasse na primeira posição. 
![passo](../../Sprint%2009/Evidencias/series_em_comum/passo_04_filtrando_e_coluna_id.png)
##

## Etapa 5
### A seguir, puxei o datetime e passei o caminho, salvando o arquivo como parquet em um diretório que criei, chamado staging area.
![passo](../../Sprint%2009/Evidencias/series_em_comum/passo_05_salvando_o_parquet_series_em_comum.png)
##

## Etapa 6
### Executei o job com sucesso.
![passo](../../Sprint%2009/Evidencias/aws/passo_01_job_series_em_comum_executado.png)
##

## Etapa 7
### Verifiquei o caminho, para ver que o arquivo foi salvo corretamente como parquet e no local correto.
![passo](../../Sprint%2009/Evidencias/aws/passo_02_verificando_o_caminho_series_comum.png)
##

## Etapa 8
### Também criei e executei um crawler para poder verificar o resultado do arquivo criado.
![passo](../../Sprint%2009/Evidencias/aws/passo_03_crawler_series_em_comum_executado.png)
##

## Etapa 9
### Após o Crawler executado, verifiquei pelo AWS Athena a tabela das séries em comum dos 2 arquivos parquet da camada trusted e como resultado, obtive 178 séries em comum. 
![passo](../../Sprint%2009/Evidencias/aws/passo_04_query_verificando_quantia_de_series_em_comum.png)
##

## Etapa 10
### Terminando a etapa da criação do arquivo das séries em comum, comecei a escrever meu script da modelagem dimensional.
### Novamente importando as bibliotecas necessárias.
![passo](../../Sprint%2009/Evidencias/modelagem_dimensional/passo_01_import_das_biblio_e_parametros.png)
##

## Etapa 11
### Continuei puxando o arquivo das séries em comum, e tratando a data, pois estava como string, então tive que transformar em "date"
![passo](../../Sprint%2009/Evidencias/modelagem_dimensional/passo_02_puxando_series_em_comum_e_tratando_a_data.png)
##

## Etapa 12
### Após puxar o arquivo e tratar a data, criei as tabelas que considerei necessárias, e criei também os ids com o "monotonically_increasing_id()" para as tabelas que não tinha os ids.
### Sobre a modelagem dimensional, dei preferência a usar a função "spark.sql" para poder fazer essa etapa toda em SQL puro, pois achei mais prático, além de que, fica mais simples para alguém que não conhece o pyspark entender o código, e como eu já havia feito a modelagem dimensional em SQL antes, decidi por fazer do mesmo modo nesta etapa do desafio.
### Para os ids que não existiam criei com o "monotonically_increasing_id()" e puxei as colunas do arquivo séries em comum para cada tabela que eu achei ser melhor, e que fazia sentido no meu ponto de vista.
![passo](../../Sprint%2009/Evidencias/modelagem_dimensional/passo_03_criação_das_tabelas_da_modelagem.png)
##

## Etapa 13
### Logo em seguida, fiz um código para escrever e salvar cada uma das tabelas em parquet, na camada REFINED utilizando do glueContext.
![passo](../../Sprint%2009/Evidencias/modelagem_dimensional/passo_04_escrevendo_as_tabelas_em_parquet.png)
##

## Etapa 14
### Job da modelagem dimensional executado com sucesso.
![passo](../../Sprint%2009/Evidencias/aws/passo_05_job_modelagem_dimensional_executado.png)
##

## Etapa 15
### Verificiando o caminho dos arquivos salvos, cada um dentro de seu próprio diretório.
![passo](../../Sprint%2009/Evidencias/aws/passo_06_verificando_caminho_dimensionamento_pos_job.png)
### dim_origem:
![dim_origem](../../Sprint%2009/Evidencias/modelagem_dimensional/dim_origem.png)
### dim_serie:
![dim_serie](../../Sprint%2009/Evidencias/modelagem_dimensional/dim_serie.png)
### dim_tempo:
![dim_tempo](../../Sprint%2009/Evidencias/modelagem_dimensional/dim_tempo.png)
### dim_votos:
![dim_votos](../../Sprint%2009/Evidencias/modelagem_dimensional/dim_votos.png)
### fato_series:
![fato_series](../../Sprint%2009/Evidencias/modelagem_dimensional/fato_series.png)
##

## Etapa 16
### Executando um Crawler para criar cada uma das tabelas, e poder assim, fazer a verificação do resultado obtido, no AWS Athena
![passo](../../Sprint%2009/Evidencias/aws/passo_07_crawler_modelagem_executado.png)
##

## Etapa 17
### Verificando as tabelas no Athena
##
### Tabela dim_origem verificada:
![passo](../../Sprint%2009/Evidencias/aws/passo_08_tabela_dim_origem.png)
### Tabela dim_serie verificada:
![passo](../../Sprint%2009/Evidencias/aws/passo_09_tabela_dim_serie.png)
### Tabela dim_tempo verificada:
![passo](../../Sprint%2009/Evidencias/aws/passo_10_tabela_dim_tempo.png)
### Tabela dim_votos verificada:
![passo](../../Sprint%2009/Evidencias/aws/passo_11_tabela_dim_votos.png)
### Tabela fato_series verificada:
![passo](../../Sprint%2009/Evidencias/aws/passo_12_tabela_fato_series.png)
##

## Etapa 18
### Na ultima etapa do desafio, criei o diagrama da modelagem dimensional feita no diagramdb.
![passo](../../Sprint%2009/Evidencias/aws/Modelagem-Dimesional-Series.png)
##

### E esse foi o meu desafio da sprint 9!