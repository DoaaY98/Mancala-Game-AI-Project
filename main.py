import helper_functions as fn

board = fn.initialize_board()
board[0] = [25,0,0,0,0,0,0,0]
board[1] = [0,2,2,2,2,2,2,4]

#print(play_move(board,0,0))


##last_location , next_player=play_move(board,0,0)


while(not fn.is_game_over(board)):
    #el3aaab

    
    #print(play_move(board,0,0))

    pass

if(fn.is_game_over(board)):
    print(fn.decide_winner(board))
