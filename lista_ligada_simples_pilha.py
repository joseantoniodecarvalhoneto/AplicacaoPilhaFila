class No:
    def __init__(self, dado):
        """Criação do nó"""
        self.dado = dado
        self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def is_empty(self):
        """Retorna se a lista esta vazia"""
        return self.tamanho == 0

    def push(self,elemento):
        """Adiciona um elemento no topo da lista"""
        no = No(elemento)
        no.proximo = self.topo
        self.topo = no 
        self.tamanho += 1

    def pop(self):
        """Remove um elemento e retornando-o"""
        if self.is_empty():
            return IndexError("A lista esta vazia.Impossível retirar elementos")
        dado_remvovido = self.topo.dado
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return dado_remvovido
    
    def peek(self):
        """Retorna o último elemento sem remove-lo da pilha"""
        if self.is_empty():
            return IndexError("A lista esta vazia.")
        
    def __str__(self):
        """Transforma os argumentos em strings"""
        elementos = []
        ponteiro_atual = self.topo
        while ponteiro_atual:
            elementos.append(str(ponteiro_atual.dado))
            ponteiro_atual = ponteiro_atual.proximo
        return " ".join(elementos)
    