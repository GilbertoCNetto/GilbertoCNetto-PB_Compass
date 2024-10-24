# Sobre o Conjunto de Dados:
## Esse é um conjunto de dados sobre a tributação e competência do país, entre os anos de 2002 e 2021, nele podemos encontrar o valor tributado por cada orçamento e Descrição(Inss, IPVA, IPTU, ICMS e por ai em diante) e qual a porcentagem daquele tributo, assim como se ele é um tributo do governo federal, municipal ou estadual. Escolhi esse conjunto pois gosto bastante da área financeira, e me dou bem com números em geral, e achei esse conjunto interessante de se trabalhar.

![amostra](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/amostra_do_conjunto_de_dados.png)

##
# **Etapas do Desafio**

## 1. Começei o desafio escrevendo um script 'bucket.py' para criar o Bucket no s3 e subindo o arquivo CSV escolhido para o Bucket.
![p1](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_1_enviando%20arquivo_pro_s3.png)
##

## 2. Após criar o Bucket e subir o arquivo, criei um novo script chamado 'conexao.py', e comecei importando as bibliotecas e fazendo a conexão do script ao s3, e lendo o arquivo com a funlçao read_csv do pandas.
![p2](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_2_importando_bibliotecas_e_conexao_s3.png)
##

## 3. Minha terceira etapa foi criar parte das funções, sendo elas as funções de:
 * Função de data - Utilizei essa função para transformar o ano em data, pois só havia o ano no conjunto de dados original.
 * Função de conversão - Utilizei essa função para converter as colunas de 'Valor da Receita tributária' e de 'Percentual do PIB' em númerico, pois estavam com tipo de objeto, por conta da vírgula, então substitui por ponto.
 * Função de String - Essa função foi para deixar a coluna 'Descrição' toda em maiúsculo.
 * Função condicional - Para a função condicional, fiz uma função que cria uma nova coluna, e dependendo do valor percentual do pib, define aquela linha como 'Alta' ou 'Baixa'
![p3](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_3_criando_funcoes_parte_1.png)
##

## 4. O restante das funções exigidas foram as de:
 * Cláusula com dois operadores lógicos - Para esta cláusula, os operadores lógicos que escolhi foram o '==' para selecionar o ano de 2002, e o > para nos retornar apenas as linhas onde o Percentual do PIB fosse maior que 0.05.
 * Duas funções de agregação - E finalmente para as duas funções de agregação, fiz uma que nos mostrava valores ano a ano do valor da receita total, e uma média do percentual do pib por linha.
![p4](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_4_criando_funcoes_parte_2.png)
##

## Tabelas geradas a partir do script:
![resultado](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/resultados_do_codigo.png)

## 5. Print para verificar as tabelas mostradas acima, e subindo os arquivos para o s3 e salvando localmente os arquivos csv.
![p5](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/passo_5_print_e_subindo_para_o_s3.png)
##

## 6. Verificando que o bucket foi criado com sucesso e que os arquivos foram corretamente enviados para o s3.
### Bucket
![bucket](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/Bucket_criado.png)
##
### Arquivos
![arquivos](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2005/Evidencias/arquivos_corretamente_enviados_pro_s3.png)

## Link para a pasta com os arquivos CSV, tanto os gerados, quanto a base de dados escolhida
- [Pasta_Arquivos](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/tree/main/Sprint%2005/Desafio/Arquivos_CSV)
##
## Link para a pasta com os Scrips utilizados no Desafio
- [Pasta_Scripts](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/tree/main/Sprint%2005/Desafio/Scripts)

