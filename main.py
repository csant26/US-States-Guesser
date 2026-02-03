"""US States guesser"""

import turtle
import constants as cons

class USStatesGuesser:
    """US States Guesser class"""
    def __init__(self):
        self.initialize_screen()
        self.initialize_turtle()

    def initialize_screen(self):
        """Initialize screen"""
        self.screen = turtle.Screen()
        self.screen.title("US States Game")
        self.screen.addshape(cons.IMAGE_PATH)

    def initialize_turtle(self):
        """Initialize turtle"""
        self.my_turtle = turtle.Turtle()
        self.my_turtle.shape(cons.IMAGE_PATH)

    def run(self):
        """Runs the game"""
        self.screen.mainloop()

game = USStatesGuesser()
game.run()
