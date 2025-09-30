'''6) implementar a versão recursiva de percorrimento (visitação) de pilha e fila implementados
com listas encadeadas simples.'''

class no:  #criação do nó com espaço do ponteiro e do dado
    def __init__ (self, dado): 
        self.dado = dado
        self.proximo = None #ponteiro ainda vazio pq acabei de criar

class estrutura_base:
    def __init__ (self):  #base da pilha e fila, criando o head que aponta para o primeiro nó
        self.head = None 

    def vazia(self):   #verifica se a lista está vazia
        return self.head is None
    
class fila(estrutura_base):
    def percorre_recursivo(self,atual):
        if atual is None:
            return
        
        print(atual.dado) #mostra o dado desse nó
        self.percorre_recursivo(atual.proximo)  #função recursiva para passar para o próximo nó

    def percorrer_fila(self):
        if self.vazia():
            print("A lista está vazia.")
            return
        
        print("FILA: ")
        self.percorrer_recursivo(self.head)  #percorre a lista com recursão, até que o ultimo ponteiro esteja vazio

class pilha(estrutura_base):
    def percorrer_recursivo(self, atual):
        if atual is None:
            return
        
        print(atual.dado)
        self.percorrer_recursivo(atual.proximo)

    def percorrer_pilha(self):
        if self.vazia():
            print("A pilha está vazia.")
            return
        print("PILHA: ")
        self.percorrer_recursivo(self.head)
        

















