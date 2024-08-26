# Criação da função Countingsort
def countingsort(lista, n):
    m = max(lista) # m - maior elemento
    aux1 = []
    aux2 = []

    # Criação de um array com m+1 zeros # C
    for i in range (0, m+1):
        aux1.append(0)
    
    # Criação de um array com n zeros # S
    for i in range (0, n-1):
        aux2.append(0)
    
    # Histograma
    for i in range (0, n):
        aux1[lista[i]] += 1
    
    # Soma acumulada
    for i in range (1, m):
        aux1[i] += aux1[i-1]
    
    # Encontra o índice de cada elemento da lista em aux1 e coloca o elemento determinado em aux2
    for i in range (0, n):
        aux1[lista[i]] -= 1
        aux2[aux1[lista[i]]] = lista[i]
    
    return aux2

# Main
numeros = [29, 12, 3, 7, 2, 17, 4, 19, 42, 31, 20, 15, 10, 9, 16, 8, 1, 13, 21, 5]

print("Vamos observar o funcionamento do Couting Sort!")

print(f'Antes da ordenação pelo Counting Sort: {numeros}')
numeros_ordenados = countingsort(numeros, len(numeros))

print(f'Depois da ordenação pelo Counting Sort: {numeros_ordenados}')

