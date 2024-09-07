-- Apresente a query para listar o código e nome do produto mais vendido entre 
-- as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status 
-- concluída. As colunas presentes no resultado devem ser cdpro e nmpro.
with contagem as (
select
    count(nmpro)
from tbvendas
)
select tbv.cdpro, nmpro
from tbvendas tbv
left join tbestoqueproduto tbep on tbv.status = tbep.status
where dtven between '2014-02-03' and '2018-02-02'
limit 1