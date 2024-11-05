# Etapas do Desafio:

## 1. Comecei o desafiando criando um txt, com o seguinte conteúdo dentro dele, que na sequência seria executado no dockerfile, quando eu fizesse o docker build.
![passo_0](../../Sprint%2006/Evidencias/desafio/conteudo_do_txt.png)
##

## 2. Após isso, fiz a criação do dockerfile, utilizando o mesmo codigo da sprint passada, com algumas pequenas alterações apenas, como por exemplo, tive que criar algumas linhas de código para fazer o volume, no caso "VOLUME ["/app/volume"]", e também tive que escrever uma linha de código para executar o arquivo txt que foi o seguinte, "RUN pip install --no-cache-dir -r biblioteca.txt ", que executou o pip install no boto3 dentro do docker. 
![passo_1](../../Sprint%2006/Evidencias/desafio/passo_1_dockerfile.png)
##

## 3. Usando o comando docker build, para criar a minha imagem "conexao_s3".
![passo_2](../../Sprint%2006/Evidencias/desafio/passo_2_build_imagem.png)
##

## 4. Após criar a imagem, parti para criação do script python, que nomeei de "desafio.py", peguei o código da sprint passada também, para usar como base, mas tive que criar diversas variáveis e importar a biblioteca datetime, para pegar a data atual.
## Além disso, também criei as variáveis para passar os caminhos que eu gostaria que fossem criados no S3, sendo elas "path_series" e "path_movies".
## Também tive que mudar o caminho de onde eu estava pegando os arquivos, pois como estavam rodando em docker, o caminho não poderia ser o mesmo do windows, então o caminho que passei foi "/app/VOLUME/arquivo_desejado".
## E por fim utilizei o comando "uploadfile_file" do S3, para subir ambos os arquivos, em seus respectivos caminhos.
![passo_3](../../Sprint%2006/Evidencias/desafio/passo_3_script_python.png)
##

## 5. Em seguida, utilizei o comando docker Run, para executar a imagem, porém foi necessário passar as credenciais da AWS(editei a imagem, para esconder as Keys e Tokens), mas o comando escrito foi o seguinte:
![passo_4](../../Sprint%2006/Evidencias/desafio/passo_4_executando_o_container.png)
##

## 6. Caminho para o arquivo "movies.csv" exatamente como foi pedido na Udemy.
![passo_5](../../Sprint%2006/Evidencias/desafio/passo_5_caminho_completo_para_o_csv_movies.png)
##

## 7. Caminho para o arquivo "series.csv" exatamente como foi pedido na Udemy.
![passo_6](../../Sprint%2006/Evidencias/desafio/passo_6_caminho_completo_para_o_csv_series.png)
##

## Como podemos ver, o desafio foi concluído com sucesso