class Node:
    def __init__(self, palavra):
        self.palavra = palavra
        self.altura = 1
        self.left = None
        self.right = None

class AVLTree(Node):
    def __init__(self):
        self.root = None

    def Altura(self, node):
        return node.altura if node else 0

    def Atualizar_altura(self, node):
        node.altura = max(self.Altura(node.left), self.Altura(node.right)) + 1

    def Fator_de_balanceamento(self, node):
        return self.Altura(node.left) - self.Altura(node.right)

    def Rotacao_esq(self, z):
        if z.right is None:
          return z
        y = z.right
        z.right = y.left
        y.left = z
        self.Atualizar_altura(z)
        self.Atualizar_altura(y)
        return y

    def Rotacao_dir(self, y):
        if y.left is None:
            return y
        z = y.left
        y.left = z.right
        z.right = y
        self.Atualizar_altura(y)
        self.Atualizar_altura(z)
        return z


    def Rebalanceamento(self, node):
        self.Atualizar_altura(node)
        balance = self.Fator_de_balanceamento(node)

        if balance > 1:
            if self.Fator_de_balanceamento(node.left) < 0:
                node.left = self.Rotacao_dir(node.left)
            return self.Rotacao_esq(node)
        elif balance < -1:
            if self.Fator_de_balanceamento(node.right) > 0:
                node.right = self.Rotacao_esq(node.right)
            return self.Rotacao_dir(node)

        return node

    def inserir(self, palavra):
        self.root = self._inserir(self.root, palavra)

    def _inserir(self, node, palavra):
        if not node:
            return Node(palavra)

        if palavra <= node.palavra:
            node.left = self._inserir(node.left, palavra)
        else:
            node.right = self._inserir(node.right, palavra)

        self.Atualizar_altura(node)
        balance = self.Fator_de_balanceamento(node)

        # Rebalanceamento
        if balance > 1 and palavra <= node.left.palavra:
            return self.Rotacao_dir(node)
        if balance < -1 and palavra > node.right.palavra:
            return self.Rotacao_esq(node)
        if balance > 1 and palavra > node.left.palavra:
            node.left = self.Rotacao_esq(node.left)
            return self.Rotacao_dir(node)
        if balance < -1 and palavra <= node.right.palavra:
            node.right = self.Rotacao_dir(node.right)
            return self.Rotacao_esq(node)

        return node


    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.palavra)
            self.inorder(node.right)

    def Buscar(self, prefix):
        results = []
        self.Busca_arvore(self.root, prefix, results)
        return results

    def Busca_arvore(self, node, prefix, results):
        if node is None:
            return

        if node.palavra.startswith(prefix):
            results.append(node.palavra)
        self.Busca_arvore(node.left, prefix, results)
        self.Busca_arvore(node.right, prefix, results)



    def contem(self, palavra):
        return self._contem(self.root, palavra)
    
    def _contem(self, node, palavra):
        if node is None:
            return False
        if node.palavra == palavra:
            return True
        if palavra < node.palavra:
            return self._contem(node.left, palavra)
        return self._contem(node.right, palavra)
