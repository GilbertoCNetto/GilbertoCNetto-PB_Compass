-- Apresente a query para listar a quantidade de livros publicada por cada autor.
-- Ordenar as linhas pela coluna nome(autor), em ordem crescente. Além desta, apresentar
-- as colunas codautor, nascimento e quantidade(total de livros de sua autoria).
select a.nome, a.codautor, a.nascimento, count(l.cod) as quantidade
from autor a
left join livro l on a.codautor = l.autor
group by a.codautor, a.nome, a.nascimento
order by a.nome asc