# **Etapas do Desafio**
## Etapa 1 - Construir uma imagem a partir de um arquivo de instruções dockerfile que execute o codigo carguru.py, e executar um container da imagem criada.
### Passo 1: Comecei o desafio, fazendo o download do arquivo carguru.py, e o inserindo na pasta do desafio:
##
![passo_1](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2004/Evidencias/Etapa_1_codigo_carguru.py_importado_pro_vscode.png)
##
### Passso 2: Após isso, escrevi o codigo no dockerfile que serviria para criação da image:
##
![passo_2](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2004/Evidencias/Etapa_1_codigo_do_dockerfile_carguru.png)
##
### Passo 3: Criando a imagem carguru:
##
![passo_3](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2004/Evidencias/Etapa_1_criando_a_imagem_do_carguru.png)
##
### Passo 4: Executando o container a partir da imagem carguru:
#### Etapa 1 executaca com sucesso.
##
![passo_4](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2004/Evidencias/Etapa_1_executando_o_container_a_partir_da_imagem_carguru.png)

---

## Etapa 2 - É possivel reutilizar containers?
### Sim, é possivel reutilizar containers, através do comando:
* docker start (nome ou id do container)

---

## Etapa 3 - Criação de um container que permita receber inputs durante sua execução.
### Passo 1: Criando o dockerfile da imagem mascarar-dados.
![passo_1e2](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2004/Evidencias/Etapa_3_codigo_do_dockerfile_mascarar-dados.png)
##
### Passo 2: Criando o arquivo hash.py que recebe o input e transforma a frase recebida em hash por meio do algoritmo SHA-1
![passo_2e2](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2004/Evidencias/Etapa_3_criando_o_script_hash.py.png)
##
### Passo 3: Criando a imagem mascarar-dados
![passo_3e2](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2004/Evidencias/Etapa_3_criando_a_imagem_mascarar-dados.png)
##
### Passo 4: Executando o container a partir da imagem mascarar-dados
![passo_4e2](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2004/Evidencias/Etapa_3_executando_o_container_a_partir_da_imagem_mascarar-dados.png)

---

### Link para a etapa 1 - carguru
- [Etapa-1-Carguru](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/tree/main/Sprint%2004/Desafio/carguru)

### Link para a etapa 3 - mascarar-dados
- [Etapa-3-Mascarar-dados](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/tree/main/Sprint%2004/Desafio/mascarar_dados)
