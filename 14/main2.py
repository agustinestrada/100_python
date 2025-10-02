import random
from game_data import data
from art import logo,vs

def format_data(account):
    """Takes the accoount data and retuns the printable format."""
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f'{account_name}, a {account_desc} from {account_country}'

def check_aswer(user_guess, a_followers, b_followers):
    """Take a user's guess and tell follower counts and return s if they got it right"""
    if a_followers > b_followers:
        return user_guess == 'A'
    elif a_followers == b_follower_count:
        print('Te la vamos a dejar pasar porque son lo mismo')
        return True
    else:
        return user_guess == 'B'

def validar_respuesta(guesss):
    if guesss == "A" or guesss == "B":
        return False
    else:
        return True

# Display Art.
print(logo)
juego = True
score = 0
account_b = random.choice(data)

# Make the game repeatable.
while juego:
    # Generate a random account form the game data.
    errores = 2
    account_a = account_b
    account_b = random.choice(data)

    print(format_data(account_a))
    print(vs)
    print(format_data(account_b))

    while account_a == account_b:
        account_b = random.choice(data)

    # Ask user for a guess.
    guess = input('Who has more followers? Type "A" or "B"').upper()

    while validar_respuesta(guess):
        errores -= 1
        guess = input('Who has more followers? Type "A" or "B"').upper()
        if errores == 0:
            print('Chau por pelotudo')
            exit()

    print('\n'*50)
    print(logo)

    # Check if user is correct.
    ## Get follower count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_aswer(guess,a_follower_count,b_follower_count)

    # Give user feedback on their guess.
    # Score Keeping.

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        juego = False

    # Making account at position B become the next account at position A.
#hola
