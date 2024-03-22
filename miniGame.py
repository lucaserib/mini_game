vitorias_player = 0 
vitorias_maquina = 0

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



while True:

    players_choice = Player_option()
    

    players_choice = input("Você quer jogar novamente?")
    if players_choice in ["SIM","Sim","sim",'s','S']:
        pass
    if players_choice in ['NAO', 'nao', 'Nao','n', 'N']:
        break
    else:
        break