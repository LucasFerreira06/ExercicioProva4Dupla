"""
QUESTAO 3 PROVA:

Recursividade é quando uma determinada função chama a si mesma dentro do seu escopo. Exemplo:
"""

def imprimir(x,y):
    if(x == y):
        return x
    if(x < y):
        print(x)
        return imprimir(x + 1, y)
    print(x)
    return imprimir(x - 1, y)

x = int(input("Digite o valor de x:"))
y = int(input("Digite o valor de y:"))

print(imprimir(x, y))
    
