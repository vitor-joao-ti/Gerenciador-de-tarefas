#aplicação com os mesmos requisitos, feita antes de ver as aulas
#Paradigma procedural, apenas usando listas e iterações

tarefas = []

menu = '''1. Adicionar Tarefa 
2. Ver Tarefas 
3. Renomear Tarefa 
4. Completar Tarefa 
5. Deletar Tarefas Completadas 
6. Sair
'''

def enum(text):
    if text.isnumeric():
        return int(text)
    else:
        print("Digite um número para chamar uma função")

def evazia(lista):
    if (len(lista) == 0):
        return True
    else:
        return False

def perguntar():
    opt = enum(input(menu)[0])
    while opt not in list(range(1, 7)):
        opt = enum(input(menu)[0])
    chamar(opt)

def adicionar():
    novaTarefa = input('Insira o nome da nova tarefa: ')
    tarefas.append(" [ ] " + novaTarefa)
    print("Nova Tarefa Cadastrada!")
    
def ver():
    if (evazia(tarefas)):
        print("Ainda não há tarefas cadastradas!")
    else:
        count = 1
        for tarefa in tarefas:
            print(str(count) + ". " + tarefa)
            count += 1

def renomear():
    if (evazia(tarefas)):
        print("Não há tarefas para serem renomeadas!")
        numTarefa = False
    else:
        numTarefa = enum(input("Digite o nº da tarefa a ser renomeada: "))
    
    if (numTarefa > len(tarefas) or numTarefa < 1):
        print("ERRO AO RENOMEAR")
    else:
        print("Renomeando tarefa: " + tarefas[numTarefa - 1])
        tarefaRenomeada = input("Digite a nova descrição da tarefa: ")
        tarefas.pop(numTarefa - 1)
        tarefas.insert(numTarefa - 1, " [ ] " + tarefaRenomeada)
        ver()

def completar():
    if (evazia(tarefas)):
        print("Não há tarefas para serem completadas!")
        numTarefa = False
    else:
        numTarefa = enum(input("Digite o nº da tarefa a ser completada: "))
    
    if (numTarefa > len(tarefas) or numTarefa < 1):
        print("ERRO AO COMPLETAR")
    else:
        tarefas[numTarefa - 1] = tarefas[numTarefa - 1].replace(" ", "#", 2).replace("#", " ", 1)
        ver()

def deletar():
    count = 0
    for tarefa in tarefas:
        if(tarefa.find("#") >= 0):
            tarefas.pop(count)
            count = 0
        count += 1
    print("Tarefas completadas foram deletadas, tarefas restantes: ")
    ver()

def chamar(opt):
    if(opt == 1):
        adicionar()
        perguntar()
    elif(opt == 2):
        ver()
        perguntar()
    elif(opt == 3):
        ver()
        renomear()
        perguntar()
    elif(opt == 4):
        ver()
        completar()
        perguntar()
    elif(opt == 5):
        deletar()
        perguntar()
    elif(opt == 6):
        print("Saindo...")
    else:
        print("ERRO")

perguntar()   
