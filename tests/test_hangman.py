from hangman import Game


def test_test():
    game = Game(words_path='dict.txt')
    assert game is not None
