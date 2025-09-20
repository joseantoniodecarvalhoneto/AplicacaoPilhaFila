from array_pilha import arrayPilha

def parentizacao(expressao):
    """A função realiza se houve o fechamento dos seguintes simbolos (), [] e {}"""
    capacidade_necessaria = len(expressao)
    pilha = arrayPilha( capacidade= capacidade_necessaria ) 

    simbolos = {')':'(', ']':'[', '}': '{'}
    abertura =  simbolos.values()

    for char in expressao:
        if char in abertura:
            try:
                pilha.push(char)
            except IndexError as e:
                print(f'Erro:{e}')
        elif char in simbolos:
            if pilha.is_empty():
                print(f"Símbolo de fechamento '{char}' não tem um par de abertura")
                return False
            topo = pilha.pop()
            if topo != simbolos[char]:
                print(f"Esperava-se simbolo de fechamento para o topo'{topo}' mas foi encontrado '{char}'")
                return False
            
    if not pilha.is_empty():
        print(f"Não foram fechados todos os símbolos")
        return False
    
    return True

def main():

    expressao1 = "{[()]()}"
    print(f"Testando expressão 1: '{expressao1}'")
    resultado1 = parentizacao(expressao1)
    print(f'{'Válida' if resultado1 else 'Inválida'}')

    expressao2 = "{[(])}"
    print(f"Testando expressão 2: '{expressao2}'")
    resultado2 = parentizacao(expressao2)
    print(f'{'Válida' if resultado2 else 'Inválida'}')

    expressao3 = "([)]"
    print(f"Testando expressão 3: '{expressao3}'")
    resultado3= parentizacao(expressao3)
    print(f'{'Válida' if resultado3 else 'Inválida'}')

main()
    





