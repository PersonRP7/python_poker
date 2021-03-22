import random
import argparse
import sys

# This is a type checker for the cmd line argparser.
# It throws an error if the provided argument is equal to, or less than 0.
def is_number_positive(number):
    number_integer = int(number)
    if number_integer <= 0:
        raise argparse.ArgumentTypeError(
            "We don't have any cards :|"
    )
    return number_integer

    
# You have the right to add a cmd line argument.
# Everything you press and type can and will be used against you.
# If you can't afford an argument, one will be appointed to you 
# by the ̶c̶o̶u̶r̶t̶
# the python interpreter.

parser = argparse.ArgumentParser()
parser.add_argument('-d', "--draw", 
                    default = random.randint(1, 11),
                    help = "How many cards does a person draw?",
                    type = is_number_positive
)

args = parser.parse_args()

# This type of hardcoding is extremely plebeian.
# A modern implementation should utilize a microservice
# architecture comprising mongodb and websockets
# because new card types are getting added all the time
# and it needs to be in real time.
# Mysql and Postgres both support JSON now but 
# they're not as cool because nobody named their
# rock band after them.
#https://www.youtube.com/watch?v=wvUQcnfwUUM

card_types = [
    "king", "queen", "spade",
    "two", "whatever"
]

# This offends the deterministic crowd.
def get_random_card():
    return random.choice(card_types)

# get leg
def get_hand(number):
    hand = [get_random_card() for i in range(number)]
    matches = [card for card in hand if card == card]
    for card in card_types:
        if matches.count(card) == 0:
            sys.stdout.write(f"You don't have any {card}.\n")
        else:
            sys.stdout.write(f"You have {matches.count(card)} {card}.\n")


# Something, something, something
# unit testing ...
if __name__ == "__main__":
    get_hand(args.draw)

