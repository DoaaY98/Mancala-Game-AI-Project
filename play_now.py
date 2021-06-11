import keyboard
class PlayNow():
    def __init__(self, play_now=0):
        self.play_now = play_now
    
    def keyPressed(self):
        while True:
            if keyboard.is_pressed('p'):  # if key 'q' is pressed 
                self.play_now = 1
                break  # finishing the loop
    
    def set_playNow(self):
        self.play_now = 0

    def check_playNow(self):
        return self.play_now