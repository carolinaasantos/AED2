# Criação da função Radixsort
def radixsort(lista, n):
    m = max(lista)
    d = 1 # Define a divisão por 1 unidade
    while m / d > 0:
        countingsort_radix(lista, n, d)
        d *= 10 # Ordena pela dezena, centena, assim por diante

# Criação da função Countingsort adaptada à divisão do Radixsort
def countingsort_radix(lista, n, d):

    # Criação de um array com n zeros
    aux1 = []
    for i in range (0, n):
        aux1.append(0)
    
    # Encontra o maior dígito em (lista[i] // d) % 10
    m = 0
    for i in range(n):
        m = max(m, (lista[i] // d) % 10)

    # Criação de um array com 10 zeros, já que os dígitos variam de 0 a 9
    aux2 = []
    for i in range (0, 10):
        aux2.append(0)
    
    # Histograma
    for i in range (0, n):
        index = (lista[i] // d) % 10
        aux2[index] += 1
    
    # Soma acumulada
    for i in range (1, 10):
        aux2[i] += aux2[i-1]
    
    # Constrói um array ordenado temporariamente a partir da soma acumulada
    for i in range (n - 1, -1, -1):
        index = (lista[i] // d) % 10
        aux2[index] -= 1
        aux1[aux2[index]] = lista[i]
    
    # Atualiza a lista, copiando o vetor ordenado na lista original
    for i in range (0, n):
        lista[i] = aux1[i]

# Main
numeros = [29, 125, 391, 74, 213, 178, 43, 19, 424, 131, 120, 158, 105, 92, 169, 81, 1, 143, 210, 51]

print("Vamos observar o funcionamento do Radix Sort!")

print(f'Antes da ordenação pelo Radix Sort: {numeros}')
radixsort(numeros, len(numeros))

print(f'Depois da ordenação pelo Radix Sort: {numeros}')