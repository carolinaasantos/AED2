# Hash table com tratamento de colisões por endereçamento aberto -> Double Hashing

from math import floor
from random import randint


# Tabela Hash de Endereçamento Aberto
class HashTable:
    def __init__(self, m):
        self.size = m
        self.T = [None] * m  # Tabela (T) com as m posições estabelecidas
        self.acessos = 0

    # Função Hash auxiliar 1 (double hashing)
    def fn_aux1(self, key):  # Utiliza-se o método da divição com o valor de m = 1019
        result = key % self.size

        return result

    # Função Hash auxiliar 2 (double hashing)
    def fn_aux2(self, key):  # Utiliza o método da divisão com m = 1013
        m_linha = 1013
        result = 1 + (key % m_linha)

        return result

    # Função Hash para Double Hashing
    def fn_hash(self, key, i):
        # O index depende das duas fn. aux e do i
        index = (self.fn_aux1(key) + i * self.fn_aux2(key)) % self.size

        return index

    # Função de inserção na Tabela Hash
    def hash_insert(self, key):
        i = 0  # Inicializa o contador

        while i != self.size:  # Enquando não chega ao final da tabela...
            q = self.fn_hash(key, i)
            # Se houver espaço para adicionar essa chave na posição q, ela é adicionada.
            if self.T[q] is None:
                self.T[q] = key
                return q

            # Se encontrar alguma chave repetida, não a adiciona e termina o processo
            if self.T[q] == key:
                return False

            i += 1  # Atualiza o contador (próxima tentativa da função hash)

        # Se a tabela estiver cheia ou h(key, i) sempre igual a posição de outras chaves...
        print(f'Não há posição livre para a chave {key}')
        return False

    # Funcão de busca na Tabela Hash
    def hash_search(self, key):
        i = 0  # Inicializa o contador
        acessos = 1  # Inicializa o contador de acessos
        q = self.fn_hash(key, i)  # Calcula a primeira posição para a key

        # Enquanto não achar uma posição calculada que esteja vazia, nem verificar todas as posições possíveis...
        while self.T[q] is not None and i != self.size:
            if self.T[q] == key:
                self.acessos += acessos
                print(f'A chave {key} foi encontrada após {acessos} acesso(s).')
                return q  # Encontrou a chave na posição q

            i += 1  # Atualiza o contador
            acessos += 1
            q = self.fn_hash(key, i)  # Calcula a próxima posição para a key

        # Ao sair do loop, sabemos que a chave não foi encontrada
        print(f'A chave {key} não foi encontrada na tabela hash após {acessos} acesso(s)')
        self.acessos += acessos
        return False

    def hash_remove(self, key):
        # Procura a chave que se deseja remover
        busca = self.hash_search(key)

        if busca is not False:
            self.T[busca] = None
            return True

        return False

    def print_hash(self):
        print('=' * 20)
        for d in range(0, self.size):  # Imprime os elementos presentes na tabela até o momento
            print(f'[{d}] = {self.T[d]}')
        print('=' * 20)


# Código Principal
if __name__ == '__main__':
    key = c = 0
    TH = HashTable(1019)  # Cria uma tabela Hash com 1019 slots
    achados = []

    # Inserção de 500 chaves distintas na tabela
    while c < 500:
        key = randint(1, 2000)
        insercao = TH.hash_insert(key)

        # Evita que a chave seja repetida ou que sejam adicionadas menos chaves que o desejado
        if insercao is not False:
            c += 1

    # Imprime os valores adicionados a tabela
    print('VALORES ADICIONADOS ATÉ O MOMENTO (500 chaves)')
    TH.print_hash()

    print()

    # Busca de 10 valores que pertencem a Tabela Hash
    print('==== BUSCA DE 10 CHAVES QUE PERTENCEM A HASH TABLE ====')
    i = c = 0  # Inicializa o contador
    while c < 10:  # Busca 10 chaves que pertencem a Hash Table
        if TH.T[i] is not None:
            key = TH.T[i]
            pos = TH.hash_search(key)
            print(f'Posição da chave na tabela: {pos} \n')
            # Adiciona a chave a um array externo
            achados.append(TH.T[pos])
            # Atualiza o contador
            c += 1
        # Atualiza o índice
        i += 10

    # Calcula a média de acessos
    print('=' * 10, end=' ')
    print('MÉDIA DE ACESSOS', end=' ')
    print('=' * 10)
    media = TH.acessos / c
    print(f'A média de acessos para buscar {c} chaves é {media:.1f}')

    print()

    # Remoção dos 10 valores encontrados
    print('==== REMOÇÃO DE 10 CHAVES QUE PERTENCEM A HASH TABLE ====')
    for k in range(0, len(achados)):
        if TH.hash_remove(achados[k]) is True:
            print(f'E removida com sucesso!\n')
        else:
            print('E NÃO foi removida! :O\n')

    print()

    # Busca de 10 valores que NÃO pertencem a Tabela Hash
    print('==== BUSCA DE 10 CHAVES QUE NÃO PERTENCEM A HASH TABLE ====')
    TH.acessos = 0  # Reinicializa o contador de acessos

    for k in range(0, len(achados)):  # Busca 10 chaves que não pertencem a Hash Table
        # Busca a chave na tabela
        TH.hash_search(achados[k])

    # Calcula a média de acessos
    print()
    print('=' * 10, end=' ')
    print('MÉDIA DE ACESSOS', end=' ')
    print('=' * 10)
    media = TH.acessos / (k + 1)
    print(f'A média de acessos para buscar {k + 1} chaves que não estão na Tabela Hash é {media:.1f}')