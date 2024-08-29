def adicionar_tarefa(tarefas, nome_tarefa):

    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return



def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")



def atualizar_tarefa(tarefas):
    nome_da_tarefa = input("Qual tarefa deseja atualizar?")
    print(f"\nO que deseja atualizar na tarefa {nome_da_tarefa}? ")
    print("1. Nome")
    print("2. Mudar status de completada para não completada?")
    escolha = input("Digite sua escolha:")

    if escolha == "1":
        nome_atualizado = input(f"O nome atual da tarefa é: {nome_da_tarefa}, Para qual nome deseja atualiza-la?")
        for tarefa in tarefas:
            if tarefa["tarefa"] == nome_da_tarefa:
                tarefa["tarefa"] = nome_atualizado
                print("Nome atualizado com sucesso!")

    elif escolha == "2":
        for tarefa in tarefas:
            if tarefa["tarefa"] == nome_da_tarefa:
                tarefa["completada"] = False


def completar_tarefa(tarefas):
    nome_da_tarefa = input("Qual tarefa deseja completar?")
    for tarefa in tarefas:
        if tarefa["tarefa"] == nome_da_tarefa:
            tarefa["completada"] = True

def deletar_completadas(tarefas):
    print("Tem certeza que deseja deletar as tarefas completadas? (Elas seram excluidas permanentemente!)")
    escolha = input("S / N ?")
    if escolha == "S" or "s":
        for indice, tarefa in enumerate(tarefas):
            if tarefa["completada"] == True:
                del tarefas[indice]
                



        

tarefas = []    


while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input('Digite a sua escolha:')




    if escolha == "1":
         
         nome_tarefa = input("Digite o nome da tarefa aqui: ")
         adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == "2":

        ver_tarefas(tarefas) 


    elif escolha == "3":
        atualizar_tarefa(tarefas)
        

    elif escolha == "4":
        completar_tarefa(tarefas)

    elif escolha == "5":
        deletar_completadas(tarefas)
         
    elif escolha == "6":
        break

    

    print("Programa finalizado")

