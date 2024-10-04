def calcular_valor_maximo(operadores_aritmeticos, pares_operandos):
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else float('inf'),
        '%': lambda x, y: x % y if y != 0 else float('inf')
    }
    operacoes_resultados = map(lambda op_par: operacoes[op_par[0]](op_par[1][0], op_par[1][1]), zip(operadores_aritmeticos, 
        pares_operandos))
    
    return max(operacoes_resultados)

operadores_aritmeticos = ['+','-','*','/','+']
pares_operandos  = [(15, 9), (-7, -7), (7, 11), (10, 12), (18, 14)]

print(calcular_valor_maximo(operadores_aritmeticos, pares_operandos))