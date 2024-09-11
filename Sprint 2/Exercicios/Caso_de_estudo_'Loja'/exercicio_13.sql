-- Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce 
-- ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem 
-- ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.
select 
    tbv.cdpro, 
    nmcanalvendas, 
    nmpro , 
    sum(qtd) as quantidade_vendas
from tbvendas tbv
left join tbestoqueproduto tbep on tbv.status = tbep.status
where tbv.status = 'Concluído'
group by tbv.cdpro, nmcanalvendas
order by quantidade_vendas asc
limit 10