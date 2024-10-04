from functools import reduce


def calcula_saldo(lancamentos):
    valores_da_conta = map(lambda x: -x[0] if x[1] == 'D' else x[0], lancamentos)
    saldo_final = reduce(lambda acc, val: acc + val, valores_da_conta)
    
    return saldo_final


lancamentos = [
    (1500, 'D'),
    (3000, 'C'),
    (800, 'C')
]

print(calcula_saldo(lancamentos))