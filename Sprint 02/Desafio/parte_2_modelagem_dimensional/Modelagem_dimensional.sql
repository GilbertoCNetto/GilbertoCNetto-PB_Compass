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

