import time
import random
plays = ['Rock', 'Paper', 'Scissors', 'Nothing']
cpu_score = 0
player_score = 0

def get_computer_choice():
    return random.choice(plays)

def get_user_choice():
    start_time = time.time()
    with open('RPS-Template.py', "rb") as cam:
        code = compile(cam.read(), 'RPS-Template.py', "exec")
    exec(code)
    choice_input = max(zip(prediction[0], plays))[1]
    elapsed_time = int(( time.time() - start_time ) // 1)
    print(f"{elapsed_time} seconds")
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
    while cpu_score < 3 and player_score < 3:
        cpu_play = get_computer_choice()
        player_play = get_user_choice()
        get_winner(cpu_play, player_play)
        print(f"Scoreboard. CPU = {cpu_score}, Player = {player_score}")
    print("game over")


play()