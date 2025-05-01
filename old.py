#7th of March
print("Hello welcome to my quiz")
print("Please answer all questions truthfully and to your best ability")
print("Question 1")
print("What is your name? ")
user_name = input()
print("nice to meet you {}")

#11th of March 
print("Hello welcome to my quiz")
print("Please answer all questions truthfully and to your best ability")
print("Just a few questions to get to know you")
print("What is your name? ")
user_name = input()

print("nice to meet you {}".format(user_name))
print("How old are you?")
user_age = input()
print("And finally whats something you enjoy doing?")
user_fun = input()
print ("So your name is {}, You are {} Years old and enjoy {}".format(user_name,user_age,user_fun))
print("Thanks for answering those questions")
print ("Now we can get onto the real questions!")
'''

str_userName = ''
int_userAge = 0

print("Hello user, what's your name?")
str_userName = input('')
print(f'Hello {str_userName}. How old are you? ')
int_userAge = int(input(''))

if int_userAge > 30:
    print(f'Man, {str_userName}, {int_userAge} is ancient')
else:
    (f'{str_userName} you are {int_userAge} years old')

    #17 of March 
    print("Hello welcome to my quiz")
print("Please answer all questions truthfully and to your best ability")
print("Please be case sensitive")
print("Just a few questions to get to know you")
print("What is your name? ")
str_userName = input()
print("nice to meet you {}".format(str_userName))
print("How old are you?")

while True:    
    try:
        int_userAge = int(input())
        break
    except:
        print("Please enter a number")
    print("How old are you?")   
    continue

print("And finally whats something you enjoy doing?")
user_fun = input()
print ("So your name is {}, You are {} Years old and enjoy {}".format(str_userName,int_userAge,user_fun))
print("Thanks for answering those questions")
print ("Now we can get onto the real questions!")
while True: 
    print("Question 1")
    d1 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower() 

    if d1 == "a":
        print("Yum, Jam")
        break  
    elif d1 == "b":
        print("Sticky, Honey")
        break  
    else:
        print("Please enter A or B.")

        #31st of march

      #print introduction
#user inputs (name,age,fun)
#print question 1 - user input
#print question 2 - user input 
#print question 3 - user input 
#print question 4 - user input 
#print question 5 - user input 
#print question 6 - user input 
#print question 7 - user input 
#print question 8 - user input 
#print question 9 - user input 
#print question 10 - user input 
#print percentage of questions correct
#print thanks for quiz participation
import time
print("Hello, welcome to my quiz")
time.sleep(1)
print("Please answer all questions truthfully and to your best ability")
time.sleep(1)
print("Just a few questions to get to know you")
time.sleep(1)

print("What is your name? ")
str_userName = input()
print(f"Nice to meet you {str_userName}")

print("How old are you?")
while True:
    try:
        int_userAge = int(input())
        break
    except ValueError:
        print("Please enter a valid number.")
print(f"Your age is {int_userAge}.")

print("And finally, what's something you enjoy doing?")
user_fun = input()
print(f"So your name is {str_userName}, you are {int_userAge} years old, and you enjoy {user_fun}.")
time.sleep(1)
print("Thanks for answering those questions.")
print("Now we can get onto the real questions!")

while True:
    print("Question 1")
    d1 = input("Who is the main character in Hunt for the Wilderpeople?: A)Ricky Baker . B) Billy Tait . C)Tim Johnson . D) Johnny Blake [A/B/C/D]: ").lower()
    if d1 == "a":
        print("Correct +1 Point")
    if d1 == "a":
   `     score += 1
        break
    elif d1 == "b":
        print("Incorrect")
        elif d1 == "b":
        print("Incorrect")   
    


break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 2")
    d2 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d2 == "a":
        print("Yum, Jam!")
        break
    elif d2 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 3")
    d3 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d3 == "a":
        print("Yum, Jam!")
        break
    elif d3 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 4")
    d4 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d4 == "a":
        print("Yum, Jam!")
        break
    elif d4 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 5")
    d5 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d5 == "a":
        print("Yum, Jam!")
        break
    elif d5 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 6")
    d6 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d6 == "a":
        print("Yum, Jam!")
        break
    elif d6 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 7")
    d7 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d7 == "a":
        print("Yum, Jam!")
        break
    elif d7 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 8")
    d8 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d8 == "a":
        print("Yum, Jam!")
        break
    elif d8 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 9")
    d9 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d9 == "a":
        print("Yum, Jam!")
        break
    elif d9 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 10")
    d10 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d10 == "a":
        print("Yum, Jam!")
        break
    elif d10 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)
    print (score)

    3rd of april 
    #print introduction
#user inputs (name,age,fun)
#print question 1 - user input
#print question 2 - user input 
#print question 3 - user input 
#print question 4 - user input 
#print question 5 - user input 
#print question 6 - user input 
#print question 7 - user input 
#print question 8 - user input 
#print question 9 - user input 
#print question 10 - user input 
#print percentage of questions correct
#print thanks for quiz participation
import time
score = 0
total_questions = 10
bool_scoreloop = True
# Setting variables
BOOL_QUESTION = True


print("Hello, welcome to my quiz")
time.sleep(1)
print("Please answer all questions truthfully and to your best ability")
time.sleep(1)
print("Just a few questions to get to know you")
time.sleep(1)

print("What is your name? ")
str_userName = input()
print(f"Nice to meet you {str_userName}")

print("How old are you?")
while True:
    try:
        int_userAge = int(input())
        break
    except ValueError:
        print("Please enter a valid number.")
print(f"Your age is {int_userAge}.")

print("And finally, what's something you enjoy doing?")
user_fun = input()
print(f"So your name is {str_userName}, you are {int_userAge} years old, and you enjoy {user_fun}.")
time.sleep(1)
print("Thanks for answering those questions.")
print("Now we can get onto the real questions!")

    print("Question 1")
    d1 = input("Who is the main character in Hunt for the Wilderpeople?: \
    A)Ricky Baker . B) Billy Tait . C)Tim Johnson . D) Johnny Blake [A/B/C/D]: ")\
    .lower()
    if d1 == "A":
        print("Correct +1 Point")
        score += 1
    if d1 == "a":
        break
    elif d1 == "b":
        print("Incorrect")
    elif d1 == "c":
        print("Incorrect")   
    elif d1 == "d":
        print("Incorrect")
    else:
        print("Please enter A,B,C or D.")
    time.sleep(1)

while True:
    print("Question 2")
    d1 = input("What is the name of Ricky's foster uncle?: A)Ricky Baker . B) Billy Tait . C)Tim Johnson . D) Johnny Blake [A/B/C/D]: ").lower()
    if d1 == "a":
        print("Correct +1 Point")
        score += 1
    if d1 == "a":
        break
    elif d1 == "b":
        print("Incorrect")
    elif d1 == "c":
        print("Incorrect")   
    elif d1 == "d":
        print("Incorrect")
        break
    else:
        print("Please enter A,B,C or D.")
    time.sleep(1)


while True:
    print("Question 3")
    d3 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d3 == "a":
        print("Yum, Jam!")
          score += 1
        break
    elif d3 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 4")
    d4 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d4 == "a":
        print("Yum, Jam!")
      score += 1    
    break
    elif d4 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 5")
    d5 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d5 == "a":
        print("Yum, Jam!")
        break
    elif d5 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 6")
    d6 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d6 == "a":
        print("Yum, Jam!")
        break
    elif d6 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 7")
    d7 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d7 == "a":
        print("Yum, Jam!")
        break
    elif d7 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 8")
    d8 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d8 == "a":
        print("Yum, Jam!")
        break
    elif d8 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 9")
    d9 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d9 == "a":
        print("Yum, Jam!")
        break
    elif d9 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)

while True:
    print("Question 10")
    d10 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d10 == "a":
        print("Yum, Jam!")
        break
    elif d10 == "b":
        print("Sticky, Honey!")
        break
    else:
        print("Please enter A or B.")
    time.sleep(1)
    print (score)
    questions
"""
#8th of april
#print introduction
#user inputs (name,age,fun)
#print question 1 - user input
#print question 2 - user input 
#print question 3 - user input 
#print question 4 - user input 
#print question 5 - user input 
#print question 6 - user input 
#print question 7 - user input 
#print question 8 - user input 
#print question 9 - user input 
#print question 10 - user input 
#print percentage of questions correct
#print thanks for quiz participation
import time
def start():
# Add score variable
score = 0
total_questions = 10

# Print introduction
print("Hello, welcome to my quiz!")
time.sleep(1)
print("Please answer all questions truthfully and to your best ability.")
time.sleep(1)

# User input for name, age, and hobby
str_userName = input("What is your name? ")
print(f"Nice to meet you, {str_userName}!")

# Validate age input
while True:
    try:
        int_userAge = int(input("How old are you? "))
        break
    except ValueError:
        print("Please enter a valid number.")
print(f"Your age is {int_userAge}.")
user_fun = input("And finally, what's something you enjoy doing? ")
print(f"So your name is {str_userName}, you are {int_userAge} years old, and you enjoy {user_fun}.")
time.sleep(1)
print("Thanks for answering those questions.")
print("Now we can get onto the real questions!")

# Function to ask a question and validate the answer
def ask_question(question, correct_answer, options):
    while True:
        answer = input(f"{question} [{options}]: ").lower()
        if answer == correct_answer:
            return True
        elif answer in options.lower():
            print("Incorrect")
            return False
        else:
            print("Please Enter A, B, C or D.")

# Questions and scoring
# Question 1
if ask_question("1. Who is the main character in Hunt for the Wilderpeople? A) Ricky Baker. B) Billy Tait. C) Tim Johnson. D) Johnny Blake", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 2
if ask_question("2. What is the name of Ricky's foster uncle? A) Ricky Baker. B) Billy Tait. C) Tim Johnson. D) Johnny Blake", 'b', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 3
if ask_question("3. Which animal do Hec and Ricky hunt together? A) Wild Boar. B) Kangaroo. C) Deer. D) Bear", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 4
if ask_question("4. What does Bella give Ricky for his birthday? A) A handmade birthday song and a hot water bottle. B) A hunting knife and boots. C) A video game console. D) A pet parrot", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 5
if ask_question("5. What does Paula repeatedly say about Ricky? A) 'No child left behind.' B) 'We will find him!' C) 'He's a criminal now.' D) 'I never lose a case.'", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 6
if ask_question("6. What is the name of Ricky's dog? A) Tupac. B) Notorious. C) Biggie. D) Scarface", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 7
if ask_question("7. Which book is Hunt for the Wilderpeople based on? A) Wild Pork and Watercress. B) The Bushman's Guide. C) Into the Wild. D) Runaway Boy", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 8
if ask_question("8. What does Hec reveal about himself while on the run with Ricky? A) He is illiterate and never learned to read. B) He used to be a famous rugby player. C) He has been in witness protection. D) He once lived in Australia", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 9
if ask_question("9. Did Hec make the cake for Ricky's birthday? A) Yes. B) No.", 'b', 'A/B'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 10
if ask_question("10. What does Ricky call Hec? A) Uncle. B) Hec. C) Dad. D) Friend", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Calculate the percentage of correct answers
percentage = (score / total_questions) * 100

# Display the result
print(f"Your score: {score}/{total_questions}")
print(f"Percentage: {percentage:.2f}")
print("Thanks for participating in the quiz!")
start()

11th of april 
while True:
#print introduction
#user inputs (name,age,fun)
#print question 1 - user input
#print question 2 - user input 
#print question 3 - user input 
#print question 4 - user input 
#print question 5 - user input 
#print question 6 - user input 
#print question 7 - user input 
#print question 8 - user input 
#print question 9 - user input 
#print question 10 - user input 
#print percentage of questions correct
#print thanks for quiz participation
import time
# Add score variable
score = 0
total_questions = 10

# Print introduction
print("Hello, welcome to my quiz!")
time.sleep(1)
print("Please answer all questions truthfully and to your best ability.")
time.sleep(1)

# User input for name, age, and hobby
str_userName = input("What is your name? ")
print(f"Nice to meet you, {str_userName}!")

# Validate age input
while True:
    try:
        int_userAge = int(input("How old are you? "))
        break
    except ValueError:
        print("Please enter a valid number.")
print(f"Your age is {int_userAge}.")
user_fun = input("And finally, what's something you enjoy doing? ")
print(f"So your name is {str_userName}, you are {int_userAge} years old, and you enjoy {user_fun}.")
time.sleep(1)
print("Thanks for answering those questions.")
print("Now we can get onto the real questions!")

# Function to ask a question and validate the answer
def ask_question(question, correct_answer, options):
    while True:
        answer = input(f"{question} [{options}]: ").lower()
        if answer == correct_answer:
            return True
        elif answer in options.lower():
            print("Incorrect")
            return False
        else:
            print("Please Enter A, B, C or D.")

# Questions and scoring
# Question 1
if ask_question("1. Who is the main character in Hunt for the Wilderpeople? A) Ricky Baker. B) Billy Tait. C) Tim Johnson. D) Johnny Blake", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 2
if ask_question("2. What is the name of Ricky's foster uncle? A) Ricky Baker. B) Billy Tait. C) Tim Johnson. D) Johnny Blake", 'b', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 3
if ask_question("3. Which animal do Hec and Ricky hunt together? A) Wild Boar. B) Kangaroo. C) Deer. D) Bear", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 4
if ask_question("4. What does Bella give Ricky for his birthday? A) A handmade birthday song and a hot water bottle. B) A hunting knife and boots. C) A video game console. D) A pet parrot", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 5
if ask_question("5. What does Paula repeatedly say about Ricky? A) 'No child left behind.' B) 'We will find him!' C) 'He's a criminal now.' D) 'I never lose a case.'", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 6
if ask_question("6. What is the name of Ricky's dog? A) Tupac. B) Notorious. C) Biggie. D) Scarface", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 7
if ask_question("7. Which book is Hunt for the Wilderpeople based on? A) Wild Pork and Watercress. B) The Bushman's Guide. C) Into the Wild. D) Runaway Boy", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 8
if ask_question("8. What does Hec reveal about himself while on the run with Ricky? A) He is illiterate and never learned to read. B) He used to be a famous rugby player. C) He has been in witness protection. D) He once lived in Australia", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 9
if ask_question("9. Did Hec make the cake for Ricky's birthday? A) Yes. B) No.", 'b', 'A/B'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 10
if ask_question("10. What does Ricky call Hec? A) Uncle. B) Hec. C) Dad. D) Friend", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Calculate the percentage of correct answers
percentage = (score / total_questions) * 100
# Display the result
print(f"Your score: {score}/{total_questions}")
print(f"Percentage: {percentage:.2f}")
print("Thanks for participating in the quiz!")

# Prompting the user to restart or exit
while True:
    response = input("Do you want to restart? (Y/N): ")
    
    # Check the user's response
    if response.upper() == "N":
        print("Exiting the program.")
        break  # Exit the loop, thus ending the program
    elif response.upper() == "Y":
        print("Restarting the quiz...")
        # Here you would reset any necessary variables or call your quiz function again
        break  # Exit to start over (or replace this with actual restart logic)
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")

        29th of april 
        while True:
#print introduction
#user inputs (name,age,fun)
#print question 1 - user input
#print question 2 - user input 
#print question 3 - user input 
#print question 4 - user input 
#print question 5 - user input 
#print question 6 - user input 
#print question 7 - user input 
#print question 8 - user input 
#print question 9 - user input 
#print question 10 - user input 
#print percentage of questions correct
#print thanks for quiz participation
import time
# Add score variable
score = 0
total_questions = 10

# Print introduction
print("Hello, welcome to my quiz!")
time.sleep(1)
print("Please answer all questions truthfully and to your best ability.")
time.sleep(1)

# User input for name, age, and hobby
str_userName = input("What is your name? ")
print(f"Nice to meet you, {str_userName}!")

# Validate age input
while True:
    try:
        int_userAge = int(input("How old are you? "))
        break
    except ValueError:
        print("Please enter a valid number.")
print(f"Your age is {int_userAge}.")
user_fun = input("And finally, what's something you enjoy doing? ")
print(f"So your name is {str_userName}, you are {int_userAge} years old, and you enjoy {user_fun}.")
time.sleep(1)
print("Thanks for answering those questions.")
print("Now we can get onto the real questions!")

# Function to ask a question and validate the answer
def ask_question(question, correct_answer, options):
    while True:
        answer = input(f"{question} [{options}]: ").lower()
        if answer == correct_answer:
            return True
        elif answer in options.lower():
            print("Incorrect")
            return False
        else:
            print("Please Enter A, B, C or D.")

# Questions and scoring
# Question 1
if ask_question("1. Who is the main character in Hunt for the Wilderpeople? A) Ricky Baker. B) Billy Tait. C) Tim Johnson. D) Johnny Blake", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 2
if ask_question("2. What is the name of Ricky's foster uncle? A) Ricky Baker. B) Billy Tait. C) Tim Johnson. D) Johnny Blake", 'b', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 3
if ask_question("3. Which animal do Hec and Ricky hunt together? A) Wild Boar. B) Kangaroo. C) Deer. D) Bear", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 4
if ask_question("4. What does Bella give Ricky for his birthday? A) A handmade birthday song and a hot water bottle. B) A hunting knife and boots. C) A video game console. D) A pet parrot", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 5
if ask_question("5. What does Paula repeatedly say about Ricky? A) 'No child left behind.' B) 'We will find him!' C) 'He's a criminal now.' D) 'I never lose a case.'", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 6
if ask_question("6. What is the name of Ricky's dog? A) Tupac. B) Notorious. C) Biggie. D) Scarface", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 7
if ask_question("7. Which book is Hunt for the Wilderpeople based on? A) Wild Pork and Watercress. B) The Bushman's Guide. C) Into the Wild. D) Runaway Boy", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 8
if ask_question("8. What does Hec reveal about himself while on the run with Ricky? A) He is illiterate and never learned to read. B) He used to be a famous rugby player. C) He has been in witness protection. D) He once lived in Australia", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 9
if ask_question("9. Did Hec make the cake for Ricky's birthday? A) Yes. B) No.", 'b', 'A/B'):
    score += 1
    print("Correct!")
time.sleep(1)

# Question 10
if ask_question("10. What does Ricky call Hec? A) Uncle. B) Hec. C) Dad. D) Friend", 'a', 'A/B/C/D'):
    score += 1
    print("Correct!")
time.sleep(1)

# Calculate the percentage of correct answers
percentage = (score / total_questions) * 100
# Display the result
print(f"Your score: {score}/{total_questions}")
print(f"Percentage: {percentage:.2f}")
print("Thanks for participating in the quiz!")

# Prompting the user to restart or exit
while True:
    response = input("Do you want to restart? (Y/N): ")
    
    # Check the user's response
    if response.upper() == "N":
        print("Exiting the program.")
        break  # Exit the loop, thus ending the program
    elif response.upper() == "Y":
        print("Restarting the quiz...")
        # Here you would reset any necessary variables or call your quiz function again
        break  # Exit to start over (or replace this with actual restart logic)
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        1st of may 
        import time
""""Imported time to use the time sleep function"""

questions = [
    ("1. Who is the main character in Hunt for the Wilderpeople? "
     "A) Ricky Baker B) Billy Tait C) Tim Johnson D) Johnny Blake", 'a'),
    ("2. What is the name of Ricky's foster uncle? "
     "A) Hec B) Ricky C) Tim D) Johnny", 'a'),
    ("3. Which animal do Hec and Ricky hunt together? "
     "A) Wild Boar B) Kangaroo C) Deer D) Bear", 'a'),
    ("4. What does Bella give Ricky for his birthday? "
     "A) A handmade birthday song and a hot water bottle B) A hunting knife and boots "
     "C) A video game console D) A pet parrot", 'a'),
    ("5. What does Paula repeatedly say about Ricky? "
     "A) 'No child left behind.' B) 'We will find him!' "
     "C) 'He's a criminal now.' D) 'I never lose a case.'", 'a'),
    ("6. What is the name of Ricky's dog? "
     "A) Tupac B) Notorious C) Biggie D) Scarface", 'a'),
    ("7. Which book is Hunt for the Wilderpeople based on? "
     "A) Wild Pork and Watercress B) The Bushman's Guide C) Into the Wild D) Runaway Boy", 'a'),
    ("8. What does Hec reveal about himself while on the run with Ricky? "
     "A) He is illiterate and never learned to read B) He used to be a famous rugby player "
     "C) He has been in witness protection D) He once lived in Australia", 'a'),
    ("9. Did Hec make the cake for Ricky's birthday? A) Yes B) No", 'b'),
    ("10. What does Ricky call Hec? A) Uncle B) Hec C) Dad D) Friend", 'a')
]

def ask_question(question, correct_answer, options):
    """Prompts user with a question and validates input."""
    while True:
        answer = input(f"{question} [{options}]: ").lower()
        if answer == correct_answer:
            return True
        elif answer in options.lower().replace(' ', '').replace('/', ''):
            print("Incorrect")
            return False
        else:
            print("Please enter a valid option.")

def run_quiz():
    score = 0
    total_questions = 10

    print("Hello, welcome to my quiz!")
    time.sleep(1)
    print("Please answer all questions truthfully and to your best ability.")
    time.sleep(1)

    user_name = input("What is your name? ")
    print(f"Nice to meet you, {user_name}!")

    while True:
        try:
            user_age = int(input("How old are you? "))
            break
        except ValueError:
            print("Please enter a valid number.")

    if 1 <= user_age <= 10:
        print("You're a bit young for tech! Go play outside instead.")
        exit()
    elif 46 <= user_age <= 100:
        print("You're an oldie! But let's continue anyway.")
    elif user_age > 100 or user_age < 1:
        print("Hmm, that doesn't seem like a valid age for this quiz.")
        exit()

    print(f"Your age is {user_age}.")
    user_hobby = input("And finally, what's something you enjoy doing? ")
    print(f"So your name is {user_name}, you are {user_age} years old, and you enjoy {user_hobby}.")
    time.sleep(1)
    print("Thanks for answering those questions.")
    print("Now we can get onto the real questions!")

    for question, correct_answer in questions:
        if ask_question(question, correct_answer, 'A/B/C/D'):
            score += 1
            print("Correct!")
        time.sleep(1)

    percentage = (score / total_questions) * 100

    print(f"Your score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.2f}%")
    print("Thanks for participating in the quiz!")

while True:
    run_quiz()

    while True:
        response = input("Do you want to restart? (Y/N): ").strip().upper()
        if response == "N":
            print("See You Next Time.")
            exit()
        elif response == "Y":
            print("Restarting the quiz...")
            time.sleep(1)
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
