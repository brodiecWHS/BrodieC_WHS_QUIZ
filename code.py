print("Hello welcome to my quiz")
print("Please answer all questions truthfully and to your best ability")
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
print("Question 1")

#how to add multi choice questions
print("do you want jam or honey")
d1 = input("Do you want : A) Jam. B)Honey [A/B]: ")
if d1 == "A":
    print("Yum, Jam")
if d1 == "B":
    print("Sticky, Honey")
