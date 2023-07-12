#NUMBER GUESSING GAME
import random
# Taking Inputs
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

x = random.randint(lower, upper)

# Initializing the number of guesses.
count = 0
while count < 8:
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")
    
	print(f"you left {8-count} of guess")

if count >= 8:
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")
