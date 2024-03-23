
from random import choice


player_wins = 0 
machine_wins = 0

def Player_option():
   players_choice = input('Escolha entre: Pedra, Papel ou Tesoura')
   players_choice.lower()
   if players_choice == 'pedra':
       return players_choice
   elif players_choice == 'papel':
       return players_choice
   if players_choice == 'tesoura':
       return players_choice
   else:
       print("Opção inválida. Tente novamente")
       Player_option()

def Machine_option():
    machine_choice = choice(["pedra", "papel", "tesoura"])
    return machine_choice

while True:
    print('--'*30)
    players_choice = Player_option()
    machine_choice = Machine_option()
    print('--'*30)

    if (players_choice == 'pedra') and (machine_choice == 'tesoura') \
        or (players_choice == 'papel') and (machine_choice == 'pedra')\
            or (players_choice == 'tesoura') and (machine_choice == 'papel'):
        print(f'Jogador escolheu {players_choice} e a Máquina escolheu {machine_choice} Resultado: Você ganhou')
        player_wins += 1
    elif players_choice == machine_choice:
        print(f'Jogador escolheu {players_choice} e a Máquina escolheu {machine_choice} Resultado: Empate')
    else:
        print(f'Jogador escolheu {players_choice} e a Máquina escolheu {machine_choice} Resultado: Você perdeu')
        machine_wins += 1



    print('-'*30)
    print(f'Vitórias do Jogador: {player_wins}')
    print(f'Vitórias da Maquina: {machine_wins}')
    print('-'*30)
    

    players_choice = input("Você quer jogar novamente?")
    if players_choice in ["SIM","Sim","sim",'s','S']:
        pass
    if players_choice in ['NAO', 'nao', 'Nao','n', 'N']:
        break
    else:
        break