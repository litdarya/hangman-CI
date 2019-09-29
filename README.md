[![Build Status](https://travis-ci.org/litdarya/hangman-CI.svg?branch=master)](https://travis-ci.org/litdarya/hangman-CI)
[![codecov](https://codecov.io/gh/litdarya/hangman-CI/branch/master/graph/badge.svg)](https://codecov.io/gh/litdarya/hangman-CI)

# Hangman-CI
An implementation of a console hangman game
in educational purposes (to try CI, code
coverage and setuptools).

# Usage
You can use it either as a package or as console game.

## Playing as script
Default [dictionary](#dictionary):
```(bash)
python3 example.py
```
Your own [dictionary](#dictionary)
```(bash)
python3 example.py --dict dict.txt
```

## As a package
```(python)
from hangman import Game

game = Game(words_path='dict.txt')
game.start_game()
```

# Dictionary

Set of words (aka dictionary) is a text file
with words separated by newline.
Default is [dict.txt](dict.txt)
