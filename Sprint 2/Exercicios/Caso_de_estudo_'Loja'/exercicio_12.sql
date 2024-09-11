-- Apresente a query para listar código, nome e data de nascimento dos dependentes do 
-- vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes 
-- no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
-- Observação: Apenas vendas com status concluído.
select 
    cddep, 
    nmdep, 
    dtnasc, 
    sum(tbv.qtd * tbv.vrunt) as valor_total_vendas
from tbdependente tbd
join tbvendedor tbve on tbve.cdvdd = tbd.cdvdd
join tbvendas tbv on tbv.cdvdd = tbve.cdvdd
where tbv.status = 'Concluído'
group by tbve.nmvdd
having valor_total_vendas > 0
order by valor_total_vendas asc
limit 1