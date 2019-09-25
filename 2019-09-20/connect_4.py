#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:56:14 2019

@author: zhangletian
"""



def initilise_board():
    global board
    global blank
    blank='M'
    board=[[blank]*7 for i in range(6)]
    
def set_up_game():
    global this_player
    this_player='O'
    global game_finished
    game_finished=False

def output_board():
    for i in range(5,-1,-1):
        for j in range(7):
            print(board[i][j],end=' ')
        print('\n')
        
def this_player_makes_move():
    global valid_column, valid_row, board
    valid_column=this_player_chooses_column()
    valid_row=find_next_free_position_in_column()
    board[valid_row][valid_column]=this_player

def this_player_chooses_column():
    print("Player {} \'s turn".format(this_player))
    while 1:
        column_number=int(input('Enter a valid column number: '))
        if column_number_valid(column_number) == True:
            break
    return column_number

def column_number_valid(column_number):
    valid=False
    if 0<= column_number and column_number<=6:
        valid=True
    return valid

def find_next_free_position_in_column():
    global valid_column
    this_row=0
    while board[this_row][valid_column] != blank:
        this_row+=1
    return this_row

def check_if_this_player_has_won():
    global game_finished, winner_found
    winner_found=False
    chliv()
    if winner_found==False:
        cvlvc()
    elif winner_found==True:
        game_finished=True
        print(this_player+'is the winner')
    else:
        check_for_full_board()

def chliv():
    global valid_row
    global winner_found
    for i in range(4):
        if board[valid_row][i] == this_player and board[valid_row][i+1] == this_player and board[valid_row][i+2] == this_player and board[valid_row][i+3] == this_player:
            winner_found=True
def cvlvc():
    global winner_found
    global valid_row
    if valid_row ==3 or valid_row==4 or valid_row==5:
        if board[valid_row][valid_column]==this_player and board[valid_row-1][valid_column]==this_player and board[valid_row-2][valid_column]==this_player and board[valid_row-3][valid_column]==this_player:
            winner_found=True

def check_for_full_board():
    global game_finished
    blank_found=False
    this_row=0
    while 1:
        this_column=0
        this_row+=1
        while 1:
            this_column+=1
            if board[this_row][this_column]==blank:
                blank_found==True
            if this_column==6 or blank_found==True:
                break
        if this_row == 5 or blank_found==True:
            break
        if blank_found==False:
            print('draw')
            game_finished=True

def swap_this_player():
    global this_player
    if this_player == 'O':
        this_player='X'
    else:
        this_player='O'
    


initilise_board()
set_up_game()
output_board()
while game_finished==False:
    this_player_makes_move()
    output_board()
    check_if_this_player_has_won()
    if game_finished==False:
        swap_this_player()
