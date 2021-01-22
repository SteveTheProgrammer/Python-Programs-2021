# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 19:19:02 2021

@author: stefanos
"""


def clear_board():
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    return board

def display(board):
    print()
    for x in range(3,0,-1):
        print( ' ', board[x*3-3], '│', board[x*3-2], '│' , board[x*3-1])
        if x >= 2: 
            print('────┼───┼────')

def user_choice():
    choice = input('Please give a number between 1-9: ')
    while choice.isdigit() == False or int(choice) < 1 or int(choice) >9:
        choice = input('This is an invalid choice! Please give a number between 1-9: ') 
    return int(choice)

def board_replacement(choice, board, turn):
    if board[choice-1] == ' ':
        if turn:
            board[choice-1] = 'X'
        else:
            board[choice-1] = 'O'
    return board

def win(board, turn):
    win = False
    if (board[0] == board[1] and board[1] == board[2] and board[0] != ' ' or 
        board[3] == board[4] and board[4] == board[5] and board[3] != ' ' or 
        board[6] == board[7] and board[7] == board[8] and board[6] != ' ' or
        board[0] == board[3] and board[3] == board[6] and board[0] != ' ' or
        board[1] == board[4] and board[4] == board[7] and board[1] != ' ' or
        board[2] == board[5] and board[5] == board[8] and board[2] != ' ' or
        board[0] == board[4] and board[4] == board[8] and board[0] != ' ' or
        board[2] == board[4] and board[4] == board[6] and board[2] != ' ' ):
           win = True
    return win
               
def empty_slot(board, choice):
    return board[choice-1] == ' '

#____________________________________MAIN_____________________________________
x_wins = 0
o_wins = 0
user_desire = 'Y'
while user_desire == 'Y' or user_desire == 'y':
    board = clear_board()
    moves = 0
    game_on = True
    turn = True
    while moves < 9 and game_on:
        display(board)
        choice = user_choice()
        if empty_slot(board, choice):
            board_replacement(choice, board, turn)
            turn = not turn
            moves += 1
            if win(board, turn) == True:
                display(board)
                game_on = False
                print()
                if turn == False:
                    print('X won the game!')
                    x_wins += 1
                else:
                    print('O won the game!')
                    o_wins += 1
        else:       
           print()
           print("This slot is not available! Please choose another one!")
    if moves == 9:
        display(board)
        print()
        print('Draw!')
    user_desire = input('Do you want to play again? Type Y/y or N/n: ')
    while user_desire != 'Y' and user_desire != 'y' and user_desire != 'n' and user_desire != 'N':
            user_desire = input('That is not a valid option! Type Y/y or N/n: ')

#RESULTS

print(f'X has won {x_wins} times')
print(f'O has won {o_wins} times')