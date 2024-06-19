import random
import time
def generate_sequence(difficulty):
    list = [random.randrange(1,102) for i in range(difficulty)]
    return list

def get_list_from_user(difficulty):
    list = []
    for i in range(difficulty):
        user = input("Put your number!\n")
        while True:
            try:
                user = int(user)
                break
            except:
                user = input(("Make sure you put a number: "))

        list.append(user)
    return list

def is_list_equal(user, generated):
    if user == generated:
        return True
    else:
        return False

def play(difficulty):
    generated = generate_sequence(difficulty)
    print(str(generated))
    time.sleep(1.0)
    print("\n"*100)
    user = get_list_from_user(difficulty)
    if is_list_equal(user, generated) :

        return True
    else:

        return False

