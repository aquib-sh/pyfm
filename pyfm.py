import sys
import re
import os
import threading
import config

if sys.platform == "win32":
    import msvcrt
elif sys.platform in ['linux', 'darwin']:
    import getch


class Pyfm:
    
    def __init__(self):
        self.title = (config.title_fg 
                    + config.title_bg
                    + "Pyfm File Manager")
        self.focus = 0

    def print_curr_files(self):
        """ Prints the current files,
            puts the cursor or color object towards focus
            while printing """
        print(self.title)
        if self.focus < 0:
            self.focus = 0

        curr_content = ["../"] + os.listdir()
        for i in range(0, len(curr_content)):
            # put fg, bg color on focus element 
            if i == self.focus:
                print(config.fg
                    + config.bg
                    + curr_content[i])
            else:
                print(config.reset_fg
                    + config.reset_bg
                    + curr_content[i])
    
    @staticmethod
    def clear_screen():
        """ Clears the console screen. """
        unix = ['linux','cygwin', 'darwin']

        if sys.platform == "win32":
            os.system("cls")
        elif sys.platform in unix:
            os.system("ls")

    def get_curr_files(self):
        """ Returns current files list. """
        return ["../"] + os.listdir()
    
    def key_action(self, key_):
        """ Takes action depending upon the keys passes """
        if key_ not in config.key_bindings:
            return 

        if config.key_bindings[key_] == "MOVE DOWN":
            self.focus += 1
            self.print_curr_files()
        elif config.key_bindings[key_] == "MOVE UP":
            self.focus -= 1
            self.print_curr_files()
        elif config.key_bindings[key_] == "QUIT":
            sys.exit()

class TempHolder:
    def __init__(self):
        self.char_value = ""
            

if __name__ == "__main__":

    fm = Pyfm()
    temp= TempHolder()
    
    def get_char():
        while True:
            if sys.platform == "win32":
                _char = msvcrt.getch 
            elif sys.platform in ['linux', 'darwin']:
                _char = getch.getch
            temp.char_value = _char.decode()
            print("focus on ", temp.char_value)

    def start_app():
        while True:
            Pyfm.clear_screen() 
            fm.key_action(temp.char_value)
            fm.print_curr_files()

    Pyfm.clear_screen() 
    t = threading.Thread(target=get_char)
    t.start()

    t1 = threading.Thread(target=start_app)
    t1.start()

       
        

