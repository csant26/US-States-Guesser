"""US States guesser"""

import turtle
import pandas as pd
import tkinter.messagebox as msg
import constants as cons

class USStatesGuesser:
    """US States Guesser class"""
    def __init__(self):
        self.initialize_screen()
        self.initialize_turtle()
        self.load_states()
        self.game_on = True

    def initialize_screen(self):
        """Initialize screen"""
        self.screen = turtle.Screen()
        self.screen.title("US States Game")
        self.screen.setup(width=725,height=491)
        self.screen.addshape(cons.IMAGE_PATH)

    def initialize_turtle(self):
        """Initialize turtle"""
        self.my_turtle = turtle.Turtle()
        self.my_turtle.shape(cons.IMAGE_PATH)
        self.guess_turtle = turtle.Turtle()
        self.guess_turtle.penup()
        self.guess_turtle.hideturtle()

    def take_user_input(self):
        """Takes user guesses"""
        return self.screen.textinput("Guess State","Make your guess.")

    def load_states(self):
        """Loads the states csv"""
        self.states_df = pd.read_csv(cons.STATES_PATH)
        self.guessed_states = []

    def check_user_guess(self,user_guess):
        """Checks if user guess matches the state list"""
        matching_rows = self.states_df[self.states_df.state.str.lower()==user_guess]
        if not matching_rows.empty:
            print(matching_rows)
            matching_row = matching_rows.iloc[0]
            self.guess_turtle.goto(matching_row.x,matching_row.y)
            self.guess_turtle.write(matching_row.state,font=("Courier",10,"normal"))
            self.guessed_states.append(matching_row.state)
            self.screen.title(f"{len(self.guessed_states)}/{len(self.states_df)} states guessed.")
            print(f"Guessed states:{self.guessed_states}")
            if len(self.guessed_states) == 2:
                msg.showinfo("WON","Great job on getting all of them.")
                self.game_on = False
        else:
            self.screen.title("No match found.")


    def run(self):
        """Runs the game"""
        while self.game_on is True:
            self.check_user_guess(self.take_user_input())

        self.screen.mainloop()

game = USStatesGuesser()
game.run()
