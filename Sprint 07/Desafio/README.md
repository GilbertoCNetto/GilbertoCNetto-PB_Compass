## Etapas do Desafio:
### Comecei o desafio criando o dockerfile.
![passo_01](../../Sprint%2007/Evidencias/desafio/passo_01_dockerfile.png)
##

### Na Segunda etapa eu fiz um docker build, para criar minha imagem.
![passo_02](../../Sprint%2007/Evidencias/desafio/passo_02_docker_build.png)
##

### Na terceira etapa eu fiz o docker run, criando o container da imagem "layer" que criei anteriormente, para criar o layer no lambda, com boto3 e requests. 
![passo_03](../../Sprint%2007/Evidencias/desafio/passo_03_docker_run_parte_1.png)
![passo_04](../../Sprint%2007/Evidencias/desafio/passo_04_docker_run_parte_2.png)
### Copiando o "Layer.zip" para tirar do container e subir pro container, nessa terceira etapa eu segui o mesmo passo a passo do exercício de lambda da sprint passada, com algumas pequenas alterações.
![passo_05](../../Sprint%2007/Evidencias/desafio/passo_05_copiando_o_layer_zip.png)
##

### Na quarta etapa comecei a escrever o script.py, criei primeiro um local, para testar e ver o resultado que iria obter, depois o adaptei para o AWS Lambda, com vou mostrar na sequência.

### Comecei esta etapa importando as bibliotecas que iria usar.
![passo_06](../../Sprint%2007/Evidencias/desafio/passo_06_criando_o_script_e_import_das_bibliotecas.png)
##

### Após a importação das bibliotecas, criei uma função definindo alguns parâmetros pra API puxar, como por exemplo o período desejado e o gênero.
![passo_07](../../Sprint%2007/Evidencias/desafio/passo_07_funcao_para_buscar_as_series.png)
##
### Em sequência, fiz uma outra função para buscar os detalhes das séries, o que eu tive que complementar na próxima função, pois ainda não estava buscando todos os dados que eu desejava, como temporadas e o status da série.
![passo_08](../../Sprint%2007/Evidencias/desafio/passo_08_funcao_para_buscar_os_detalhes_da_serie.png)
##

### Agora chegamos a etapa principal do desafio, comecei essa função puxando as variáveis de ambiente, que defini nas próprias configurações do AWS Lambda, defini também o ano de inicio e de fim que escolhi para período da minha análise, também escolhi um limite para o máximo de séries que desejava puxar. Além disso criei uma variável para o total de séries para a função não estabelecer o limite que defini.

### Após as configurações iniciais, usei o datetime para puxar a data atual, para criar o caminho corretamente no bucket do meu datalake e criei a variável 's3_bucket' para passar o nome do meu bucket.

### Então dei continuação ao código, para puxar as séries, utilizei um while, para o total de séries ser menor que o limite de séries que defini. Também fiz alguns IFs, o primeiro para que o total de séries seja exatamente 300, e dentro desse IF, fiz um FOR com um IF dentro, para puxar o status e as temporadas das séries. E fiz também um ELSE caso houvesse algum erro durante a busca. E uma contagem nas páginas no final, para não repetir as páginas buscadas.
![passo_09](../../Sprint%2007/Evidencias/desafio/passo_09_funcao_principal_do_lambda.png)
##

### Chegando na parte final do meu script, foi a etapa de salvar as buscas feitas pela API em um arquivo JSON e envia-los para o meu bucket no S3, configurando o path como foi pedido no pdf do desafio, e como nos foi aconselhado, delimitei em 100 registros por arquivo, como puxei 300 séries, me foram criados 3 arquivos json como resultado
![passo_10](../../Sprint%2007/Evidencias/desafio/passo_10_salvando_as_series_em_json_e_envio_ao_S3.png)
![passo_11](../../Sprint%2007/Evidencias/desafio/passo_11_confirmacao_que_o_codigo_foi_executado.png)
##

### Exemplo do resultado dos arquivos JSON:
![exemplo_arquivo_json](../../Sprint%2007/Evidencias/desafio/arquivo_json.png)
##

### Desafio concluído com sucesso, caminho criado conforme o que foi pedido, e os arquivos upados corretamente
![passo_12](../../Sprint%2007/Evidencias/desafio/passo_12_arquivos_upados_e_caminho_no_S3.png)
##


## Mudanças na Análise escolhida:
### Fiz algumas mudanças na minha análise para focar em um período específico e um valor mínimo de votos de usuário, no caso, vou analisar as séries entre os anos 2000 e 2020 e que tenham ao menos 300 votos.
#### Com base nisso pretendo responder as seguintes perguntas:
 * Quais as séries de cada década eu indicaria para alguém com base nas notas?
 * Qual a série com maior número de episódios?
 * Qual a série com maior número de temporadas?
 * Quais as séries de maiores notas, com pelo menos 3 temporadas?