import time
""""Imported time to use the time sleep function"""
   
questions = [
        ("1. Who is the main character in Hunt for the Wilderpeople? "
         "A) Ricky Baker B) Billy Tait C) Tim Johnson D) Johnny Blake", 'a'),
        ("2. What is the name of Ricky's foster uncle? "
         "A) Ricky Baker B) Billy Tait C) Tim Johnson D) Johnny Blake", 'b'),
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
"""Put the questions at the top as it is a variable"""

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
            print("See You Next Time :).")
            exit()
        elif response == "Y":
            print("Restarting the quiz...")
            time.sleep(1)
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
