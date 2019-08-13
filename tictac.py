# ----------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
# Author:   Vishaal Yalamanchali
# ----------------------------------------------------------------------
"""
Module to implement a generic game of tic tac toe
"""
import tkinter
import random

class Game(object):
    """
    GUI Game class that supports a 3x3 game of tic tac toe

    Argument:
    parent (Tkinter.tk) the root window object

    Attributes:
    parent (tkinter.Tk) the root window object
    canvas (tkinter.Canvas) canvas root objecct
    BOARD (dictonary) holds board and position
    BOARD_SIZE (int) has default board size
    WINS (list) list of possible board positions to win
    GAME_STATUS (int) 0 for tie, 1 for user win, 2 for loss
    """

    BOARD = {row + 1: 0 for row in range(9)}
    WINS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]]
    GAME_STATUS = 0
    BOARD_SIZE = 100
    # Board
    # 1 : 0 | 2 : 0 | 3 : 0
    # ---------------------
    # 4 : 0 | 5 : 0 | 6 : 0
    # ---------------------
    # 7 : 0 | 8 : 0 | 9 : 0

    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        # Create the restart button widget
        button_frame = tkinter.Frame(parent)
        button_frame.grid()

        restart_button = tkinter.Button(button_frame, text="RESTART",
                                        command=self.restart)
        restart_button.grid()
        self.canvas = tkinter.Canvas(parent, width=300, height=300)
        self.canvas.grid()
        # Create a canvas widget
        for row in range(3):
            for column in range(3):
                self.canvas.create_rectangle(self.BOARD_SIZE * column,
                                             self.BOARD_SIZE* row,
                                             self.BOARD_SIZE * (column + 1),
                                             self.BOARD_SIZE* (row + 1),
                                             fill="white")
        # Create a label widget for the win/lose message
        self.result_label = tkinter.Label(parent, text=" ")
        self.result_label.grid()

        # Create any additional instance variable you need for the game
        self.canvas.bind("<Button-1>", self.play)
        # take out the pass statement and enter your code

    def restart(self):
        """
        Restarts the current program and clears board/dictionary
        Parameters:
            None
        return: None
        """
        for shape in self.canvas.find_all():
            self.canvas.itemconfigure(shape, fill='white')
        self.result_label.configure(text=" ")

        self.BOARD.clear()
        self.BOARD = {row + 1: 0 for row in range(9)}
        self.GAME_STATUS = 0

    def play(self, event):
        """
        Restarts the current program.
        Parameters:
            event (object) holds the coordinates of user clicks
        return: None
        """
        if self.GAME_STATUS == 0:
            shape = self.canvas.find_closest(event.x, event.y)
            if self.BOARD[shape[0]] == 0:
                self.BOARD[shape[0]] = 1
                self.winnner_check()
                self.canvas.itemconfigure(shape, fill='pink')
                if self.board_not_full():
                    a = random.choice(tuple({tile for tile in self.BOARD if
                                             self.BOARD[tile] == 0}))
                    self.BOARD[a] = -1
                    self.winnner_check()
                    if self.GAME_STATUS != 2:
                        self.canvas.itemconfigure((a,), fill='cyan')
            if 0 not in self.BOARD.values() and self.GAME_STATUS == 0:
                self.GAME_STATUS = 1
                self.result_label.configure(text="It's a Tie!")

    def board_not_full(self):
        """
        Checks status of board every iteration of play
        Parameters:
            None
        return:
        True (boolean) if board has empty tiles
        False (boolean) if not
        """
        for tiles in self.BOARD:
            if self.BOARD[tiles] == 0:
                return True
        return False

    def winnner_check(self):
        """
        Checks to see who won every iteration of play
        Parameters:
            None
        return:
            sets new game status and returns without checking other if
            None
        """
        j = 0
        for i in range(8):
            if self.BOARD[self.WINS[i-1][j]] == \
                    self.BOARD[self.WINS[i-1][j+1]] == \
                    self.BOARD[self.WINS[i-1][j+2]]:
                if self.BOARD[self.WINS[i-1][j+1]] == 1:
                    self.result_label.configure(text="You Win!")
                    self.GAME_STATUS = 2
                    return
                if self.BOARD[self.WINS[i-1][j+1]] == -1:
                    self.result_label.configure(text="You Lose!")
                    self.GAME_STATUS = 1
                    return
        # This method is invoked when the user clicks on a square.
        # take out the pass statement and enter your code
        
def main():
    root = tkinter.Tk()
    my_app = Game(root)
    root.mainloop()

    # Instantiate a root window
    # Instantiate a Game object
    # Enter the main event loop
    # take out the pass statement and enter your code


if __name__ == '__main__':
    main()