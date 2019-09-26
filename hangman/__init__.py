import os
import csv
import random
from sys import argv
import numpy as np


class Game:
    def __init__(self, words_path, tries=5):
        assert os.path.exists(words_path)
        self.words_path = words_path
        self.words = []
        self.play_word = None
        self.max_tries = tries

        self._read_words()

    def _read_words(self):
        with open(self.words_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter='\n')
            for row in reader:
                self.words.append(row[0].strip())

    def pick_random(self):
        return random.choice(self.words)

    def start_game(self):
        self.play_word = self.pick_random()
        word = np.array(list(self.play_word.strip()))
        guess_word = np.array(['*']*len(self.play_word))
        tries = 0
        tmp_word = ''

        while tries < self.max_tries:
            guess = input("Guess a letter:\n").strip()

            if guess in word:
                idx = np.where(word == guess)
                guess_word[idx] = guess
                print("Hit!\n")
            else:
                tries += 1
                print(f"Missed, mistake {tries} out of {self.max_tries}.\n")

            tmp_word = ''.join(guess_word)
            print(f"The word: {tmp_word}\n")
            if tmp_word == self.play_word:
                break

        if tmp_word == self.play_word:
            print("You won!")
            return True

        print("You lost!")
        return False


def main():
    assert len(argv) == 2
    game = Game(words_path=str(argv[1]))
    game.start_game()


if __name__ == '__main__':
    main()
