import random
import requests

import json
def convert_uds_to_ils(amount):
    with open('C:\\Users\\David\\Desktop\\DevOps\\config.json') as config_file:
        config = json.load(config_file)
        api_key = config['api_key']
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/USD/ILS/{amount}'

    try:
        response = requests.get(url)
        data = response.json()
        if data['result'] =='success':

            amount *= data['conversion_rate']
            return int(amount)
        else:
            return None
    except Exception as e:
        print(f"An error occured: {e}")
        return None


def get_money_interval(difficulty, total_val):

    total_val = convert_uds_to_ils(total_val)

    return total_val-(5-difficulty), total_val +(5-difficulty)

def get_guess_from_user():
    user = input("Enter your guess: ")
    while True:
        try:
            user = int(user)
            break
        except:
            user = input(("Make sure you put a number: "))

    return user

def play(difficulty):
    money = random.randrange(1,101)
    print("What do you think is the value of the", money, "from USD to ILS")
    low,up = get_money_interval(difficulty, money)
    ans = get_guess_from_user()

    if ans <= up and ans >= low:

        return True
    else:

        return False

