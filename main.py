import helper_functions as fn
import numpy as np
import save_load as sv

# import minimax as minimax
board = fn.initialize_board()
# board[1] = [15,0,6,0,0,0,14,0]
# board[0] = [0,0,0,0,0,0,0,12]
# fn.print_board(board)
if __name__ == "__main__":

    board_loaded = sv.load_game()
    saved = 0
    difficulty_level = ""

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

    board = np.array([])
    if board_loaded.size == 0:
        board = fn.initialize_board()
        print("-------------------******----------------------")
        print("-------------------******----------------------")
        print("||                 NEW GAME STARTING....             ||")
        print("-------------------******----------------------")
        print("-------------------******----------------------")
        starting = input("Do You Like to Start? \n if Yes Press Y  \n if You want the COMPUTER to start Press any other key.... \n")

        if(starting=='Y' or starting== 'y'):
            player ='1'
        else :
            player='0'

        difficulty_level = input(
        "CHOOSE Difficulty Level :  \n For Easy Mode Press E  \n For Medium Mode Press M \n For Hard Mode Press H \n")

        stealing_mode= input("Would You like to enter STEALING MODE? \n if Yes Press Y  \n if NO then press any other key.... \n")

        if(stealing_mode=='Y' or stealing_mode== 'y'):
            mode='0'
        else:
            mode='1'

    else:
        starting = input("Would you like to LOAD Last game? \n if Yes Press 'Y'  \n if You want to start a NEW GAME  Press any other key.... \n")

        if(starting=='Y' or starting== 'y'):
            #loading last game
            board=board_loaded
            player ='1'
            print("-------------------******----------------------")
            print("-------------------******----------------------")
            print("||                LOADING LAST GAME....             ||")
            print("-------------------******----------------------")
            print("-------------------******----------------------")
            stealing_mode= input("Would You like to enter STEALING MODE? \n if Yes Press Y  \n if NO then press any other key.... \n")


            if(stealing_mode=='Y' or stealing_mode== 'y'):
                mode='0'
            else:
                mode='1'


        else:
            
            board = fn.initialize_board()
            print("-------------------******----------------------")
            print("-------------------******----------------------")
            print("||                 NEW GAME STARTING....             ||")
            print("-------------------******----------------------")
            print("-------------------******----------------------")
            starting = input("Do You Like to Start? \n if Yes Press Y  \n if You want the COMPUTER to start Press any other key.... \n")

            if(starting=='Y' or starting== 'y'):
                player ='1'
            else :
                player='0'

            difficulty_level = input(
        "CHOOSE Difficulty Level :  \n For Easy Mode Press E  \n For Medium Mode Press M \n For Hard Mode Press H \n")
            stealing_mode= input("Would You like to enter STEALING MODE? \n if Yes Press Y  \n if NO then press any other key.... \n")

            if(stealing_mode=='Y' or stealing_mode== 'y'):
                mode='0'
            else:
                mode='1'


    print("Game Started.................")
    if (mode == '0'):
        print("STEALING MODE IS ON ....")
    else:
        print("STEALING MODE IS OFF ...")

    fn.print_board(board)
    print("\n")
    next_player = 0
    if difficulty_level == "E" or difficulty_level == "e":
        depth = 2
    elif difficulty_level == "M" or difficulty_level == "m":
        depth = 5
    elif difficulty_level == "H" or difficulty_level == "h":
        depth = 10
    else:
        depth = 10
    while not fn.is_game_over(board):
        if player == "0":  # ai to start
            print("The Computer is Playing Now .............")
            print("-----------------------------------------")
            print("\n")

            player = 0
            val, best_move = fn.minimax(board, depth=depth,  maximizingPlayer=1, mode=bool(mode))
            last_location, next_player = fn.play_move(board, best_move, int(player))
            if mode == '0':
                fn.stealing_mode(board, best_move, int(player), last_location)
        elif player == "1":  # player to start
            player = 1
            your_turn = input("YOUR TURN \n Choose move between 1 --> 6 :\n")
            valid_moves = fn.get_valid_moves(board, int(player))

            if your_turn=='quit' or your_turn=='QUIT' or your_turn=='Quit':

                print("-------------------******----------------------")
                print("-------------------******----------------------")
                print("||                SAVING GAME             ||")
                print("-------------------******----------------------")
                print("-------------------******----------------------")
                sv.save_game(board)
                print("-------------------******----------------------")
                print("-------------------******----------------------")
                print("||                GOODBYE                  ||")
                print("-------------------******----------------------")
                print("-------------------******----------------------")
                saved=1
                break

            else: 
                move = int(your_turn)
                if move in valid_moves:
                    last_location, next_player = fn.play_move(board, move, int(player))
                    if mode == '0':
                        fn.stealing_mode(board, move, int(player), last_location)
                else:
                    print("inValid Move xxxx")
                    print("Please choose a valid move ........")
                    # print("-----------------------------------------")
                    print("\n")
                    next_player = str(player)
        fn.print_board(board)
        print("\n")
        player = str(next_player)

if saved == 1:
    saved = 0


elif fn.is_game_over(board):
    print(fn.decide_winner(board))
    fn.print_board(board)