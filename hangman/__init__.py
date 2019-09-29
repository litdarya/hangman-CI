import os
import csv
import random
import sys
import numpy as np


class Game:
    """
    Hangman game class
    """

    def __init__(self, words_path=None, tries=5):
        self.words_path = words_path
        self.words = []
        self.play_word = None
        self.play_word_lst = None
        self.guess_word = None
        self.max_tries = tries
        # these members are needed for mocking in test
        self.input_stream = sys.stdin

        self._read_words()

    def _read_words(self):
        if self.words_path is None:
            return

        assert os.path.exists(self.words_path)

        with open(self.words_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter='\n')
            for row in reader:
                self.words.append(row[0].strip())

    def pick_random(self):
        self.play_word = random.choice(self.words)
        self.play_word_lst = np.array(list(self.play_word.strip()))
        self.guess_word = np.array(['*'] * len(self.play_word))

    def check_guess(self, guess):
        ans = True
        if guess in self.play_word_lst:
            idx = np.where(self.play_word_lst == guess)
            self.guess_word[idx] = guess
        else:
            ans = False

        tmp_word = ''.join(self.guess_word)
        return ans, tmp_word

    def start_game(self):
        self.pick_random()
        tries = 0
        curr_word = ''

        print("Guess a letter:\n")
        for line in self.input_stream:
            guess = line.strip()
            correct, curr_word = self.check_guess(guess)

            if correct:
                print("Hit!\n")
            else:
                tries += 1
                print(f"Missed, mistake {tries} out of {self.max_tries}.\n")

            print(f"The word: {curr_word}\n")
            if curr_word == self.play_word or tries >= self.max_tries:
                break
            print("Guess a letter:\n")

        if curr_word == self.play_word:
            print("You won!")
            return True

        print("You lost!")
        return False
