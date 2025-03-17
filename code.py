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
    d1 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower()
    if d1 == "a":
        print("Yum, Jam!")
        break
    elif d1 == "b":
        print("Sticky, Honey!")
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
