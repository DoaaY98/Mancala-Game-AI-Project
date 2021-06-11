import numpy as np
import os


def save_game(board):


    a_file = open("save_game.txt", "w")
    for row in board:
        np.savetxt(a_file,row)
         

    a_file.close()


def load_game():
    if os.stat("save_game.txt").st_size == 0:
         board=np.array([])
    else:

        board = np.loadtxt("save_game.txt").reshape(2, 8)
        board = board.astype(int)
        open('save_game.txt', 'w').close()
    return board




#board = np.array([[3, 4, 4, 4, 4, 4, 4, 0],
#             [0, 4, 4, 5, 4, 4, 4, 5]])

#save_game(board)

#board = np.array([[0, 4, 4, 4, 4, 4, 4, 0],
#             [0, 4, 4, 5, 4, 4, 4,4]])

#board=load_game()
#print(board)