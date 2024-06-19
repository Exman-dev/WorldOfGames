import CurrencyRoulleteGame
import GuessGame
import MemoryGame
import Score


def input_verify(text):
    user = input()
    while user not in text:
        print(f"Please select a number between {text[0]}-{text[len(text)-1]}")

        user = input()
    return int(user)

def welcome(name):
    return f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.'

def load_game():
    while True:
        print("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n""")

        game = input_verify("1230")

        if game == 0:
            "You quit the game"
            break
        print("""
Please select a difficulty between 1 to 5: """)
        print()
        user_diff = input_verify("12345")
        if game == 1:
            if MemoryGame.play(user_diff):
                Score.add_score(user_diff)
                print("You win !")
            else:
                print("You lost! ")
        elif game == 2:
            if GuessGame.play(user_diff):
                Score.add_score(user_diff)
                print("You win !")
            else:
                print("You lost! ")
        elif game == 3:
            if CurrencyRoulleteGame.play(user_diff):
                Score.add_score(user_diff)
                print("You win !")
            else:
                print("You lost! ")










