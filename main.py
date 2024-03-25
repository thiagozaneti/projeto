from database import times, campeonato
from lib.funcoes import (
    visualizar_times,
    atualizar_times,
    apagar_times,
    visualizar_jogadores,
    apagar_jogadores,
    cadastrar_novo_jogador,
    cadastrar_novo_time,
    adicionar_campeonato,
    adicionar_time_camp,
)

if __name__ == "__main__":

    def menu():
        while True:
            print(
                """
Gerenciar Times[1]
Gerenciar Campeonato[2]
                """
            )
            user_select = int(input("Digite a sua escolha: "))
            if user_select == 1:
                print(
                    """
1 - Visualizar Times
2 - Atualizar Time
3 - Deletar Time
4 - Cadastrar Novo Time
5 - Deletear Jogador
6 - Cadastrar novo jogador"""
                )
                second_select = int(input("Digite a sua escolha: "))
                if second_select == 1:
                    visualizar_times(times)
                elif second_select == 2:
                    atualizar_times(times)
                elif second_select == 3:
                    apagar_times(times)
                elif second_select == 4:
                    cadastrar_novo_time(times)
                elif second_select == 5:
                    apagar_jogadores(times)
                elif second_select == 6:
                    cadastrar_novo_jogador(
                        times
                    )  # Substitua 'pass' com a chamada da função adequada

            elif user_select == 2:
                print(
                    """ 
1 - Adicionar Campeonato
2- Adicionar Time nos campeonatos
"""
                )
                terceiro_select = int(input("Digite a sua escolha: "))
                if terceiro_select == 1:
                    adicionar_campeonato(campeonato)
                elif terceiro_select == 2:
                    adicionar_time_camp(campeonato)

    menu()
