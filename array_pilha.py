import array

class arrayPilha():

    def __init__(self, capacidade = 50):
        """Inicia a pilha com uma capacidade fixa usando a biblioteca array.
        O array é pre alocado com valores nulos ['\0'].
        Tipo de dados do array: String('u')."""
        self.capacidade = capacidade
        self.dado = array.array ('u', ['\0'] * self.capacidade)
        self.topo = 0

    def size(self):
        """Retorna o número de elementos da pilha"""
        return self.topo()
    
    def is_empty(self):
        """Verifica se a pilha esta vazia(topo = 0)"""
        return self.topo == 0
    
    def is_full(self):
        """Verifica se a pilha esta cheia"""
        return self.topo == self.capacidade

    def push(self, elemento):
        "Adiciona um elemento no topo da pilha"
        if self.is_full():
            raise IndexError("Estouro da pilha('Overflow')")
        self.dado[self.topo] = elemento
        self.topo += 1

    def pop(self):
        """Remove e retorna o elemento ao topo"""
        self.topo -= 1
        elemeto_removido = self.dado[self.topo]
        self.dado[self.topo] = '\0' #Remove da memória a parte da pilha usada pelo elemento
        return elemeto_removido
    
    def peek(self):
        """Retorna o elemento do topo da lista sem remove-lo"""
        if self.is_empty():
            raise IndexError("A pilha esta vazia")
        return self.dado[self.topo - 1]
    
    def __str__(self):
        """Cria uma representação em strings dos elementodos da pilha"""
        elementos = []
        for i in range(self._topo):
            elementos.append(self._dados[i])
        return str(elementos)
        
    