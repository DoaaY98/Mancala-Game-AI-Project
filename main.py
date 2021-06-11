import helper_functions as fn
import time
global start_time
#import minimax as minimax
board = fn.initialize_board()
#board[1] = [15,0,6,0,0,0,14,0]
#board[0] = [0,0,0,0,0,0,0,12]
#fn.print_board(board)
if __name__ == "__main__":

    print("-------------------**************----------------------")
    print("||               Welcome to Mancala Game             ||")
    print("-------------------**************----------------------")
    print("     This game was developed by our Amazing Team ")
    print("-------------------**************----------------------")
    print("     We hope you enjoy it")
   
    print("||               WE CHALLENGE YOU TO WIN             ||")
    print("-------------------**************----------------------")
    print("||               GOOD LUCK FROM OUR TEAM MEMBERS:      ")
    print("|| Dalia  ||")
    print("|| Doaa   ||")
    print("|| Dina   ||")
    print("|| Sara   ||")
    print("|| Zeinab ||")
    print("-------------------**************----------------------")
    print("-------------------**************----------------------")
    print("||                 LET'S START                       ||")

    
    starting = input("Do You Like to Start? \n if Yes Press Y  \n if You want the COMPUTER to start Press any other key.... \n")
    player='0'
    if(starting=='Y' or starting== 'y'):
        player ='1'
    else :
        player='0'

    
    stealing_mode= input("Would You like to enter STEALING MODE? \n if Yes Press Y  \n if NO then press any other key.... \n")

    mode ='0'
    if(stealing_mode=='Y' or stealing_mode== 'y'):
        mode='0'
    else:
        mode='1'


    print("Game Started.................")
    if(mode=='0'):
        print("STEALING MODE IS ON ....")
    else:
        print("STEALING MODE IS OFF ...")
    
    fn.print_board(board)
    print("\n")
    next_player = 0
    while not fn.is_game_over(board):
        if player == "0":  # ai to start
            print("The Computer is Playing Now .............")
            print("-----------------------------------------")
            print("\n")
            print("Timer has start")
            start_time=time.time()
            def get_time():
                elapsed_time=time.time()-start_time
                return elapsed_time
            player = 0
            val, best_move = fn.minimax(board, maximizingPlayer=1, mode=bool(mode))
            last_location, next_player = fn.play_move(board, best_move, int(player))
            if mode=='0':
                fn.stealing_mode(board, best_move, int(player),last_location)
            elapsed_time=time.time()-start_time
            print("Elapsed time: " + str(elapsed_time))
        elif player == "1":  #  player to start
            player = 1
            move = int(input("YOUR TURN \n Choose move between 1 --> 6 :\n"))
            valid_moves = fn.get_valid_moves(board, int(player))
            if move in valid_moves:
                last_location, next_player = fn.play_move(board, move, int(player))
                if mode=='0':
                    fn.stealing_mode(board, move, int(player),last_location)
            else:
                print("inValid Move xxxx")
                print("Please choose a valid move ........")
                #print("-----------------------------------------")
                print("\n")
                next_player = str(player)
        fn.print_board(board)
        print("\n")
        player = str(next_player)
if fn.is_game_over(board):
        print(fn.decide_winner(board))
        fn.print_board(board)


