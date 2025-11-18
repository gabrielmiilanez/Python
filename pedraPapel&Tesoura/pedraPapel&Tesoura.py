#Jogo básico de Pedra, Papel e Tesoura.

def player_choice(value):
    match value:
        case "1":
            return "Pedra"
        case "2":
            return "Papel"
        case "3":
            return "Tesoura"
        case _:
            return "Escolha inválida"

def determine_winner(player1, player2):
    if player1 == player2:
        return "Empate!"
    elif (player1 == "1" and player2 == "3") or (player1 == "2" and player2 == "1") or (player1 == "3" and player2 == "2"):   
        return "Player 1 vence!"
    else:
        return "Player 2 vence!"    

print("Player 1: Escolha uma opção:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")
player1 = player_choice(input("Digite o número da sua escolha: "))

print("\n" * 50)

print("Player 2: Escolha uma opção:")
print("1 - Pedra")  
print("2 - Papel")
print("3 - Tesoura")
player2 = player_choice(input("Digite o número da sua escolha: "))

print(determine_winner(player1, player2))

