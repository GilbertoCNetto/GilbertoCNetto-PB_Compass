-- Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado
--  deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas
--  pela coluna que representa a quantidade de livros em ordem decrescente.
select count(*) as quantidade, nome, estado, cidade
from livro l
join editora e on e.codEditora = l.editora 
join endereco en on en.codEndereco = e.endereco
group by editora 
order by quantidade desc