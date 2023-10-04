# It is simple riddle game
# You have to answer the questions correctly
# There will be score out of 10
# It will generate your result in the end according to your performance.
# For Every correct you will get 1 score and for every wrong answer 1 will deducted from your score
# PLEASE : Type your answer carefully, answer box is spelling sensitive.
# Enjoy :)
import time

print("welcome to the game!!! Buddy")


Name = input("what is your name? ")

age = input("what is your age? ")

age = int(age)

if age >= 12:
    print('oh let me check if you can play the game or not............. ')
    time.sleep(4)
    print("Congratulation! " + Name + " \nYou can play the game")
else:
    print("sorry you cannot play the game! Grow up you toddler")
    quit()

time.sleep(3)

consent = input("Do you want to play the game? (yes/no)")

consent = str(consent)

if consent == "yes":
    print("Okay cool you can play !!! let's start")
elif consent == "no":
    print("it's okay if you don't wanna play ping me anytime to play ! Have a wonderful day")
    quit()
else:
    print("Answer only in yes and no format")

# keeping the note of score

Score = 0


# prompting user for 1st Question

choice_1 = input(
    " What month of the year has 28 days?\n1) February\n2) December\n3) All of them\nChoose one of the above answer\n ")

# using the if loop to determine the right answer.

if choice_1 == "All of them":
    print("wow you got the right answer")
    Score = Score + 1

else:
    print("Now that is a wrong answer " + "The correct answer is 'All of them'")
    Score = Score - 1
print("You score is", Score)

# Keeping 1 seconds gap between question

time.sleep(1)

# 2nd question

choice_2 = input(
    " What is always in front of you but can’t be seen?\n1) Car\n2) Future\n3) Eyes\nChoose one of the above answer\n ")

if choice_2 == "Future":
    print("wow you got the right answer")
    Score = Score + 1

else:
    print("Now that is a wrong answer " + "The correct answer is 'Future'")
    Score = Score - 1
print("You score is", Score)

time.sleep(1)

# 3rd question

choice_3 = input(
    "A man who was outside in the rain without an umbrella or hat did not get a single hair on his head wet. Why?\n"
    "1) He was bald\n2) I don't know\n3) Waterproof man\n"
    "Choose one of the above answer\n ")

if choice_3 == "He was bald":
    print("wow you got the right answer")
    Score = Score + 1

else:
    print("Now that is a wrong answer " + "The correct answer is 'He was bald'")
    Score = Score - 1
print("You score is", Score)

time.sleep(1)

# 4th question
choice_4 = input(
    " What has hands, but can’t clap?\n1) A clock\n2) I don't know\n3) sculpture\nChoose one of the above answer\n ")

if choice_4 == "A clock":
    print("wow you got the right answer")
    Score = Score + 1

else:
    print("Now that is a wrong answer " + "The correct answer is 'A clock'")
    Score = Score - 1
print("You score is", Score)

time.sleep(1)

# prompting for 5th question
choice_5 = input(
    " What runs all around a backyard, yet never moves?\n"
    "1) Grass\n2) A fence\n3) water\nChoose one of the above answer\n ")

if choice_5 == "A fence":
    print("wow you got the right answer")
    Score = Score + 1

else:
    print("Now that is a wrong answer " + "The correct answer is 'A fence'")
    Score = Score - 1
print("You score is", Score)

time.sleep(1)

# prompting for the 6th question
choice_6 = input(
    "What has a head and a tail but no body?\n"
    "1) A coin\n2) circle\n3) I don't know\nChoose one of the above answer\n ")

if choice_6 == "A coin":
    print("wow you got the right answer")
    Score = Score + 1

else:
    print("Now that is a wrong answer " + "The correct answer is 'A coin'")
    Score = Score - 1
print("You score is", Score)

time.sleep(1)

# prompting for 7th question

choice_7 = input(
    "What is so fragile that saying its name breaks it?\n"
    "1) Silence\n2) Mirror\n3) I don't know\nChoose one of the above answer\n ")

if choice_7 == "Silence":
    print("wow you got the right answer")
    Score = Score + 1

else:
    print("Now that is a wrong answer " + "The correct answer is 'Silence'")
    Score = Score - 1
print("You score is", Score)

time.sleep(1)

# prompting for 8th question
choice_8 = input(
    "What can fill a room but takes up no space?\n"
    "1) Light\n2) Smoke\n3) I don't know\nChoose one of the above answer\n ")

if choice_8 == "Light":
    print("wow you got the right answer")
    Score = Score + 1

else:
    print("Now that is a wrong answer " + "The correct answer is 'Light'")
    Score = Score - 1
print("You score is", Score)

time.sleep(1)

# prompting for 9th question

choice_9 = input(
    "If there are three apples and you take away two, how many apples do you have?\n"
    "1) One\n2) Two\n3) I don't know\nChoose one of the above answer\n ")

if choice_9 == "Two":
    print("wow you got the right answer")
    Score = Score + 1

else:
    print("Now that is a wrong answer " + "The correct answer is 'One'")
    Score = Score - 1
print("You score is", Score)

time.sleep(1)

# prompting for 10th question

choice_10 = input(
    "What would you find in the middle of Toronto?\n"
    "1) The letter “o”\n2) Treasure\n3) Water\nChoose one of the above answer\n ")

if choice_10 == "The letter o":
    print("wow you got the right answer")
    Score = Score + 1

else:
    print("Now that is a wrong answer " + "The correct answer is 'The letter “o”'")
    Score = Score - 1
print("You score is", Score)

time.sleep(1)


# making the report card for the total score
if Score >= 5:
    print("I like the way your brain works "+"\nYour score is ",Score)
else:
    print("\nI don't wanna make you feel bad about this game but you pretty bad at itt")
