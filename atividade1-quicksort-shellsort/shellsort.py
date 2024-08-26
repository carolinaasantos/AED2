# Também vai inserindo os valores no "novo array" na posição correta,
# porém com passos maiores do que 1 (utiliza gap)
# Com isso se torna mais eficiente ao diminuir o gap desde n//2 até 1

def swap(L, a, b):
    aux = L.index(b)
    L[L.index(a)] = b
    L[aux] = a
    return L

def shellsort(L, n):
    h = n//2
    iteracao = 0
    while h > 0:
        for i in range (h, n):
            j = i
            while j >= h and L[j-h] > L[j]:
                L = swap(L, L[j], L[j-h])
                j = j - h
                print(L)
        h = h//2
        iteracao += 1
    return iteracao

lista = [5, 3, 1, 4, 6, 2, 10, 11, 8, 7]
iteracao = shellsort(lista, len(lista))
print(f'Teve {iteracao} iteracoes')
print(lista)