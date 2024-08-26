# Escolhe um pivô e particiona a lista de modo que os valores menores
# que o pivô fiquem à esquerda e maiores que o pivô à direita
# Repete esses passos nas sublistas menores até que fique ordenado

def swap(L, a, b):
    aux = L.index(b)
    L[L.index(a)] = b
    L[aux] = a
    return L

def partition(L, low, high):
    x = L[high] # Pivô
    i = low - 1 # Maior índice do lado esquerdo
    for j in range (low, high-1): # Processa todo elemento menor que o pivô
        if L[j] <= x: # É menor do que o pivô (lado esquerdo)?
            i = i + 1 # Novo índice para o lado esquerdo
            swap(L, L[i], L[j]) # Adiciona ele no lado esquerdo
    swap(L, L[high], L[i + 1]) # Pivô vai no fim do lado esquerdo
    return (i + 1) # Índice do pivô

def quicksort(L, low, high):
	if low < high:
		q = partition (L, low, high)
		quicksort(L, low, q-1)
		quicksort(L, q + 1, high)

