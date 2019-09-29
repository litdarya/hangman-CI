import argparse
from hangman import Game


def main():
    parser = argparse.ArgumentParser(description='hangman game')
    parser.add_argument('--dict', type=str, required=False, default='dict.txt',
                        help='path to dictionary, file with words')

    args = parser.parse_args()
    game = Game(words_path=args.dict)
    game.start_game()


if __name__ == '__main__':
    main()
