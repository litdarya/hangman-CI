from hangman import Game


def test_two_letters():
    """
    Checks if a guess is correct and there are more
    than one guessed letter in a word, it changes all
    """
    game = Game()
    game.words = ['kitty']
    game.pick_random()
    guess = 't'
    _, word = game.check_guess(guess)
    assert word == '**tt*'


def test_bad_guess():
    """
    Checks if a guess is incorrect
    """
    game = Game()
    game.words = ['game']
    game.pick_random()
    guess = 'q'
    check, word = game.check_guess(guess)
    assert not check
    assert word == '****'


def test_win():
    """
    Checks win scenario
    """
    game = Game()
    game.words = ['game']
    game.pick_random()
    game.input_stream = [
        'a',
        'g',
        'm',
        'e',
    ]
    check = game.start_game()
    assert check
    assert ''.join(game.guess_word) == 'game'


def test_fail():
    """
    Checks lose scenario
    """
    game = Game()
    game.words = ['game']
    game.pick_random()
    game.input_stream = [
        'a',
        'g',
        'm',
        'b',
        'c',
        'd',
        'f',
        'i',
    ]
    check = game.start_game()
    assert not check
    assert ''.join(game.guess_word) == 'gam*'
