"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730439833"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
fortune_cookie: int = randint(1,4)
print("Your fortune cookie says...")
if fortune_cookie == 1:
    print("You will get an A on your next assignment")
else:
    if fortune_cookie == 2:
        print("You will be surprised tomorrow")
    else:
        if fortune_cookie == 3:
            print("Watch your back")
        else:
            if fortune_cookie == 4:
                print("Now is a good time to eat cake")

print("Now, go spread positive vibes!")