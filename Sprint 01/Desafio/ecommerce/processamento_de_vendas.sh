mkdir vendas
cp ecommerce/dados_de_vendas.csv vendas
cd vendas/
mkdir backup/
DATA=$(date +'%Y%m%d')
cp dados_de_vendas.csv backup/dados_de_vendas-$DATA.csv
mv backup/dados_de_vendas-$DATA.csv backup-dados-$DATA.csv
mv backup-dados-$DATA.csv backup/
cd backup/
DATA_SISTEMA_OPERACIONAL=$(date +'%Y%m%d %HH:%MM')
DATA_PRIMEIRO_REGISTRO=$(head -n 2 backup-dados-$DATA.csv | cut -d ',' -f 5)
DATA_ULTIMO_REGISTRO=$(tail -n 1 backup-dados-$DATA.csv | cut -d ',' -f 5)
ITENS_DIFERENTES=$(tail -n +2 backup-dados-$DATA.csv | cut -d ',' -f 2 | uniq | wc -l)
RELATORIO="relatorio-$DATA.txt"
echo 'Data do Sistema Operacional:'$DATA_SISTEMA_OPERACIONAL >> "$RELATORIO"
echo 'Primeiro registro '$DATA_PRIMEIRO_REGISTRO >> "$RELATORIO"
echo 'Ultimo registro data '$DATA_ULTIMO_REGISTRO >> "$RELATORIO"
echo 'Itens diferentes vendidos: '$ITENS_DIFERENTES >> "$RELATORIO"
head -n 10 backup-dados-$DATA.csv >> "$RELATORIO"
cat "$RELATORIO"

zip backup-dados-$DATA.zip backup-dados-$DATA.csv
rm backup-dados-$DATA.csv

cd ..
rm dados_de_vendas.csv








