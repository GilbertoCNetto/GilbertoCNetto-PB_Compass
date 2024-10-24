# **Etapas do Desafio**

## 1. Comecei o desafio alterando o nome da tb_locacao para tb_locacao_bruto.

### Codigo:

``` SQL
ALTER TABLE tb_locacao RENAME TO tb_locacao_bruto;
```
##

## 2. Após isso, parti para as 3 formas normais, criando todas as tabelas que considerei necessárias e inseri os dados das respectivas colunas.

### Codigo:

```SQL
CREATE TABLE tb_clientes (
    id_cliente INTEGER PRIMARY KEY,
    nome_cliente VARCHAR(100),
    id_localizacao INT,
    FOREIGN KEY (id_localizacao) REFERENCES tb_localizacao(id_localizacao)
);

INSERT OR REPLACE INTO tb_clientes (id_cliente , nome_cliente, id_localizacao)
SELECt DISTINCT idCliente , nomeCliente, id_localizacao
FROM tb_locacao_bruto tbc
LEFT JOIN tb_localizacao tbl ON tbc.cidadeCliente = tbl.cidade_cliente

CREATE TABLE tb_combustivel (
	id_combustivel INTEGER PRIMARY KEY,
	tipo_combustivel VARCHAR(20)
);

INSERT OR REPLACE INTO tb_combustivel(id_combustivel, tipo_combustivel)
SELECT idcombustivel, tipoCombustivel FROM tb_locacao_bruto;

CREATE TABLE tb_carros (
    id_carro INTEGER PRIMARY KEY,
    km_carro_atual INT,
    classi_carro VARCHAR(50),
    modelo_carro VARCHAR(80),
    ano_carro INT,
    id_combustivel INT,
    id_marca INTEGER,
    FOREIGN KEY (id_combustivel) REFERENCES tb_combustivel(id_combustivel),
    FOREIGN KEY (id_marca) REFERENCES tb_marca(id_marca)
);

INSERT OR REPLACE INTO tb_carros(id_carro, km_carro_atual, classi_carro, modelo_carro, ano_carro, id_combustivel, id_marca)
SELECT idCarro, kmCarro, classiCarro, modeloCarro, anoCarro, idcombustivel, id_marca 
FROM tb_locacao_bruto tbc
LEFT JOIN tb_marca tbm ON tbm.marca_carro = tbc.marcaCarro


CREATE TABLE tb_marca (
	id_marca INTEGER PRIMARY KEY,
	marca_carro VARCHAR(80)
)

INSERT OR REPLACE INTO tb_marca(marca_carro)
SELECT DISTINCT marcaCarro FROM tb_locacao_bruto;

CREATE TABLE tb_vendedor (
	id_vendedor INTEGER PRIMARY KEY,
	nome_vendedor VARCHAR(15),
	sexo_vendedor SMALLINT,
	estado_vendedor VARCHAR(40)
);

INSERT OR REPLACE INTO tb_vendedor(id_vendedor, nome_vendedor, sexo_vendedor, estado_vendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor FROM tb_locacao_bruto;



CREATE TABLE tb_localizacao (
	id_localizacao INTEGER PRIMARY KEY AUTOINCREMENT,
	cidade_cliente VARCHAR(40),
    estado_cliente VARCHAR(40),
    pais_cliente VARCHAR(40)
)

INSERT OR REPLACE INTO tb_localizacao(cidade_cliente, estado_cliente, pais_cliente)
SELECT DISTINCT cidadeCliente, estadoCliente, paisCliente FROM tb_locacao_bruto;

CREATE TABLE tb_locacao (
	id_locacao INT PRIMARY KEY,
	id_cliente INT,
	id_carro INT,
	id_combustivel INT,
	id_vendedor INT,
	data_locacao DATETIME,
	hora_locacao TIME,
	data_entrega DATE,
	hora_entrega TIME,
	qtd_diaria INT,
	valor_diaria decimal(18,2),
	FOREIGN KEY (id_cliente) REFERENCES tb_clientes(id_cliente),
	FOREIGN KEY (id_carro) REFERENCES tb_carros(id_carro),
	FOREIGN KEY (id_vendedor) REFERENCES tb_vendedor(id_vendedor)
);

INSERT OR REPLACE INTO tb_locacao (id_locacao, id_cliente, id_carro, id_combustivel, id_vendedor, data_locacao, hora_locacao, data_entrega, hora_entrega, qtd_diaria, valor_diaria)
SELECT idLocacao, idCliente, idCarro, idcombustivel, idVendedor, dataLocacao,horaLocacao, dataEntrega, horaEntrega, qtdDiaria, vlrDiaria FROM tb_locacao_bruto;
```

### Comandos de destaque:
  * CREATE TABLE - cria novas tabelas;
  * PRIMARY KEY - transforma uma coluna em chave primária, que é um campo ou conjunto de campos com valores exclusivos por toda a tabela;
  * FOREIGN KEY - transforma a coluna em chave extrangeira, que é a chave que permite a referência a registros orinados de outras tabelas;
  * INSERT OR REPLACE - que utilizei para inserir os dados da tb_locacao_bruto, nas outras tabelas criadas;
  * SELECT - seleciona as coluna que desejo;
  * FROM - seleciona a tabela de onde quero a coluna;
  * AUTOINCREMENT - foi muito útil para criar colunas de id, que atualizava seu valor baseado na quantidade de linhas da coluna
##

## 3. Após a normalização, decidi remover a tb_locacao_bruto.

### CODIGO:

```SQL
DROP TABLE tb_locacao_bruto 
```
##

## 4. E criei o diagrama do modelo relacional.

![Modelagem Relacional](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2002/Evidencias/Passo%203%20-Diagrama_modelagem_relacional.png)
##

## 5. Após a normalização e a criação do diagrama do modelo relacional, criei as views para o modelo dimensional(conforme recomendado no desafio).

### Codigo:

```SQL
CREATE VIEW fato_locacao AS 
SELECT id_locacao AS id_locacao,
	   id_cliente AS id_cliente,
	   id_carro AS id_carro,
	   id_vendedor AS id_vendedor,
	   data_locacao AS data_locacao,
	   hora_locacao AS hora_locacao,
	   data_entrega AS data_entrega,
	   hora_entrega AS hora_entrega,
	   qtd_diaria AS qtd_diaria,
	   valor_diaria AS valor_diaria
FROM tb_locacao;

CREATE VIEW dim_clientes AS
SELECT id_cliente AS id_cliente,
	   nome_cliente AS nome_cliente,
	   cidade_cliente AS cidade_cliente,
	   estado_cliente AS estado_cliente, 
	   pais_cliente AS pais_cliente
FROM tb_clientes tc 
LEFT JOIN tb_localizacao tl ON tl.id_localizacao = tc.id_localizacao;

CREATE VIEW dim_carros AS 
SELECT id_carro AS id_carro,
	   km_carro_atual AS km_carro,
	   classi_carro AS classi_carro,
	   marca_carro AS marca_carro,
	   modelo_carro AS modelo_carro,
	   ano_carro AS ano_carro
FROM tb_carros tca 
LEFT JOIN tb_marca tm ON tm.id_marca = tca.id_marca;

CREATE VIEW dim_vendedor AS 
SELECT id_vendedor AS id_vendedor,
	   nome_vendedor AS nome_vendedor,
	   sexo_vendedor AS sexo_vendedor,
	   estado_vendedor AS estado_vendedor
FROM tb_vendedor;

CREATE VIEW dim_data AS
SELECT DISTINCT
    data_locacao AS data_locacao,
    substr(data_locacao, 1, 4) AS ano INT,     
    substr(data_locacao, 5, 2) AS mes INT,      
    substr(data_locacao, 7, 2) AS dia INT      
FROM tb_locacao
WHERE data_locacao IS NOT NULL;
```
##

## 6. Nessa etapa criei o diagrama da modelagem dimensional.

![Modelagem Dimensional](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2002/Evidencias/Passo%205%20-Diagrama_modelo_dimensional_star_schema.png)
##

## 7. Após todos esses passos, decidi testar o modelo dimensional, e puxar algumas métricas sobre o database, desensolvi a seguinte query para isso:

![Métricas](https://github.com/GilbertoCNetto/GilbertoCNetto-PB_Compass/blob/main/Sprint%2002/Evidencias/Passo%206%20-%20puxando_algumas_metricas.png)

### Análisando os resultados, é possivel observar que o estado que gerou o maior valor total em locação, foi o estado do Amazonas com o valor de R$17.600,00, e o estado com o menor valor total em locação foi o estado de São Paulo, com o valor de apenas R$400,00

### Já os estados com o maior número de locações foram o Rio de Janeiro e o Mato Grosso do Sul, ambos com 5 locações ao todo
### Importante observar que o Rio de Janeiro conseguiu isso graças a soma das locações de dois clientes, que geraram somados R$7.100,00. Já o Mato Grosso do Sul foi tudo de um só cliente, que em valor total de locação gerou R$12.600,00
