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
menu = ["Adicionar tarefa", "Ver tarefa(s) adicionada", "Atualizar tarefas", "Completar tarefas", "Deletar tarefas que foram completadas", "Sair"]

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

#Criar Função para Ver tarefa(s) adicionada
def ver_tarefas():
    print("******** TAREFAS ********\n")
    tamanho_pendentes = len(tarefas_pendentes) 
    for indice, tarefa in enumerate(tarefas_pendentes):#Tarefas não concluídas ficam com a coluna de check vazia
        print(f"[ ] {indice+ 1} - {tarefa}")
    for indice, tarefa in enumerate(tarefas_concluidas):#Coloca o sinal de check nas tarefas que ja foram concluídas
        print(f"[\u2714] {indice + 1 + tamanho_pendentes} - {tarefa}") 
    print("\nCOMANDOS\n[1] - RETORNAR AO MENU \n[2] - FINALIZAR PROGRAMA")

#Criar Função para Atualizar tarefas

#Criar Função para Completar tarefas

#Criar Função para Deletar tarefas que foram completadas

#Criar Função para Sair
def sair():
    print("Programa Finalizado!!!") #Apenas exibe a mensagem para informar o usuário 


def main():
    limpar_terminal()

    menu_principal()

    validar = entrada_numerica("\nSelecione uma ação (Digite o número correspondente): ")
    while validar > 6 or validar < 1:
        limpar_terminal()
        print("Comando inválido. Por favor, tente novamente!")
        menu_principal()
        validar = entrada_numerica("\nSelecione uma ação (Digite o número correspondente): ")

    if validar == 2:
        limpar_terminal()
        ver_tarefas()
        comando = entrada_numerica("\n ")
        while comando > 2 or comando < 1:#A função ficará repetindo até o usuário colocar um comando válido
            limpar_terminal()
            print("Comando inválido. Por favor, tente novamente!\n")
            ver_tarefas()
            comando = entrada_numerica("\nSelecione uma ação (Digite o número correspondente): ")
        if comando == 1:
            main()
        else: 
            sair()
            
    if validar == 6:
            sair()

main()