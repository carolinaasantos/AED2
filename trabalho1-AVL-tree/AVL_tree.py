# Declaração da classe Node
class Node:
    def __init__(self, key, p=None):
        self.key = int(key)
        self.left = None
        self.right = None
        self.height = 1
        self.p = p

# Declaração da classe AVL_binary_tree
class AVL_binary_tree:
    def __init__(self):
        self.root = None

    # Método que encontra a altura de um nó
    def encontra_altura(self, node):
        if not node:
            return 0
        return node.height
        
    # Método que insere nós na árvore AVL
    def inserir_chave(self, key):
        def _inserir_chave(node, key, p=None):
            # Caso o nó seja nulo
            if not node:
                print(f"Inserindo {key}")
                return Node(key, p)
            # Se a chave for menor que o pai, deve-se inserir à esquerda
            elif key < node.key:
                node.left = _inserir_chave(node.left, key, node)
            # Se não, deve-se inserir à direita
            else:
                node.right = _inserir_chave(node.right, key, node)

            # Atualiza a altura do nó
            node.height = 1 + max(self.encontra_altura(node.left), self.encontra_altura(node.right))

            # Aqui devemos garantir que a árvore continua balanceada, verificando o fator de 
            # balanco do nó e realizando as rotações necessárias
            b = self.fator_balanco(node)

            if b > 1 and key < node.left.key:
                #print(f"Rotação à direita no nó {node.key}")
                return self.rotacao_dir(node)
            if b < -1 and key > node.right.key:
                #print(f"Rotação à esquerda no nó {node.key}")
                return self.rotacao_esq(node)
            if b > 1 and key > node.left.key:
                #print(f"Rotação esquerda-direita no nó {node.key}")
                return self.rotacao_esq_dir(node)
            if b < -1 and key < node.right.key:
                #print(f"Rotação direita-esquerda no nó {node.key}")
                return self.rotacao_dir_esq(node)
            
            return node
        
        self.root = _inserir_chave(self.root, key)
    
    def sucessor(self, node):
        if node is None or node.left is None:
            return node
        return self.sucessor(node.left)

    # Método que define a remoção de uma chave da árvore
    def remover_chave(self, node, key):
        # Caso o nó seja nulo, retorna nulo
        if not node:
            return node

        # Se a chave a ser removida é menor que o nó atual, analisamos a subárvore à esquerda
        if key < node.key:
            node.left = self.remover_chave(node.left, key)
        # Se a chave é maior, analisa-se a subárvore à direita
        elif key > node.key:
            node.right = self.remover_chave(node.right, key)
        # Se for igual à chave do nó atual, este é o nó a ser removido
        else:
            # Se o nó não tem filho à esquerda, substitui o nó pelo filho à direita
            if node.left is None:
                temp = node.right
                node = None
                return temp
            # Se o nó não tem filho à direita, substitui o nó pelo filho à esquerda
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # Se o nó tiver dois filhos, encontra o nó com menor valor na subárvore à direita,
            # copia o valor do sucessor para o nó atual e remove o sucessor da subárvore
            temp = self.sucessor(node.right)
            node.key = temp.key
            node.right = self.remover_chave(node.right, temp.key)

        # Atualiza a altura do nó
        node.height = 1 + max(self.encontra_altura(node.left), self.encontra_altura(node.right))

        # Aqui devemos garantir que a árvore continua balanceada, verificando o fator de 
        # balanco do nó e realizando as rotações necessárias
        balanco = self.fator_balanco(node)

        if balanco > 1 and self.fator_balanco(node.left) >= 0:
            return self.rotacao_dir(node)
        if balanco > 1 and self.fator_balanco(node.left) < 0:
            return self.rotacao_esq_dir(node)
        if balanco < -1 and self.fator_balanco(node.right) <= 0:
            return self.rotacao_esq(node)
        if balanco < -1 and self.fator_balanco(node.right) > 0:
            return self.rotacao_dir_esq(node)

        return node

    # Método que define o percurso inorder de uma árvore
    def inorder(self, root):
        res = []
        if root:
            # Percorre a subárvore à esquerda
            res = self.inorder(root.left)
            res.append(root.key)
            # Percorre a subárvore à direita
            res = res + self.inorder(root.right)
        return res

    # Método que encontra o fator de balanço de um nó
    def fator_balanco(self, node):
        if not node:
            return 0
        # Retorna o fator balanço dado por altura árvore à esquerda - altura da árvore à direita
        b = self.encontra_altura(node.left) - self.encontra_altura(node.right)
        return b

    # Método que define a rotação à esquerda de um nó
    def rotacao_esq(self, x):
        # x é o Node que precisa ser rotacionado
        y = x.right
        alpha = y.left
        y.left = x
        x.right = alpha
        y.p = x.p
        x.p = y
        if alpha:
            alpha.p = x

        # Atualizando a altura dos nós
        x.height = 1 + max(self.encontra_altura(x.left), self.encontra_altura(x.right))
        y.height = 1 + max(self.encontra_altura(y.left), self.encontra_altura(y.right))

        # y passa a assumir o lugar de x
        return y

    # Método que define a rotação à direita de um nó
    def rotacao_dir(self, y):
        # y é o Node que precisa ser rotacionado
        x = y.left
        beta = x.right
        x.right = y
        y.left = beta
        x.p = y.p
        y.p = x
        if beta:
            beta.p = y

        # Atualizando a altura dos nós
        y.height = 1 + max(self.encontra_altura(y.left), self.encontra_altura(y.right))
        x.height = 1 + max(self.encontra_altura(x.left), self.encontra_altura(x.right))

        # x passa a assumir o lugar de y
        return x

    # Método que define a rotação à esquerda e à direita de um nó
    def rotacao_esq_dir(self, z):
        z.left = self.rotacao_esq(z.left)
        return self.rotacao_dir(z)

    # Método que define a rotação à direita e à esquerda de um nó
    def rotacao_dir_esq(self, z):
        z.right = self.rotacao_dir(z.right)
        return self.rotacao_esq(z)
    
    # Método que define os fatores de balanço de todos os nós de uma árvore
    def fatores_balanco(self, node, fatores):
        if node:
            fatores[node.key] = self.fator_balanco(node)
            self.fatores_balanco(node.left, fatores)
            self.fatores_balanco(node.right, fatores)
        return fatores

# Main

# Declaração da árvore binária AVL
tree = AVL_binary_tree()

chaves = [11, 12, 13, 14, 15, 20, 19, 18, 17, 16, 5, 4, 3, 2, 1, 6, 7, 8, 9, 10]

# Inserção das chaves
print(f'=== Inserindo as chaves ===')
for chave in chaves:
    tree.inserir_chave(chave)
print(f'=== Inserção concluida ===')

# Mostrando o percurso inorder, com a árvore já balanceada
print('')
print(f'=== Mostrando o percurso inorder ===')
print("Percurso inorder: ", tree.inorder(tree.root))

# Calculando o fator de balanço de cada nó
print('')
print(f'===  Calculando o fator de balanço de todos os nós ===')
fatores = tree.fatores_balanco(tree.root, {})
for chave, fator in fatores.items():
    print(f"Fator de balanço do nó {chave}: {fator}")

# Removendo as chaves 5, 10 e 15
print('')
print('=== Removendo a chave 5 ===')
tree.remover_chave(tree.root, 5)

print('=== Removendo a chave 10 ===')
tree.remover_chave(tree.root, 10)

print('=== Removendo a chave 15 ===')
tree.remover_chave(tree.root, 15)

# Mostrando o percurso inorder, após as remoções
print('')
print(f'=== Mostrando o percurso inorder ===')
print("Percurso inorder: ", tree.inorder(tree.root))

# Calculando novamente o fator de balanço de cada nó
print('')
print(f'===  Calculando o fator de balanço de todos os nós ===')
fatores = tree.fatores_balanco(tree.root, {})
for chave, fator in fatores.items():
    print(f"Fator de balanço do nó {chave}: {fator}")
