# **Etapas do Desafio**

## 0. Comecei o desafio instalando as bibliotecas do Pandas e do Matplotlib no VSCode, pois já havia instalado a extensão do jupyter.
$$
![passo_0_p1](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2003/Evidencias/passo_0_Instalando_o_pandas.png)
##
![passo_0_p2](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2003/Evidencias/passo_0_parte_2_instalando_o_matplotlib.png)
##

## 1. Lendo o Arquivo e Removendo as linhas duplicadas
### Após a instalação das bibliotecas, fiz a importação delas e também importei o submodulo mticker da biblioteca matplotlib que serve para personalizar os ticks dos eixos no gráfico(utilizado na etapa 2 e etapa 8), e li o arquivo 'csv' com o comando 'pd.read_csv' e criei uma variavel chamada 'dataset' para armazenas as informações.
### Logo após isso removi as linhas duplicadas por App, que foi o que considerei mais lógico, e como podemos ver, o resultado foi que sai de 10841 linhas para 9660. 
### Usei o comando 'display', que serve como um print do pandas, ele torna a visualização do dataset melhor, por isso preferi utiliza-lo no lugar do print.
##
![passo_1](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2003/Evidencias/Passo%2001%20-%20Lendo%20o%20arquivo%20e%20eliminando%20linhas%20duplicadas.png)
##

## 2. Criação do Gráfico de Barras
### Comecei essa etapa ordenando o dataset em ordem decrescente utilizando o comando sort_values(by='App', ascending='False'), e vi que havia uma linha fora do padrão e que a coluna de instalações não estava no tipo númerico, então removi a linha  fora de padão com o comando drop passando o index da linha e transformei a coluna 'Installs' para valores númericos conforme mostra a imagem.
## 
![passo_2_p1](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2003/Evidencias/passo_02_grafico_de_barras_parte_1.png)

### Após a remoção da linha e conversão da coluna pra tipo númerico, fiz o Gráfico de barras com os 5 Apps mais instalados. <br> Decidi criar uma função para formatar os valores no eixo y, pra melhorar a compreensão do gráfico, e usei o comando head(5) para puxar apenas os 5 primeiros apps do dataset.
##
![passo_2_p2](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2003/Evidencias/passo_02_grafico_de_barras_parte_2.png)
##

## 3. Criar o Gráfico de Pizza(pie chart) das categorias por frequência.
### Como eu já havia removido as duplicatas e ordenado o dataset, a unica coisa que me deu mais trabalho aqui foi criar a catergoria 'Others' pra melhorar a visualização do meu gráfico de pizza, criei um tipo de filtro para fazer isso, definindo um valor limite de instalações para ter sua própria categoria, os que tinham abaixo de 170 instalações entraram na categoria 'Others', escolhi o valor 170 com base em testes, até achar um valor que me agradou com o resultado. <br> Algo de diferente que também fiz, foi criar esse 'explode' que destaca a categoria que mais apareceu no dataset
##
![passo_3](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2003/Evidencias/passo_03_grafico_de_pizzas.png)
##

## 4. Mostrar qual o App mais caro no dataset.
### Comecei verificando o tipo da coluna, e vi que estava como objeto, então transformei em número, desta vez utilizando uma função, também ordenei a função em ordem decrescente utilizando o comando sort_values(by='Price', ascending =False) e usei o comando head(1), pra puxar o App mais caro.
##
![passo_4](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2003/Evidencias/passo_04_app_mais_caro.png)
##

## 5. Mostrar quantia de Apps classificados como 'Mature 17+'.
### Para puxar apenas os apps classificados como 'Mature 17+' criei uma variavel que usei de filtro pra 'palavra' que eu queria e utilizei o count(), para ver quantas vezes 'Mature 17+' aparece no dataset.
##
![passo_5](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2003/Evidencias/passo_05_quantia_apps_mature17%2B.png)
##


## 6. Mostar o top 10 Apps por número de 'Reviews'
### Mais uma vez comecei verificando o tipo da coluna, que também estava como objeto, desta vez usei o comando pd.to_numeric(), após a conversão utilizei o comando sort_values() para ordernar o dataset em ordem decrescente por reviews e head(10) pra puxar as 10 primeiras linhas.
##
![passo_6](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2003/Evidencias/passo_06_apps_por_numero_de_reviews.png)
##

## 7. Criar 2 Cálculos sobre o dataset um em formato de lista, e outro em formato de valor
### O primeiro cálculo que escolhi foi o de 5 notas(Rating) mais frequentes no dataset, pois achei que estava faltando algum cálculo relacionado as avaliações dos apps, e é uma métrica que pode nos dar uma noção de como estão classificados a maioria dos aplicativos. <br> Já o segundo cálculo eu decidi fazer uma média geral dos aplicativos, para complementar o meu primeiro cálculo.
##
![passo_7](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2003/Evidencias/passo_07_criando_2_calculos_sobre_o_dataset.png)
##

## 8. Criar 2 novos gráficos em cima do dataset.
### Para os 2 gráficos, escolhi fazer um gráfico de barras horizontal sobre as reviews por aplicativo, e um histograma, pra complementar ainda mais meu cálculo sobre a frequência das avaliações.<br> No primeiro gráfico utilizei uma função novamente para persolizar os valores do eixo x no gráfico de barras horizontal, e usei o comando plt.gca().invert_yaxis() para deixar o gráfico na ordem decrescente, também utilizei o comando dropna() para remover valores 'NaN' caso houvesse algum.
##
![passo_8_p1](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2003/Evidencias/passo_08_criando_2_outros_graficos_parte_1.png)

### Já o segundo gráfico foi bem simples, usei somente os comandos básicos assim como fiz nos outros gráficos: <br> Comandos Básicos: <br> plt.hist - pra defini-lo como histograma <br> plt.figure - pra definir o tamanho da figura <bt> plt.title - para definir o título <br> plt.xlabel - para definir o nome do eixo x <br> plt.ylabel - para definir o nome do eixe y <br >plt.show() - para mostrar o gráfico <br>

##
![passo_8_p2](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2003/Evidencias/passo_08_criando_2_outros_graficos_parte_2.png)
##













