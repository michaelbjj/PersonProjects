# lista_de_tarefas.py

tarefas = []

def mostrar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa adicionada ainda.")
    else:
        print("\nLista de Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            status = "[x]" if tarefa["concluida"] else "[ ]"
            print(f"{i}. {status} {tarefa['descricao']}")

def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    tarefas.append({"descricao": descricao, "concluida": False})
    print("Tarefa adicionada com sucesso!")

def remover_tarefa():
    mostrar_tarefas()
    try:
        num = int(input("Digite o número da tarefa a remover: "))
        if 1 <= num <= len(tarefas):
            tarefas.pop(num - 1)
            print("Tarefa removida com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def marcar_concluida():
    mostrar_tarefas()
    try:
        num = int(input("Digite o número da tarefa concluída: "))
        if 1 <= num <= len(tarefas):
            tarefas[num - 1]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Ver tarefas")
        print("2. Adicionar tarefa")
        print("3. Remover tarefa")
        print("4. Marcar tarefa como concluída")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mostrar_tarefas()
        elif escolha == "2":
            adicionar_tarefa()
        elif escolha == "3":
            remover_tarefa()
        elif escolha == "4":
            marcar_concluida()
        elif escolha == "5":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o app
menu()
