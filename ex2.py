'''2) Implementar um algoritmo usando pilha para checar se os símbolos de abertura e
fechamento de tags de arquivos html estão corretos. Apresentar 03 casos de teste.
'''

class Pilha():
    def __init__(self):
        self.elementos = []

    def VerificaPilhaVazia(self):
        return len(self.elementos) == 0

    def AddElementos(self, elemento):
        self.elementos.append(elemento)

    def popElementos(self):
        if not self.VerificaPilhaVazia():
            return self.elementos.pop()
        return None
    
    def OlhaUltimoElemento(self):
        if not self.VerificaPilhaVazia():
            return self.elementos[-1]
        return None
    

def Verificacao(html):
    pilha = Pilha()
    contador = 0

    while contador < len(html):
        if html[contador] == "<":
            contadorFechamento = html.find(">", contador+1)
            if contadorFechamento == -1:
                return False
    
            tag = html[contador+1:contadorFechamento]

            if not tag.startswith("/"):  
                pilha.AddElementos(tag)
            else:  
                nome_tag = tag[1:]
                if pilha.VerificaPilhaVazia() or pilha.OlhaUltimoElemento() != nome_tag:
                    return False
                pilha.popElementos()

            contador = contadorFechamento
        contador += 1
    
    return pilha.VerificaPilhaVazia()

teste1 = "<html><body><p></p></body></html>"  
teste2 = "<html><body><p></body></html>"      
teste3 = "<div><span></div></span>"           

print(Verificacao(teste1))  
print(Verificacao(teste2))  
print(Verificacao(teste3))  
