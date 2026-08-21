import random

attempt = 5
number = random.randint(1, 20)
print(f"I picked a number from 1 to 20. You have {attempt} attempts.")

while attempt > 0:
    guess = input(f"Attempt {6 - attempt}: Input the number: ")
    if not guess.isdigit():  # little check
        print("Input the digit!")
        continue

    guess = int(guess)

    if guess not in range(1, 21):  # little check
        print("I picked a number from 1 to 20")
        continue

    attempt -= 1

    if guess == number:
        print("You are right! great job")
        break
    elif guess > number:
        print(f"Too much! Attempts left: {attempt}")
    else:
        print(f"Too little! Attempts left: {attempt}")

else:
    print(f"Attempts are over! Picked number was: {number}")
