def adicionarSorteado(sorteados):
    numAdd = random.randint(0, 100)
    sorteados.append(numAdd)
    print(sorteados)

def adicionarAluno(alunos, matricula, nome):
    alunos[matricula] = nome

def exibirAlunos(alunos):
    for chave, valor in alunos.items():
        print("Matricula:", chave, "Aluno:", valor)

def buscarAluno(alunos, matricula):
    for achado, nome in alunos.items():
        if(achado == matricula):
            print("Matricula encontrado! ->", achado, "Aluno:", nome)

def Menu():
    contador = 0
    while(contador == 0):
        escolha = eval(input("1 para adicionar um numero a lista, 2 para adicionar um aluno a lista, 3 para exibir os alunos, 4 para buscar aluno e 5 para sair."))
        if(escolha == 1):
            adicionarSorteado(sorteados)
        elif(escolha == 2):
            matricula = eval(input("Digite a matricula para adicionar: "))
            nome = input("Digite o nome do aluno: ")
            adicionarAluno(alunos, matricula, nome)
        elif(escolha == 3):
            exibirAlunos(alunos)
        elif(escolha == 4):
            matricula = eval(input("Digite a matricula a ser buscada: "))
            buscarAluno(alunos, matricula)
        else:
            contador = 1

Menu()
            
            
