import random
min = int
max = int
random_number = int
diff = int
min = 1
max = 50
random_number = random.choice(range(min, max))
def validate_input(guess):
    if type(guess) == int:
        return 1
    else:
        return 0
def difference(guess):
    diff = int(random_number) - int(guess)
    return diff
def comparison(diff):
    if int(diff) == 0:
        return ("Your guess is right !!!")
    elif int(diff) < 0:
        return ("Your guess is too high...")
    else:
        return ("Your guess is too low...")
