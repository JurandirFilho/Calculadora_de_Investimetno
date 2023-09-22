# criando função para calcular
def calcular_lucro(investimento_inicial, dias_de_investimento, retorno_garantido):
    
    retorno_diario = retorno_garantido / 100 / dias_de_investimento
    
    lucro_diario = investimento_inicial * retorno_diario
    lucro_semanal = lucro_diario * 7
    lucro_mensal = lucro_diario * 30
    lucro_total = investimento_inicial *(1 + retorno_garantido / 100)
    
    print(f'Lucro diário: {lucro_diario:.2f}')
    print(f'Lucro semanal: {lucro_semanal:.2f}')
    print(f'Lucro mensal: {lucro_mensal:.2f}')
    print(f'Lucro diário: {lucro_total:.2f}')
    
calcular_lucro(5000,30,5)