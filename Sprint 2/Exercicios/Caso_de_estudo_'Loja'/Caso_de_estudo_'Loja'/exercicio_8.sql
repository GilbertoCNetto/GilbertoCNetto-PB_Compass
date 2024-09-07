-- Apresente a query para listar o código e o nome do vendedor com maior número de 
-- vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas 
-- presentes no resultado devem ser, portanto, cdvdd e nmvdd.
with contagem as (
select 
    count(tbv.status)
from tbvendas
)
select tbv.cdvdd, nmvdd
from tbvendas tbv
left join tbvendedor tbvdd on tbv.cdvdd = tbvdd.cdvdd
left join tbestoqueproduto tbep on tbv.status = tbep.status
limit 1