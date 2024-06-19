import random


def generate_number(difficulty):
    secret_number=random.randrange(1,difficulty+1)
    return secret_number

def get_guess_from_user(difficulty):

    user_input = input(f"Select a number between 1 and the {difficulty}:\n")
    try:
        user_input = int(user_input)
        return user_input
    except Exception:
        print("You didnt provide a number...")
        return '0'

def compare_results(secret_number,difficulty):
    user = get_guess_from_user(difficulty)
    while user == '0':
        user = get_guess_from_user(difficulty)

    if user == secret_number:

        return True
    else:

        return False

def play(difficulty):
    secret_number= generate_number(difficulty)

    return compare_results(secret_number, difficulty)




