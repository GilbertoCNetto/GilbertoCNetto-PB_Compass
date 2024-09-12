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
    km_carro INT,
    classi_carro VARCHAR(50),
    modelo_carro VARCHAR(80),
    ano_carro INT,
    id_combustivel INT,
    id_marca INTEGER,
    FOREIGN KEY (id_combustivel) REFERENCES tb_combustivel(id_combustivel),
    FOREIGN KEY (id_marca) REFERENCES tb_marca(id_marca)
);

INSERT OR REPLACE INTO tb_carros(id_carro, km_carro, classi_carro, modelo_carro, ano_carro, id_combustivel, id_marca)
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

INSERT OR REPLACE INTO tb_locacao (id_locacao, id_cliente, id_carro, id_combustivel, id_vendedor, data_locacao,hora_locacao, data_entrega, hora_entrega, qtd_diaria, valor_diaria)
SELECT idLocacao, idCliente, idCarro, idcombustivel, idVendedor, dataLocacao,horaLocacao, dataEntrega, horaEntrega, qtdDiaria, vlrDiaria FROM tb_locacao_bruto;

DROP TABLE tb_locacao_bruto 

