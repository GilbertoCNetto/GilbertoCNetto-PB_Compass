## Etapas do Desafio:
##

## Etapa 1
### Comecei meu desafio importando as tabelas do athena, conforme foi indicado no pdf do desafio, e após a importação, fiz um tipo de join nas tabelas, e o resultado obtido foi esse:
![tabelas](../../Sprint%2010/Evidencias/passo_01_tabelas_importadas.png)
##

## Etapa 2
### Após fazer alguns testes criando alguns gráficos que não iria utilizar, mudei as perguntas da minha análise para as seguintes perguntas
### OBS: Filtrei para que apenas as séries com o 'vote_count' acima de 5 mil fossem analisadas, pois quanto maior a amostra de votos, mais precisa será a a análise e mais confiável serão os resultados.
### Quais as séries com ao menos 5 mil votos a partir do ano de 2000 até 2010?
### Quais as séries com ao menos 5 mil votos a partir do ano de 2011 até 2020?
### Houve algum aumento na produção ou na qualidade das séries entre os períodos analisados acima?
### Quais as 10 melhores séries com base nas notas?
### Quais as séries mais longas?
### Quais as melhores séries com base nas notas com ao menos 10 temporadas?

## Etapa 3
### Finalizadas as perguntas que eu gostaria de responder, comecei a construir meus gráficos, iniciei criando o gráfico para verificar as séries dos anos de 2000 à 2010, para criar esse gráfico tive que criar um campo calculado, puxando apenas esse período específico de tempo e o resultado obtido foi esse:
![graf_1](../../Sprint%2010/Evidencias/passo_02_series_2000-2010.png)

## Etapa 4
### Nesta etapa, criei o mesmo gráfico, porém para o período seguinte, de 2011 à 2019, também criando um campo calculado para esta etapa, e esse foi o resultado: 
![graf_2](../../Sprint%2010/Evidencias/passo_03_series_2011-2019.png)
### Analisando os dois gráficos e comparando-os, é possível visualizar o aumento na produção de séries e o aumento da contagem de votos, e podemos deduzir a partir disso, que conforme o acesso a serviços de streaming foram sendo criados a partir da década de 2010, se tornou mais fácil e simples o acesso a séries para a população, o que aumentou a quantia de séries sendo avaliadas, e a produção também aumentou. 
### Também podemos observar, que a popularidade e a contagem de votos demonstrou uma correlação maior nos anos 2000, enquanto de 2010 em diante, ouve uma correlação entre a quantia de séries e os votos, por exemplo em 2018, tivemos a série de maior popularidade do gráfico, sendo "CoBra Kai", mas a quantidade de votos não foi tão expressiva quanto no ano de 2017 e 2018, que tiveram mais séries sendo lançadas nesses anos.

## Etapa 5
### Na etapa 5, fiz o gráfico com as 10 melhores séries, com base nas maiores notas, também com o filtro de votos acima de 5 mil, igual usei em todos os outros gráficos do meu dashboard.
![graf_3](../../Sprint%2010/Evidencias/passo_04_top_10_series_nota.png)
### Como podemos ver, a melhor série de acordo com as notas foi "Breaking Bad", que é uma série de 2008, então também foi a melhor série da década, e em segundo lugar, temos "Better Call Saul", que é uma série derivada de Breaking Bad, e foi a melhor série da sua década também, já que estreou em 2015, o que é muito interessante, pois as duas se passam no mesmo universo e também tem o mesmo produtor.
### Também podemos tirar a informação de que das 10 melhores séries, 5 foram produzidas pela netflix, sendo elas, Stranger things, The Umbrella Academy, Peaky Blinders, Riverdale e Dark.
### Portanto, para pessoas interessadas em séries de qualidade, e que não tem interesse em pagar por vários serviços de streaming, podemos dizer que a Netflix ainda mantém um catalogo bem robusto e variado. 

## Etapa 5
### Após verificar quais são as melhores séries, criei o gráfico para ver quais eram as séries mais longas, para pessoas que gostam de séries mais longas.
![graf_4](../../Sprint%2010/Evidencias/passo_05_series_mais_longas.png)
### Destaque especial para Grey's Anatomy, sendo a série com maior números de temporadas.
##

## Etapa 6
### E na ultima etapa, puxei as séries com ao menos 10 temporadas, ordenadas por notas, para sabermos quais as melhores séries longas, de acordo com as notas.
![graf_5](../../Sprint%2010/Evidencias/passo_06_melhores_series_longas.png)
### A partir desse gráfico, é possivel concluir que a melhor série com ao menos 10 temporadas é "Supernatural", com uma pequena margem para Grey's Anatomy 
##

## Dashboard Completo
![dash](../../Sprint%2010/Evidencias/dash.png)