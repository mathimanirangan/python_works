import random
import sys
from idlelib.macosx import fixb2context

import pyjokes

low = int(sys.argv[1])
high = int(sys.argv[2])

rand = random.randint(low,high)

input("system has guessed a number")

while True:
    guess=int(input(f"type your guess between {low} and {high}: "))
    if rand == guess:
        print(f"your guess of {guess} is correct")
        print(pyjokes.get_joke('en','neutral'))
        break
    else:
        print(f"your guess {guess} didnt match with {rand}, lets try one more time")

