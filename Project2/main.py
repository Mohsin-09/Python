import random
import tkinter as tk
from tkinter import font as tkfont
from hangman_moves import HangmanMoves
from words import choose_word  # Ensure words.py is updated and available

class HangmanGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hangman Game")
        self.geometry("700x700")
        self.configure(bg="#e0f7fa")  # Light cyan background
        self.hangman = HangmanMoves()
        self.max_incorrect_guesses = 6
        self.categories = ['animals', 'fruits', 'countries', 'sports', 'vehicles', 'movies', 'music', 'literature', 'tv shows', 'celebrities',
                           'brands', 'foods', 'drinks', 'historical_figures', 'cities', 'planets', 'inventions', 'emotions', 'mythical_creatures', 'countries',
                           'landmarks', 'languages', 'plants', 'sea_creatures', 'countries', 'tools', 'weather', 'mammals', 'reptiles', 'technologies', 
                           'sports', 'modes of transport', 'famous_people']
        self.word = ''
        self.guessed_letters = set()
        self.incorrect_guesses = 0

        # Fonts
        self.title_font = tkfont.Font(family='Arial', size=24, weight='bold')
        self.label_font = tkfont.Font(family='Arial', size=16)
        self.entry_font = tkfont.Font(family='Arial', size=14)

        # Layout
        self.create_widgets()

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(self, text="Hangman Game", font=self.title_font, bg="#00796b", fg="white", padx=20, pady=20)
        self.title_label.pack(fill=tk.X)

        # Category Selection
        self.category_frame = tk.Frame(self, bg="#e0f7fa")
        self.category_frame.pack(pady=20)

        self.category_label = tk.Label(self.category_frame, text="Choose a category:", font=self.label_font, bg="#e0f7fa", fg="#004d40")
        self.category_label.pack(side=tk.LEFT, padx=10)

        self.category_var = tk.StringVar(value=self.categories[0])
        self.category_menu = tk.OptionMenu(self.category_frame, self.category_var, *self.categories)
        self.category_menu.config(font=self.label_font, width=30, bg="#ffffff", fg="#00796b", borderwidth=2, relief=tk.RAISED)
        self.category_menu.pack(side=tk.LEFT)

        self.start_button = tk.Button(self.category_frame, text="Start Game", command=self.start_game, font=self.label_font, bg="#004d40", fg="white", relief=tk.RAISED, padx=10, pady=5)
        self.start_button.pack(side=tk.LEFT, padx=10)

        # Hangman Stage
        self.hangman_frame = tk.Frame(self, bg="#e0f7fa")
        self.hangman_frame.pack(pady=20)

        self.hangman_label = tk.Label(self.hangman_frame, text=self.hangman.get_stage(0), font=("Courier", 16), bg="#e0f7fa", fg="#d32f2f")
        self.hangman_label.pack()

        # Word Display
        self.word_label = tk.Label(self, text="", font=("Courier", 28), bg="#e0f7fa", fg="#004d40")
        self.word_label.pack(pady=20)

        # Guess Entry
        self.guess_frame = tk.Frame(self, bg="#e0f7fa")
        self.guess_frame.pack(pady=10)

        self.guess_entry = tk.Entry(self.guess_frame, font=self.entry_font, width=12, borderwidth=2, relief=tk.SUNKEN)
        self.guess_entry.pack(side=tk.LEFT, padx=10)

        self.guess_button = tk.Button(self.guess_frame, text="Guess", command=self.make_guess, font=self.label_font, bg="#0288d1", fg="white", relief=tk.RAISED, padx=10, pady=5)
        self.guess_button.pack(side=tk.LEFT, padx=10)

        # Message Display
        self.message_label = tk.Label(self, text="", font=self.label_font, bg="#e0f7fa", fg="#d32f2f")
        self.message_label.pack(pady=20)

    def start_game(self):
        category = self.category_var.get()
        self.word = choose_word(category)
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.update_display()
        self.message_label.config(text="")

    def update_display(self):
        self.hangman_label.config(text=self.hangman.get_stage(self.incorrect_guesses))
        self.word_label.config(text=self.display_word())

    def display_word(self):
        display = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + ' '
            else:
                display += '_ '
        return display

    def make_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if not guess or len(guess) != 1:
            self.message_label.config(text="Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            self.message_label.config(text="You already guessed that letter.")
        elif guess in self.word:
            self.guessed_letters.add(guess)
            self.message_label.config(text=f"Good job! '{guess}' is in the word.")
        else:
            self.incorrect_guesses += 1
            self.message_label.config(text=f"Sorry, '{guess}' is not in the word. You have {self.max_incorrect_guesses - self.incorrect_guesses} guesses left.")

        if set(self.word) == self.guessed_letters:
            self.message_label.config(text=f"Congratulations! You guessed the word '{self.word}'!")
        elif self.incorrect_guesses >= self.max_incorrect_guesses:
            self.message_label.config(text=f"Game over! The word was '{self.word}'.")

        self.update_display()

if __name__ == "__main__":
    game = HangmanGame()
    game.mainloop()
