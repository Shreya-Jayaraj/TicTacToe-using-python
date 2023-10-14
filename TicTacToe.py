def display_board():
    
    print()
    print('_'*19)
    print()
    print('  {0:^3} | {0:^3} | {0:^3}  '.format(''))
    print('  {0:^3} | {1:^3} | {2:^3}  '.format(board[7],board[8],board[9]))
    print('  {0:^3} | {0:^3} | {0:^3}  '.format(''))
    print(' '+'-'*17+' ')
    print('  {0:^3} | {0:^3} | {0:^3}  '.format(''))
    print('  {0:^3} | {1:^3} | {2:^3}  '.format(board[4],board[5],board[6]))
    print('  {0:^3} | {0:^3} | {0:^3}  '.format(''))
    print(' '+'-'*17+' ')
    print('  {0:^3} | {0:^3} | {0:^3}  '.format(''))
    print('  {0:^3} | {1:^3} | {2:^3}  '.format(board[1],board[2],board[3]))
    print('  {0:^3} | {0:^3} | {0:^3}  '.format(''))
    print('_'*19)
    print()

def gameon_choice():

    choice = ' '
    
    while choice.upper() not in ['Y','N']:
        choice = (input('Replay? (Y/N) ')).upper()
        
        if choice not in ['Y','N']:
            print('Sorry please enter (Y/N).')
        
    if choice == 'Y':
        return True
    else:
        print('💕 Thank you for playing! 💕')
        return False    
        
from random import randint

def marker_choice():
    
    markers = ['X','O']
    marker = ''
    while marker not in markers:
        marker = input("Choose 'X' or 'O': ").upper()
        
        if marker not in markers:
            print('Sorry please enter X or O. ')
    
    x = randint(1,2)
    markers.remove(marker)
    if x==1:
        player1 = marker
        player2 = markers[0]
    else:
        player2 = marker
        player1 = markers[0]
    
    print('-'*15)
    print(f'| Player 1: {player1} |')
    print(f'| Player 2: {player2} |')
    print('-'*15)
    
    return player1,player2


def position_choice(positions, player_name):
    
    choice = 0
       
    while choice not in positions:      
        choice = input(f'{player_name}: Please choose your position (1-9): ')
        
        if choice.isdigit() == False:
            print('Please enter valid choice. ') 
            
        elif int(choice) not in range(1,10):
            print('Please choose valid position (1-9).')
        
        elif int(choice) in choice_list:
            print('Position taken! Please choose a different position.')
        
        else:
            choice_list.append(int(choice)) 
            positions.remove(int(choice))
            board[int(choice)] = player_name
            break
    
    return positions


def turn_choice(player1, player2):
    
    if turn%2 == 0:
        print('Player 2, its your turn now.')
        player_name = player2
    else:
        print('Player 1, its your turn now.')
        player_name = player1
        
    return player_name


def winner(player_name):
       
    for i in winning_patterns:
        win = 0
        for j in i:
            if board[j] == player_name:
                win += 1
                if win == 3:
                    print(f'Congratulations, player {player_name}. You have won the game!. ')
                    return win
                



gameon = True

while gameon:
    
    print('WELCOME TO TIC TAC TOE! ')
    
    board = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
    positions = [1,2,3,4,5,6,7,8,9]
    winning_patterns = [(1,2,3),(4,5,6),(7,8,9),(3,5,7),(1,5,9),(1,4,7),(2,5,8),(3,6,9)]
    choice_list = []
    turn = 1
    
    player1,player2 = marker_choice()
        
    while turn<10:
        
        display_board()
        player_name = turn_choice(player1,player2) 
        positions = position_choice(positions, player_name)
        turn+=1
        
        if turn in range(5,11):
            game_over = winner(player_name)
            if game_over == 3 :
                display_board()
                gameon = gameon_choice()
                break

            if turn == 10:
                display_board()
                print('DRAW MATCH.🤝🤝🤝')
                gameon = gameon_choice()
                break
            
        else:
            continue       