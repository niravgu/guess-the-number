import numbers
import random
no = random.randint(1,10)
pname = input ("hi, what is your name?")
print ("hello",pname + " i am thinking of a number between 1 to 10. can you guess it?")
numberofguess = 0
while numberofguess < 4:
    guess = int(input("enter your guess"))
    numberofguess +=1
    if guess > no:
        print ("your number is higher than my number")
    elif guess < no :
        print("your number is lesser than my number")
    elif guess == no :
        break
    else:
        print("please enter a valid number")
if guess == no :
    print ("you guessed in ", str(numberofguess) + "tries.")
else :
    print("oops! you couldn't guess it. number is ", str(no))