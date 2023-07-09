import random
plays = ['Rock', 'Paper', 'Scissors']

def get_computer_choice():
    return random.choice(plays)

def get_user_choice():
    choice_input = input("Enter choice of either Rock, Paper or Scissors: ")
    return choice_input

def get_winner(cpu, player):
    print(f"Computer chose {cpu}")
    print(f"Player chose {player}")
    if player == cpu:
        print("It's a tie!")
    elif cpu == 'Rock':
        if player == 'Paper':
            print('You win!')
        else: print('You lose!')
    elif cpu == 'Paper':
        if player == 'Scissors':
            print('You win!')
        else: print('You lose!')
    elif cpu == 'Scissors':
        if player == 'Rock':
            print('You win!')
        else: print('You lose!')

def play():
    cpu_play = get_computer_choice()
    player_play = get_user_choice()
    get_winner(cpu_play, player_play)

play()