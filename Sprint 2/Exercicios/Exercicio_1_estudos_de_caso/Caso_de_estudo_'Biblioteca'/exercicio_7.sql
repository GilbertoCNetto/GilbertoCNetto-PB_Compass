-- Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los
-- em ordem crescente.
with nenhuma_publicacao as (
select
    nome,
    count(l.cod) as quantidade
from autor a
left join livro l on a.codautor = l.autor
group by a.nome
having quantidade = 0
)

select nome
from nenhuma_publicacao
