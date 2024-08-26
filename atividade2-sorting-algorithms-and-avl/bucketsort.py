import math

# Criação de um vetor preenchido com outros vetores (bucket)
def buckets(n):  # Criação dos n buckets vazios
    bucket = []
    for c in range(0, n):
        bucket.append([])
    return bucket

# Criação da função Bucketsort
def bucketsort(lista, n):
    # Inicializa n buckets vazios
    b = buckets(n)

    final = []  # Onde será armazenado o resultado final

    # Encontrando o maior valor na lista para calcular o índice do bucket
    max_value = max(lista)

    # Distribuindo os elementos da lista nos buckets apropriados
    for i in range(n):
        index = math.floor(n * lista[i] / (max_value + 1))
        b[index].append(lista[i])  # Adiciona o valor no bucket correspondente

    # Ordenando cada bucket individualmente e o concatenando-os no vetor final
    for bucket in b:
        bucket.sort()
        final += bucket

    return final

# Main
numeros = [29, 12, 3, 7, 2, 17, 4, 19, 42, 31, 20, 15, 10, 9, 16, 8, 1, 13, 21, 5]

print("Vamos observar o funcionamento do Bucket Sort!")

print(f'Antes da ordenação pelo Bucket Sort:{numeros}')
numeros_ordenados = bucketsort(numeros ,len(numeros))
                               
print(f'Depois da ordenação pelo Bucket Sort: {numeros_ordenados}')