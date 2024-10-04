def conta_vogais(texto):
    vogais = 'aeiou'
    quantia_vogais = filter(lambda x: x in vogais, texto.lower())
    return len(list(quantia_vogais))

texto = "Quantia de vogais"
print(conta_vogais(texto))
