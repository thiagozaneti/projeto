import pprint ##biblioteca para visualizar o dicionario 
def visualizar_jogadores(times):
    for time, jogadores in times.items():
        print(f"Time: {time}")
        for jogador in jogadores:
            print("jogadores")
            print(f"Nome: {jogador['nome']}, Idade: {jogador['idade']}, Posição: {jogador['posicao']}")


        
def visualizar_times(times):
    for time, jogadores in times.items():
        print(f"Time: {time}")
        for jogador in jogadores:
            print(f"Nome: {jogador['nome']}, Idade: {jogador['idade']}, Posição: {jogador['posicao']}")


def atualizar_times(times):
    pprint.pprint(times)
    id_jogadores = int(input("Digite o ID do jogador para mudar: "))
    for jogadores in times.values():  # Itera sobre os valores (listas de jogadores)
        for jogador in jogadores:  # Itera sobre os jogadores na lista
            if jogador['id'] == id_jogadores:
                print("""
                O que deseja alterar?
                [1] Nome
                [2] Idade
                [3] Posição""")
                user_select = int(input("Digite o número da opção desejada: "))
                if user_select == 1:
                    jogador["nome"] = input("Digite o novo nome: ")
                elif user_select == 2:
                    jogador["idade"] = input("Digite o novo valor: ")
                elif user_select == 3:
                    jogador["posicao"] = input("Digite a nova posição: ")
                else:
                    print("Opção inválida.")
                print("jogador alterada com sucesso.")
                return  # Retorna após alterar um jogador
    print("Jogador não encontrado.")

def apagar_times(times):
    try:
        nome_time = input("Digite o nome do time para apagar: ")
        if nome_time in times:
            del times[nome_time]
            print("Time apagado com sucesso.")
        else:
            print("Time não encontrado.")
    except ValueError:
        print("Valor inválido")

def apagar_jogadores(times):
    try:
        id_jogador = input("Digite o id para remover:)")
        for jogadores in times:
            if jogadores['id'] == id_jogador:
                times.remove(jogadores)
                print("Jogador apagado com sucesso.")
                return  # Retorna após apagar um jogador
    except ValueError:
        print("Por favor, insira um número válido.")

def cadastrar_novo_jogador(times):
    id_time = input("Digite o nome do time para adicionar o jogador: ")
    novo_jogador = {}

    novo_jogador['id'] = int(input("Digite o ID do novo jogador: "))
    novo_jogador['nome'] = input("Digite o nome do novo jogador: ")
    novo_jogador['idade'] = int(input("Digite a idade do novo jogador: "))
    novo_jogador['posicao'] = input("Digite a posição do novo jogador: ")

    if id_time in times:
        times[id_time].append(novo_jogador)
        print("Novo jogador adicionado com sucesso ao time", id_time)
    else:
        print("Time não encontrado.")

def cadastrar_novo_time(times):
    try: 
        nome_time = input("Digite o nome do novo time: ")
        times[nome_time] = []
        print("Novo time adicionado com sucesso.")
    except ValueError:
        print("Por favor, insira um nome válido.")

##campeonato
        
def adicionar_campeonato(campeonato):
    try:
        nome_campeonato = input("Digite o nome do campeonato: ")
        campeonato[nome_campeonato] = []
        print("Campeonato adicionado com sucesso.")
        pprint.pprint(campeonato)
    except ValueError:
        print("Por favor, insira um nome válido.")

def adicionar_time_camp(campeonato):
    try:
        nome_campeonato = input("Digite o nome do campeonato: ")
        nome_time = input("Digite o nome do time: ")
        campeonato[nome_campeonato].append(nome_time)
        print("Time adicionado com sucesso.")
        pprint.pprint(campeonato)
    except ValueError:
        print("Por favor, insira um nome válido.")
