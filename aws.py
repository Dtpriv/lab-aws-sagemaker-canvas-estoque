# Dados de entrada e saída
horas_estudo = [1, 2, 3, 4, 5]
nota_prova = [70, 55, 60, 65, 70]

# Função para calcular a inclinação (slope) e a interseção (intercept) da regressão linear
def calcular_regressao_linear(x, y):
    n = len(x)
    
    x_media = sum(x) / n
    y_media = sum(y) / n
    
    numerador = sum((xi - x_media) * (yi - y_media) for xi, yi in zip(x, y))
    denominador = sum((xi - x_media) ** 2 for xi in x)
    
    inclinação = numerador / denominador
    interseção = y_media - (inclinação * x_media)
    
    return inclinação, interseção

# Calcula a inclinação e a interseção
inclinação, interseção = calcular_regressao_linear(horas_estudo, nota_prova)

# Função para prever novas notas
def prever_nota(horas_estudo_teste, inclinação, interseção):
    return [inclinação * x + interseção for x in horas_estudo_teste]

# Testa o modelo com novos dados
horas_estudo_teste = [6, 7, 8]
notas_previstas = prever_nota(horas_estudo_teste, inclinação, interseção)

# Exibe os resultados
print(f'Inclinação (Slope): {inclinação:.2f}')
print(f'Interseção (Intercept): {interseção:.2f}')
print(f'Notas Previstas para Horas de Estudo [6, 7, 8]: {notas_previstas}')
