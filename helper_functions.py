import numpy as np


##############################################
def initialize_board ():
    board = np.array([[0, 4, 4, 4, 4, 4, 4, 0],
             [0, 4, 4, 4, 4, 4, 4, 0]])
                #1, 2, 3,  4  ,5 ,6
    return board

###############################################


def valid_move(board, move, player):
    # function to check whether the move is valid or not, check the forbidden holes & check if the move is empty
    x, y = player, move
    if (x == 0 and y == 0) or (x == 0 and y == 7) or (x == 1 and y == 0) or (x == 1 and y == 7):
        return False
    if board[x][y] == 0:
        return False
    if move > 6:
        return False
    return True
#########################################################


def is_game_over(board):
    # function to check if the game whether over or not
    game_over = False
    sum = 0
    for half_board in board:
        for hole, i in zip(half_board, range(len(half_board))):
            if i == 0 or i == 7:
                continue
            sum += hole 
        if sum == 0:
            game_over = True
    return game_over
##########################################################


def collect_reminder_stones(board):
        sum = 0
        player = 0
        for half_board in board:
            for hole, i in zip(half_board, range(len(half_board))):
                if i == 0 or i == 7:
                    continue
                sum += hole
                board[player][i] = 0
            if sum == 0:
                player += 1
                continue
            else:
                if player == 0:
                    board[0][0] += sum
                else:
                    board[1][7] += sum
############################################################


def decide_winner(board):
    # function to decide the winner after collecting remainder stones
    winner_player = "none"
    collect_reminder_stones(board)
    if board[0][0] >= board[1][7]:
        winner_player = "player1"
    else:
        winner_player = "player2"
    return winner_player
####################################################


def player1_move(board, no_of_iterations, index):
    possible_moves = [board[0][6], board[0][5], board[0][4], board[0][3], board[0][2], board[0][1], board[0][0],
                      board[1][1], board[1][2], board[1][3], board[1][4], board[1][5], board[1][6]]
    # print(possible_moves)
    index = (6-index)+1
    while no_of_iterations:
        possible_moves[index] += 1
        index = (index+1) % 13
        no_of_iterations -= 1
    player1_list = possible_moves[0:7]
    # print(player1_list)
    player2_list = possible_moves[7:]
    # print(player2_list)
    # print(possible_moves)
    np.put(board[0], [6, 5, 4, 3, 2, 1, 0], player1_list)
    np.put(board[1], [1, 2, 3, 4, 5, 6], player2_list)
    index = index-1
    last_location = 0
    if index < 7:
        last_location = [6-index, 0]
    else:
        last_location = [index-6, 1]
    return last_location


def player2_move(board,no_of_iterations,index):

    possible_moves=[board[1][1],board[1][2],board[1][3],board[1][4],board[1][5],board[1][6],board[1][7],
                    board[0][6],board[0][5],board[0][4],board[0][3],board[0][2],board[0][1]]
    #print(possible_moves)
    # 1 2 3 4 5 6
    # 0 1 2 3 4 5
    
    while(no_of_iterations):
        possible_moves[index]+=1
        index=(index+1)%13
        no_of_iterations-=1
    player2_list=possible_moves[0:7]
    #print(player1_list)
    player1_list=possible_moves[7:]
    #print(player2_list)
    #print(possible_moves)
    np.put(board[0],[6,5,4,3,2,1],player1_list)
    np.put(board[1],[1,2,3,4,5,6,7],player2_list)
    index=index-1
    last_location=0
    if(index<7):
        last_location=[index+1,1]
    else:
        new_index=(index-7)
        last_location=[(6-new_index),0]
    return last_location
 

################################################
#################################################
#################################################
################################################

# play move is a function that returns last_location and next player
# last location is a list of two variables [current hole,player that the last hole is at]
# next_player is a variable that indicates the player that now has the turn (0 for player 1 and 1 for player2)
def play_move(board, hole, player):
    current_player = player
    next_player = (player+1) % 2
    last_location = []
    if not valid_move(board, hole, player):
        # if move is not valid
        print("move is not valid")
        return [], current_player
    else:
        # move is valid
        no_of_iterations = board[player][hole]
        board[player][hole] = 0  # empty this hole
        index = hole
        if player == 0:
            last_location = player1_move(board, no_of_iterations, index)
            if last_location[1] == 0 and last_location[0] == 0:
                # at pocket of player then play again
                next_player = current_player
        elif player == 1:
            last_location = player2_move(board, no_of_iterations, index)
            if last_location[1] == 1 and last_location[0] == 7:
                # at pocket of player then play again
                next_player = current_player
        
    return last_location, next_player

########################################################################


def current_score(board, hole, player):
    last_location, next_player = play_move(board, hole, player)
    if player == 0:
        if last_location[0] != 0 and last_location[1] != 0:
            board[0][0] += 1
        elif last_location[0] == 0 and last_location[1] == 0:
            board[0][0] += 1
        else:
            pass

    elif player == 1:
        if last_location[0] != 7 and last_location[1] != 1:
            board[1][7] += 1
        elif last_location[0] == 7 and last_location[1] == 1:
            board[1][7] += 1
        else:
            pass
    score_player0 = board[0][0]
    score_player1 = board[1][7]
    return score_player0, score_player1

#####################################################################

def stealing_mode(board, hole, player):
    last_location, next_player = play_move(board, hole, player)
    current_hole = last_location[0]
    current_player = last_location[1]

    if ((board[current_player][current_hole] == 1) & (player == current_player)):
        if player == 0:
            board[player][0] += board[player][current_hole] + board[1][current_hole]
            board[player][current_hole] = 0
            board[1][current_hole] = 0
            #return board[0][0]
        elif player == 1:
            board[player][7] += board[player][current_hole] + board[0][current_hole]
            board[player][current_hole] = 0
            board[0][current_hole] = 0
            #return board[1][7]


##########################################
def eval_board(board):
    pass

def get_valid_moves(board, maximizingPlayer=False):
    pass



def minimax(board, depth=3, alpha=-999, beta=+999, maximizingPlayer=False):
    if depth==0 or is_game_over(board):
        return eval_board(board)
    
    if maximizingPlayer:
        max_eval = -999
        moves = get_valid_moves(board, False)
        for index in moves:
            new_board = board.deepcopy()
            _,_ = play_move(new_board, index, False)
            my_eval = minimax(new_board, depth - 1, alpha, beta, False)
            max_eval = max(my_eval, max_eval)
            alpha = max(alpha, my_eval)
            if beta <= alpha:
                break

        return max_eval
    
    #Here the other oponent plays, so we get the moves of the next player
    else:
        min_eval = +999
        moves = get_valid_moves(board, True)
        for index in moves:
            new_board = board.deepcopy()
            _,_ = play_move(new_board, index, True)
            my_eval = minimax(new_board, depth - 1, alpha, beta, False)
            min_eval = min(my_eval, max_eval)
            beta = min(alpha, my_eval)
            if beta <= alpha:
                break
        
        return min_eval









