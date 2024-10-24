
# **Etapas do Desafio**

## 1. Começei o desafio escrevendo um script para criar o Bucket no s3 e subindo o arquivo CSV escolhido para o Bucket.
![p1](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_1_criando_o_bucket.png)
##

## 2. Após criar o Bucket e subir o arquivo, criei um novo script chamado 'conexao.py', e comecei importando as bibliotecas e fazendo a conexão do script ao s3, e lendo o arquivo com a funlçao read_csv do pandas.
![p2](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_2_import_das_bibliotecas_conexao_s3_e_read_csv.png)
##

## 3. Minha terceira etapa foi criar uma função usando dois operadores lógicos, no qual defini um tanto de chegadas para certas classificações de chegadas no país entre alta, baixa e média.
![p3](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_3_clausula_usando_dois_operadores_logicos.png)
##

## 4. Logo após fiz uma função de conversão para melhorar a visualização dos estados usando o 'map' do pandas e criando um dicionário com as 'UFS' e substituindo suas respectivas posições.
![p4](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_4_funcao_de_conversao.png)
##

## 5. Em seguida, criei uma função de string com a intenção de deixar a coluna 'Continente' toda em maiaúsculo e transforormar a coluna 'Páis' em 'title' e fazer um 'strip' na coluna continente.
![p5](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_5_funcao_de_string.png)
##

## 6. Após a função de string, eu fiz uma função para data, pois o dataset não tinha datas exatas.
![p6](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_6_funcao_de_data.png)
##

## 7. Então decidir utilizar uma função condicional para filtrar os países que não tinham voos, para reduzir o número de linhas em uma tabela com o dataset filtrado.
![p7](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_7_funcao_condicional.png)
##

## 8. Para finalizar a parte de tratamento e visualização dos dados fiz duas funções de agregação, a primeira, para retirar insights contendo a soma de chegadas por páis, e uma média, já a segunda foi para fazer uma contagem de chegadas por continentes, foi possivel perceber que as pessoas que mais vem para o Brasil, são do continente Europeu.
![p8](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_8_duas_funcoes_de_agregacao.png)
##

## 9. Após toda a etapa de criação das funções, dei um print pra poder visualizar o resultado.
![p9](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_9_criando_variaveis_pra_cada_tabela_e_printando_o_resultado.png)
##
## E o resultado obtido foi esse:
![image](https://github.com/user-attachments/assets/65e2df7d-7555-4f0b-bc3b-9706054a7ca7)


## 10. Em seguida, subi todos os CSVs criados, para o bucket com o seguinte codigo:
![p10](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_10_salvando_localmente_os_csv_e_subindo_pro_s3.png)
##

## 11. Como é possivel visualizar, o Bucket foi criado com sucesso no S3.
![p11](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_11_verificando_o_bucket_criado.png)
##

## 12. Os arquivos CSV, também foram carregados corretamente para o Bucket.
![p12](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_12_verificando_os_arquivos_csv_upados_no_s3.png)
##

## 13. Finalmente parti para a última etapa, que era a de deletar o Bucket, porém, não foi possivel deletar o Bucket direto, primeiro precisei deletar os CSVs, e foi isso que eu fiz, como é possivel ver na imagem a seguir:
![p13](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_13_deletando_os_arquivos_csv.png)
##

## 14. Após deletar os arquivos, deletei o Bucket.
![p14](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_14_deletando_o_bucket_do_s3.png)
##

## 15. Imagem do Bucket deletado com sucesso.
![p15](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_15_bucket_deletado_com_sucesso.png)
##


