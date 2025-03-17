import time
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
time.sleep(1)
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
time.sleep(1)
while True:
    print("Question 2")
    time.sleep(1)
    d2 = input("Do you want: A) Jam. B) Honey [A/B]: ").lower() 

    if d2 == "a":
        print("Yum, Jam")
        break  
    elif d2 == "b":
        print("Sticky, Honey")
        break  
    else:
        print("Please enter A or B.")
        continue
