'''4) Implementar um algoritmo usando pilha para verificar (consistir) e avaliar o resultado de
uma expressão em notação posfixa. Apresentar 03 casos de teste.'''

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
    
def NotacaoPosFixa(expressao):
    pilha = Pilha()

    for elemento in expressao.split():
        if elemento.isdigit():  
            pilha.AddElementos(int(elemento))
        else:
            op2 = pilha.popElementos()
            op1 = pilha.popElementos()

            if op1 is None or op2 is None:
                raise ValueError("Expressão inválida: faltam operandos.")

            if elemento == "+":
                pilha.AddElementos(op1 + op2)
            if elemento == "-":
                pilha.AddElementos(op1 - op2)
            if elemento == "*":
                pilha.AddElementos(op1 * op2)
            if elemento == "/":
                pilha.AddElementos(op1 / op2)

    resultado = pilha.popElementos()
    if not pilha.VerificaPilhaVazia():
        raise ValueError("Expressão inválida: operandos sobrando.")
    
    return resultado

exp1 = "9 4 +"
exp2 = "5 1 5 + 4 * + 3 -"   
exp3 = "10 11 6 * + 5 -"       

print(f"Expressão: {exp1} = {NotacaoPosFixa(exp1)}")
print(f"Expressão: {exp2} = {NotacaoPosFixa(exp2)}")
print(f"Expressão: {exp3} = {NotacaoPosFixa(exp3)}")