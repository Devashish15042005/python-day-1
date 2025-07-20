import random
secret_number = random.randint(1,10)
attempts = 0

while True: 
    guess = int(input("enter any number from 1 to 10"))
    attempts += 1
    if guess == secret_number:
        print(f"\U0001F389 Congratulations! correct you guessed it in {attempts}attempts.")
        break 
    elif guess < secret_number:
        print("too low")
    else: 
        print("too high")
                