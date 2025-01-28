'''
Elaborar um gerenciador de tarefas com as seguintes funcionalidades:
1 - Adicionar tarefa
2 - Ver tarefa(s) adicionada
3 - Atualizar tarefas
4 - Completar tarefas
5 - Deletar tarefas que foram completadas
6 - Sair
'''
import os 

#Função para limpar o terminal
def limpar_terminal():
    # Limpa a tela dependendo do sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

#Criar variáveis 
tarefas_pendentes = ["Lavar roupa", "Estudar Python", "Estudar inglês"]
tarefas_concluidas =["Ir na academia"]
menu = ["Adicionar tarefa", "Ver tarefa(s)", "Atualizar tarefas", "Completar tarefas", "Deletar tarefas que foram completadas", "Sair"]
aux_tarefas_pendentes = tarefas_pendentes[:]

#Função para mostrar o menu
def menu_principal():
    print("\n******** MENU PRINCIPAL ********\n")#Realiza apenas a impressão do menu
    for indice, tarefa in enumerate(menu):
        print(f"{indice+1} - {tarefa}")
 
#Função para aceitar apenas valor numérico
def entrada_numerica(prompt):
    while True:#Caso a entrada não for numérica ira retornar erro 
        try: 
            return int(input(prompt))
        except:
            print(f"Comando invalido. Por favor, tente novamente!")

#Criar Função para adicionar tarefa
def adicionar_tarefa():
    global aux_tarefas_pendentes
    nova_tarefa = ""
    print("******** ADICIONAR TAREFA ********\n")
    print("COMANDOS\n[1] - RETORNAR AO MENU \n[2] - FINALIZAR PROGRAMA\n")
    nova_tarefa = input("Escreva qual tarefa deseja adicionar: ")
    
    if nova_tarefa == "1":
        limpar_terminal()
        main()
    elif nova_tarefa == "2":
        sair()
    else:
        aux_tarefas_pendentes.append(nova_tarefa)
        print(f"A tarefa {nova_tarefa} foi adicionada com SUCESSO!")
        return aux_tarefas_pendentes

#Criar Função para Ver tarefa(s) adicionada
def ver_tarefas():
    print("******** TAREFAS ********\n")
    tamanho_pendentes = len(tarefas_pendentes) 
    for indice, tarefa in enumerate(tarefas_pendentes):#Tarefas não concluídas ficam com a coluna de check vazia
        print(f"[ ] {indice+ 1} - {tarefa}")
    for indice, tarefa in enumerate(tarefas_concluidas):#Coloca o sinal de check nas tarefas que ja foram concluídas
        print(f"[\u2714] {indice + 1 + tamanho_pendentes} - {tarefa}") 
    print("\nCOMANDOS\n[1] - RETORNAR AO MENU \n[2] - FINALIZAR PROGRAMA\n")

#Criar Função para Atualizar tarefas
def att_tarefas():
    global tarefas_pendentes
    global aux_tarefas_pendentes
    tarefas_pendentes = aux_tarefas_pendentes[:]
    limpar_terminal()
    print("Tarefas atualizadas com SUCESSO!")
    
#Criar Função para Completar tarefas

#Criar Função para Deletar tarefas que foram completadas

#Criar Função para Sair
def sair():
    print("Programa Finalizado!!!") #Apenas exibe a mensagem para informar o usuário 
    exit()

def main():

    menu_principal()

    validar = entrada_numerica("\nSelecione uma ação (Digite o número correspondente): ")
    while validar > 6 or validar < 1:
        limpar_terminal()
        print("Comando inválido. Por favor, tente novamente!")
        menu_principal()
        validar = entrada_numerica("\nSelecione uma ação (Digite o número correspondente): ")

    if validar == 1:
        limpar_terminal()
        adicionar_tarefa()
        main()
        
    elif validar == 2:
        limpar_terminal()
        ver_tarefas()
        comando = entrada_numerica("\n ")
        while comando > 2 or comando < 1:#A função ficará repetindo até o usuário colocar um comando válido
            limpar_terminal()
            print("Comando inválido. Por favor, tente novamente!\n")
            ver_tarefas()
            comando = entrada_numerica("\nSelecione uma ação (Digite o número correspondente): ")
        if comando == 1:
            limpar_terminal()
            main()
        else: 
            sair()
            
    elif validar == 3:
        att_tarefas()
        main()      

    elif validar == 6:
            sair()

limpar_terminal()
main()