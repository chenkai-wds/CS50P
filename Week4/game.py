import random

while True:
    try:
        n = int(input("Level: "))
        if n <= 0:
            raise ValueError
    except ValueError:
        pass
    else:
        break

the_num = random.randint(1, n)
while True:
    try:
        guess_num = int(input("Guess: "))
        if guess_num <= 0:
            raise ValueError
    except ValueError:
        pass
    else:
        if guess_num < the_num:
            print("Too small!")
        elif guess_num > the_num:
            print("Too large!")
        else:
            print("Just right!")
            break