# **Etapas do Desafio**

## 1. Criando repositório no Github.
#### Aqui o meu foco foi nos principais comandos do git, como por exemplo:
* git init - iniciar o git dentro da pasta;
* git add - para adicionar os arquivos que eu queria dar commit;
* git commit - para efetuar o upload dos arquivos pro repositório;
* git push - envia os arquivos de fato;
* git status - para verificar a condição dos aquivos, quais estavam selecionados.

#### Tive algumas dificuldades nessa etapa, pois estava ocorrendo algum conflito entre as pastas .git, porém com alguma pesquisa e ajuda do meu colega Rafael Nascimento Prado, descobrimos que se abrissemos o git bash a partir da pasta 'sprint 1' resolveria o problema, como de fato resolveu. 
  
![Criação do Repositório](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%201/Evidencias/Criando%20Reposit%C3%B3rio%20com%20Git(1).png)
![Criação do Repositório](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%201/Evidencias/Criando%20Reposit%C3%B3rio%20com%20Git(2).png)

## 2. Criando o diretório 'ecommerce' e inserindo 'dados_de_vendas.csv' nele.
#### Aqui usei o comando mkdir para criar o diretório 'ecommerce' e movi o arquivo 'dados_de_vendas' pelo explorador de arquivos do windows.

![ecommerce](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%201/Evidencias/Passo%201%20-%20Diret%C3%B3rio%20'ecommerce'%20e%20arquivo%20'dados_de_vendas%2Ccsv'.png)

## 3. Criando o arquivo'processamento_de_vendas.sh'.png.
#### Criei o arquivo utilizando o editor de textos 'nano'.

![processamento de vendas](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%201/Evidencias/Passo%202%20-%20Criar%20o%20executavel%20'processamento_de_vendas.sh'.png)

## 4. Tornando o arquivo executavel.
#### Para tornar o arquivo executavel, foi necessário usar o comando chmod.

![Tornando Executavel](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%201/Evidencias/Passo%203%20-%20Tornando%20o%20script%20um%20executavel.png)

## 5. Comandos para o executavel
#### Através do nano, passei os comandos desejados para o executavel:
* mkdir - para criar os diretórios;
* cp - para copiar arquivos de uma pasta pra outra;
* mv - tanto para mover arquivos quanto para renomea-los;
* date - pegar o tempo atual;
* =$ - Criar uma especie de variavel, na qual adicionei informações que iria inserir no relatório;
* echo - Utilizei para mostras as informações coletadas, acompanhadas de frases como por exemplo 'Primeiro registro';
* cat - Foi útil enquanto eu rodava o executavel por conta própria, para mostrar como estava ficando o relatório
* zip - para compressão dos dados de vendas
* rm - para apagar os antigos dados, para economizar memória.

#### É importante mencionar, que previamente a está etapa, eu testei a maioria desses comandos a mão, eu mesmo criando os diretórios, copiando e criando arquivos, movendo e renomeando, transformando em zip, tudo isso para ter uma noção básica de como utiliza-los, testes estes que estão no diretório 'evidências' dentro de um subdiretório chamado 'teste comandos pro arquivo executavel'.

![Comandos do executavel](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%201/Evidencias/Passo%204%20-%20Comandos%20pro%20executavel%20-%20final.png)

## 6. Iniciando, verificando status e criando o agendamento.
#### Nesta etapa tive que pesquisar como fazer agendamentos no Linux, e descobri o Cron e seus comandos:
* sudo service cron start - para iniciar o cron;
* sudo service cron status - para verificar se o cron está rodando;

  
![Iniciando e verificando status](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%201/Evidencias/Passo%205%20-%20Iniciando%20e%20verificando%20status%20do%20cron.png)

* crontab -e - para criar o agendamento, passando diversos parâmetros, na seguinte ordem (minutos - horas - dias do mês - mês - dias da semana);

![Criando agendamento](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%201/Evidencias/Passo%206%20-%20Criando%20agendamento%20com%20crontab%20-e.png)
![Passando os parâmetros para o cron](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%201/Evidencias/Passo%207%20-%20Defidindo%20execu%C3%A7%C3%A3o%20do%20script%20'processamento_de_vendas.sh'%20com%20um%20dia%20de%20antecedencia%20para%20caso%20algo%20de%20errado.png)

* crontab -l - verifica se temos algum agendamento.

![Verificando agendamento](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%201/Evidencias/Passo%208%20-%20Verificando%20se%20meu%20agendamento%20com%20o%20crontab%20-L.png)

## 7. Rodando o programa com um dia de antecedência.
#### Como estava um pouco adiantado quando cheguei a está etapa, que no caso foi domingo de manhã, já aproveitei para executa-lo um dia antes para caso ocorresse algum erro, eu já pudesse corrigir.

![Resultado do programa executado no domingo](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%201/Evidencias/Passo%209%20-%20Rodando%20o%20programa%20agendado%20com%20um%20dia%20de%20antecedencia%20para%20ver%20se%20esta%20funcionando.png)

## 8. Programa rodando segunda-feira - 20240826.
#### Como podem ver, cometi um erro, que nesse caso foi não adicionar a data ao backup.zip, o que faria com que ele não criasse novos backup.zip a cada dia.
* Comando tree - mostra como se fosse realmente um árvore, os diretórios e arquivos, em um tipo de cascata.
  
![Primeiro dia execução](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%201/Evidencias/Passo%2010%20-%20Rodando%20o%20programa%20dia%2020240826%20-%20segunda%20feira%20-%20tudo%20funcionando.png)

## 9. Programa rodando terça-feira - 20240827.
#### Aqui o erro da falta de data no backup.zip foi corrigido.

![Segundo dia de execução](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%201/Evidencias/Passo%2011%20-%20Programa%20executado%20dia%2020240827%20-%20segundo%20dia%20-%20tudo%20funcionando.png)

## 10. Programa rodando quarta-feira - 20240828.
#### Tudo funcionando perfeitamente

![Terceiro dia de execução](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%201/Evidencias/Passo%2012%20-%20Programa%20executado%20dia%2020240828%20-%20terceiro%20dia%20-%20tudo%20funcionando.png)

## 11. Programa não rodou quinta-feira
#### Como não foi executado quinta-feira, agendei novamente pra sexta-feira:

![Novo agendamento](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%201/Evidencias/Passo%2013%20-%20N%C3%A3o%20rodou%20o%20programa%20na%20quinta%20-%2020240829%20-%20remarquei%20para%20sexta.png)
