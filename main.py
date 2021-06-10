import helper_functions as fn
#import minimax as minimax
board = fn.initialize_board()
#board[0] = [25,0,0,0,0,0,0,0]
#board[1] = [0,2,0,2,0,2,2,4]
if __name__ == "__main__":
    player = input("Choose player to start: \n for you to start enter 1 \n"
                       " for computer to start enter 0\n")
    mode = input("Choose mode to start: \n stealing mode enter 0 \n for non stealing mode enter 1 \n")
    print("Game Started")
    print(board)
    next_player = 0
    while not fn.is_game_over(board):
        if player == "0":  # ai to start
            print("enter ai ")
            player = 0
            val, best_move = fn.minimax(board, maximizingPlayer=1, mode=bool(mode))
            last_location, next_player = fn.play_move(board, best_move, int(player))
            if not bool(mode):
                fn.stealing_mode(board, best_move, int(player))
        elif player == "1":  #  player to start
            player = 1
            move = int(input("Choose move between 1 --> 6 :\n"))
            valid_moves = fn.get_valid_moves(board, int(player))
            if move in valid_moves:
                last_location, next_player = fn.play_move(board, move, int(player))
                if not bool(mode):
                    fn.stealing_mode(board, move, int(player))
            else:
                print("please choose a valid move")
                next_player = str(player)
        print(board)
        player = str(next_player)
    if fn.is_game_over(board):
        if fn.decide_winner(board) == "player1":
            print(board)
            print("YOU LOST")
        else:
            print("YOU WON")



#print(play_move(board,0,0))

#print(fn.get_valid_moves(board,False))
##last_location , next_player=play_move(board,0,0)


#while(not fn.is_game_over(board)):
    #el3aaab

    
    #print(play_move(board,0,0))

 #  pass

# if(fn.is_game_over(board)):
#     print(fn.decide_winner(board))
