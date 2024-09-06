-- Apresente a query para listar o código e nome cliente com maior gasto na loja. As 
-- colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando 
-- o somatório das vendas (concluídas) atribuídas ao cliente.
select 
    cdcli, 
    nmcli,
    sum(qtd * vrunt) as gasto
from tbvendas tbv
left join tbestoqueproduto tbep on tbv.status = tbep.status
where tbv.status ='Concluído' 
group by nmcli
order by gasto desc
limit 1
