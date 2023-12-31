from cam_manual import camera_feed
import time
import random
plays = ['Rock', 'Scissors', 'Paper', 'Nothing']
cpu_score = 0
player_score = 0

def get_computer_choice():
    return random.choice(plays[0:3])

def get_user_choice():
    start = time.time()
    print("Press the 'a' key to play your hand")
    player_play = camera_feed()
    elapsed_time = round((time.time() - start), 2)
    print(f"Player has chosen to play {player_play}. Decision took {elapsed_time} seconds")
    return player_play

def get_winner(cpu, player):
    global player_score
    global cpu_score
    print(f"Computer chose {cpu} and Player chose {player}")
    if player == cpu:
        print("It's a tie!")
    elif cpu == 'Rock':
        if player == 'Paper':
            print('Paper wraps Rock. You win!')
            player_score += 1
        else: 
            print('Rock breaks Scissors. You lose!')
            cpu_score += 1
    elif cpu == 'Paper':
        if player == 'Scissors':
            print('Scissors cuts Paper. You win!')
            player_score += 1
        else: 
            print('Paper wraps Rock. You lose!')
            cpu_score += 1
    elif cpu == 'Scissors':
        if player == 'Rock':
            print('Rock breaks Scissors. You win!')
            player_score += 1
        else: 
            print('Scissors cuts Paper. You lose!')
            cpu_score += 1

def play():
    while cpu_score < 3 and player_score < 3:
        cpu_play = get_computer_choice()
        player_play = get_user_choice()
        get_winner(cpu_play, player_play)
        print(f"Scoreboard. CPU = {cpu_score}, Player = {player_score}")
    print("game over")
    if player_score == 3:
        print("Congratulations!! you beat that pesky computer!")
    else:
        print("The man has been beaten by a machine... Better luck next time.")

play()