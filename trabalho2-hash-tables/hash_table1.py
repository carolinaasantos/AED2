# Hash table com tratamento de colisões por encadeamento lógico

import random

# Nó que representa um par chave-valor e também um ponteiro para o próximo elemento na lista encadeada
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Definição da classe Hash Table
class Hash_table:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Definição do método da função hash
    def hash_function(self, key):
        # Convertendo chave para inteiro se for string
        if not isinstance(key, int):
            key = self.convert_to_int(key)
        # Mapear uma chave k para um slot m por meio do método da divisão
        h = key % self.size
        # Retorna valor hash
        return h

    # Definição do método auxiliar da função hash que transforma str em int por meio dos valores ASCII
    def convert_to_int(self, key):
        int = sum(ord(char) for char in str(key))
        return int

    # Definição do método para inserção de chaves na tabela
    def inserir_chave(self, key, value):
        # Encontra o index do valor na tabela hash
        index = self.hash_function(key)
        new_node = Node(key, value)

        # Se não tiver nenhum elemento naquele index, o novo elemento é adicionado
        if self.table[index] is None:
            self.table[index] = new_node
        # Caso já tenha um elemento, deve ser adicionado ao final da lista encadeada do index
        else:
            current = self.table[index]
            while current.next is not None:
                if current.key == key:
                    current.value = value # Atualiza o valor se a chave já existir
                    return
                current = current.next
            if current.key == key:
                current.value = value # Atualiza o valor se a chave já existir no último nó
            else:
                current.next = new_node # Adiciona o novo nó ao final da lista

    # Definição do método para buscar uma chave dentro da tabela hash
    def buscar_chave(self, key):
        # Encontra o index do valor na tabela hash
        index = self.hash_function(key)
        current = self.table[index]
        acessos = 0

        # Percorre a tabela hash
        while current is not None:
            acessos += 1
            if current.key == key:
                # Retorna o valor encontrado
                print(f"Foi necessario {acessos} acesso(s) para encontrar a chave '{key}'")
                return current.value
            current = current.next

        # Caso contrário, o valor não foi encontrado
        print(f"Foi necessario {acessos} acesso(s) para NÃO encontrar a chave '{key}'")
        return None

    # Definição do método para remoção de uma chave dentro da tabela hash
    def remover_chave(self, key):
        # Encontra o index do valor na tabela hash
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        # Procura o elemento a ser removido
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                print(f"A chave {key} foi removida com sucesso.")
                return
            prev = current
            current = current.next

        # Caso a chave não exista
        print("A chave não pôde ser removida porque não foi encontrada")
        return

    # Definição do método para printar todos os elementos da tabela hash
    def imprimir_chaves(self):
        for i in range (0, self.size):
            current = self.table[i]
            print(f"Slot {i}: ", end="")
            # Printa todos os elementos até que o current seja nulo
            while current is not None:
                print(f"({current.key}: {current.value}) -> ", end="")
                current = current.next
            print("None")

    # Definição do método para printar o tamanho de cada uma das listas encadeadas dos slots
    # e calcular a média
    def imprimir_tamanhos_slots(self):
        total_tamanho = 0
        for i in range(self.size):
            current = self.table[i]
            tamanho_lista = 0
            while current is not None:
                tamanho_lista += 1
                current = current.next
            print(f"Tamanho slot {i}: {tamanho_lista}")
            total_tamanho += tamanho_lista
        media = total_tamanho / self.size
        print(f"Tamanho médio das listas encadeadas: {media:.2f}")

# Main
# Criação de uma tabela hash com 43 slots
hash_table = Hash_table(43)

# Inserindo 500 chaves geradas aleatoriamente
print(f'=== Inserindo as chaves na Hash Table ===')
for i in range (0, 500):
    numero = random.randint(1, 2000)
    hash_table.inserir_chave(f"Numero {i}", numero)
print(f'=== Inserção concluída ===')

# Imprimindo tamanhos de cada uma das listas encadeadas e calculando a média
print('')
print(f'=== Imprimindo os tamanhos de cada uma das listas encadeadas ===')
hash_table.imprimir_tamanhos_slots()

# Buscando 3 chaves que pertençam à tabela hash
print('')
print(f'=== Buscando 3 chaves que pertençam à tabela hash ===')
print("Busca por Numero 2:", hash_table.buscar_chave("Numero 2"))
print("Busca por Numero 6:", hash_table.buscar_chave("Numero 6"))
print("Busca por Numero 15:", hash_table.buscar_chave("Numero 15"))

# Removendo as 3 chaves buscadas
print('')
print(f'=== Removendo as 3 chaves anteriormente buscadas ===')
hash_table.remover_chave("Numero 2")
hash_table.remover_chave("Numero 6")
hash_table.remover_chave("Numero 15")

# Buscando as 3 chaves que, agora, não pertencem mais à tabela hash
print('')
print(f'=== Buscando as mesmas 3 chaves que, agora, não pertencem mais à Hash Table ===')
print("Busca por Numero 2:", hash_table.buscar_chave("Numero 2"))
print("Busca por Numero 6:", hash_table.buscar_chave("Numero 6"))
print("Busca por Numero 15:", hash_table.buscar_chave("Numero 15"))

# Imprimindo a Hash Table
print('')
print(f'=== Imprimindo todas as chaves da Hash Table ===')
hash_table.imprimir_chaves()