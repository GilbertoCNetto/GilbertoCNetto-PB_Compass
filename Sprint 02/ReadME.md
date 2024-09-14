## Cursos:

Nesta Sprint, o nosso foco era SQL e AWS, com os cursos de SQL para Análise de Dados: Do básico ao avançado e o curso AWS Partner: Sales Accreditation

#### SQL:
#### Eu havia utilizado o SQL umas 2 ou 3 vezes no máximo, então não conhecia muito bom, mas gostei bastante do curso, e dessa sprint como um todo, foi muito gratificante e recompensador resolver o desafio e aprender e práticar SQL.
Alguns comandos que acho importante ressaltar são:
* SELECT - Útil para fazer seleção de colunas de tabelas que queremos visualizar;
* FROM - Seleciona a tabela que estamos querendo utilizar;
* JOIN - Faz um tipo de união de uma tabela pra outra, para puxar dados de outras tabelas, já que o FROM só nos permite selecionar uma tabela;
* GROUP BY - Agrupa por uma tabela específica; 
* ORDER BY - Ordena por uma tabela específica;
* WHERE - Indica um tipo de condição, que desejamos na nossa busca;
* CREATE TABLE - Usado para criar tabelas;
* INSERT - Insere dados desejados numa tabela;
* INTEGER -  Wrapper classe que encapsula um tipo primitivo e fornece alguns métodos de conversão;
* PRIMARY KEY - Chave primária de uma tabela;
* FOREIGN KEY - Relaciona uma tabela a outra a partir de uma coluna;
* COUNT - Conta quantas vezes aparece um X parâmetro na coluna por exemplo;
* SUM - Soma o valor total de X parâmetro na coluna;
* AVG - Faz uma média de X valor desejado. 

#### AWS:
#### Até essa sprint, eu apenas tinha ouvido falar sobre AWS, porém nunca havia estudado sobre o assunto, gostei do curso, achei uma boa introdução sobre AWS, estou animado para ver os próximos passos e aprender sobre a parte prática dessa tecnologia.

## Evidências:
#### Gostaria de evidênciar os diagramas referentes a modelagem relacional(normalizada) e a modelagem dimensional.
#### Modelagem Relacional:

![Modelagem Relacional](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2002/Evidencias/Diagrama_modelagem_relacional.png)

#### Modelagem Dimensional:

![Diagrama Modelagem Dimensional](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2002/Evidencias/Diagrama_modelo_dimensional_star_schema.png)

#### Escolhi o modelo Star Schema por ter menos complexidade de Querys e também por não ter suas dimensões normalizadas, o que torna mais simples a análise desses dados, principalmente devido a sua estrutura simples e de baixa manutenção.

## Exercícios:
#### Sobre os exercícios dessa sprint, eu gostei bastante, tinham um nivel de dificuldade agradável, e foram proveitosos pro meu aprendizado, em conjunto com o curso SQL, sinto que realmente consigo me desdobrar em SQL hoje.
#### Exemplo(exercício-10):
``` SQL
  select
      tvd.nmvdd as vendedor, 
      sum(tbv.qtd * tbv.vrunt) as valor_total_vendas, 
      round(sum(tbv.qtd * tbv.vrunt) * tvd.perccomissao / 100, 2) as comissao
  from tbvendas tbv
  join tbvendedor tvd on tbv.cdvdd = tvd.cdvdd
  where tbv.status = 'Concluído'
  group by tvd.nmvdd
  order by comissao desc;
```

## Certificado:
![Certificado AWS](https://github.com/user-attachments/assets/e2753ea5-e5ed-4d33-8545-038078110130)

