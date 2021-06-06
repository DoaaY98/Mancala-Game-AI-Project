import numpy as np

def initialize_board ():
    board = np.array([[0, 4, 4, 4, 4, 4, 4, 0],
             [0, 4, 4, 4, 4, 4, 4, 0]])
                #1, 2, 3,  4  ,5 ,6
    return board


def valid_move (board, move, player):
    #function to check whether the move is vaild or not, check the forbidden holes & check if the move is empty
    x,y = player, move
    if ((x == 0 and y == 0) or (x == 0 and y == 7) or (x == 1 and y == 0) or (x == 1 and y == 7)):
        return False
    if (board[x][y] == 0):
        return False
    if (move > 6):
        return False
    return True


def is_game_over (board):
    #function to check if the game whether over or not
    game_over = False
    sum = 0
    for half_board in board:
        for hole, i in zip(half_board, range(len(half_board))):
            if (i == 0 or i == 7):
                continue
            sum += hole 
        if (sum == 0):
            game_over = True
        else:
            game_over = False
    return game_over

def collect_reminder_stones():
    pass

def decide_winner(board):
    #function to decide the winner after check whether the game is over or not
    winner_player = "none"
    if (is_game_over()):
        collect_reminder_stones()
        if (board[0][0] >= board[1][7]):
            winner_player = "player1"
        else:
            winner_player = "player2"
    return winner_player
    

