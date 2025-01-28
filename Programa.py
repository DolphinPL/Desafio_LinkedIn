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

#Criar variáveis 
tarefas_pendentes = ["Lavar roupa", "Estudar Python", "Estudar inglês"]
tarefas_concluidas =["Ir na academia"]
menu = ["Adicionar tarefa", "Ver tarefa(s)", "Atualizar tarefas", "Completar tarefas", "Deletar tarefas que foram completadas", "Sair"]
aux_tarefas_pendentes = tarefas_pendentes[:]
aux_tarefas_concluidas = tarefas_concluidas[:]

#Função para limpar o terminal
def limpar_terminal():
    # Limpa a tela dependendo do sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

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

#Função para adicionar tarefa
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

#Função para Ver tarefa(s) adicionada
def ver_tarefas():
    tamanho_pendentes = len(tarefas_pendentes) 
    print("******** TAREFAS ********\n")
    for indice, tarefa in enumerate(tarefas_pendentes):#Tarefas não concluídas ficam com a coluna de check vazia
        print(f"[ ] {indice+ 1} - {tarefa}")
    for indice, tarefa in enumerate(tarefas_concluidas):#Coloca o sinal de check nas tarefas que ja foram concluídas
        print(f"[\u2714] {indice + 1 + tamanho_pendentes} - {tarefa}") 
    print("\nCOMANDOS\n[1] - RETORNAR AO MENU \n[2] - FINALIZAR PROGRAMA")

#Função para Atualizar tarefas
def att_tarefas():
    global tarefas_pendentes
    global tarefas_concluidas
    global aux_tarefas_pendentes
    global aux_tarefas_concluidas
    
    tarefas_pendentes = aux_tarefas_pendentes[:]
    tarefas_concluidas = aux_tarefas_concluidas[:]
    
    limpar_terminal()
    print("Tarefas atualizadas com SUCESSO!")
    
#Criar Função para Completar tarefas
def concluir_tarefas():
    limpar_terminal()
    print("******** TAREFAS CONCLUÍDAS ********\n")
    for indice, tarefa in enumerate(aux_tarefas_pendentes):#Tarefas não concluídas ficam com a coluna de check vazia
        print(f"{indice+ 1} - {tarefa}")
    print("\nCOMANDOS\n[0] - RETORNAR AO MENU")
    
#Função para Deletar tarefas que foram completadas
def deletar_concluidas():
    global aux_tarefas_concluidas
    aux_tarefas_concluidas = []
    
#Função para Sair
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

    if validar == 1: #Para adicionar tarefa
        limpar_terminal()
        adicionar_tarefa()
        main()
        
    elif validar == 2: #Para Vizualizar as tarefas
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
            
    elif validar == 3: #Para atualizar as tarefas
        att_tarefas()
        main()    
        
    elif validar == 4: #Para Concluir uma tarefa
        concluir_tarefas() 
        comando = entrada_numerica("\nSelecione o número referente a tarefa que deseja concluir:")
        tamanho = len(aux_tarefas_pendentes) 
        while comando < 0 and comando > tamanho:#A função ficará repetindo até o usuário colocar um comando válido
            limpar_terminal()
            print("Comando inválido. Por favor, tente novamente!\n")
            concluir_tarefas()
            comando = entrada_numerica("\nSelecione o número referente a tarefa que deseja concluir:")
        if comando == 0:
            limpar_terminal()
            main()
        else: 
            escolha_usuario = comando - 1
            aux_tarefas_concluidas.append(aux_tarefas_pendentes[escolha_usuario])
            del aux_tarefas_pendentes[escolha_usuario]
            main()

    elif validar == 5: #Para deletar todas as tarefas concluídas
        deletar_concluidas()
        print("As tarefas concluídas foram excluídas.")
        main()

    elif validar == 6: #Para finalizar o programa
            sair()

limpar_terminal()
main()