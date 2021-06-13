import numpy as np
import os


def save_game(board,mode,difficulty):


    a_file = open("save_game.txt", "w")
    for row in board:
        np.savetxt(a_file,row)
         
       
    a_file.close()

    text = open("data.txt", "w") 
    #writing lines one by one
    
    text.write(mode)
    text.write(difficulty)
    #closing the file
    text.close()

def load_game():
    mode=''
    difficulty=''
    if os.stat("save_game.txt").st_size == 0:
         board=np.array([])
         mode='0'
         difficulty='e'
    else:

        board = np.loadtxt("save_game.txt").reshape(2, 8)
        board = board.astype(int)
        
        open('save_game.txt', 'w').close()

        fp = open("data.txt", "r")
        text= fp.readlines()
        mode=text[0][0]
        difficulty=text[0][1]
        fp.close()
        open("data.txt", "w").close()

    return board,mode,difficulty




#board = np.array([[3, 4, 4, 4, 4, 4, 4, 0],
#             [0, 4, 4, 5, 4, 4, 4, 5]])

#save_game(board)

#board = np.array([[0, 4, 4, 4, 4, 4, 4, 0],
#             [0, 4, 4, 5, 4, 4, 4,4]])

#board=load_game()
#print(board)