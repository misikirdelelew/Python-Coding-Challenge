import math
import time
# mafunction is a builtin function for mathematical operations! 

pi = 3.14
x = 1
y = 2
z =3

# print(round(pi))
# print(math.ceil(pi))
# print(math.sqrt(pi))
# print(math.pow(pi,2))
# print(max(x,y,z))
# print(min(x,y,z))

#  String Slcing in python
#  its creating substring from a given string. we can do it with index[],slice(): [start:stop:step]: the first character inclusive, the last character exclusive

name = "Misikir Delelew"
# first_name = name[0:7]
# last_name = name[8:]
# print(first_name)
# print(last_name)

# website = "https://yahoo.com"
# website1 = "https://google.com"
# 
# x = slice(8,)
# y = slice(1,8)
# print(website[x])
# print(website1[y])

#  If statement :excutes  the condition is True
# age = int(input("How old are you:"))

# if age == 100:
    # print("You are century years old!")
# elif age >= 20:
    # print("You are an adult!"
# elif age > 10:
    # print("you are a child")
# else:
    # print("you are so child!")

# while : it

# N=10
# sum = 0
# counter = 1
# 
# while counter <= N:
    # sum = sum + counter
# print("sun of 1 until ",N," is ",sum)
    
fruits = ["apple","banana","cherry"]
# for x in fruits:
    # print(x)

# for letter in "banana":
    # print(letter)
    # if letter == "n":
        # break
    # print("letter is ",letter)

# for i in range(10):
        # print(i)
        # if i == 5:
            # break
        # print("i is ",i)      
# import random

# secr/et_number = random.randint(1, 10)
# guess = None
# 
# while guess != secret_number:
    # guess = int(input("Guess the number between 1 and 10: "))
    # if guess < secret_number:
        # print("Too low!")
    # elif guess > secret_number:
        # print("Too high!")
# print("Congratulations! You've guessed the correct number."


# for i in range(1,11):
#   print(i)

# name= 'Misikir Delelew'
# for i in reversed(name):
#    print(i)

# for second in range(10,0,-1):
    # print(second)
    # time.sleep(2)
# print("Happy New Year!")
    
# def factorial(n):

# Nested for loop in python

# row = int(input("How many Rows you have?"))
# col = int(input("How many columns you have?"))
# symbole = input("please write your symbole?")
# for i in range(row):
#    for j in range(col):
    #   print(symbole, end=
    # "")
    #   print()

    #  loop control statements: break, continue, pass

#  break: it terminates the loop and transfers the execution to the statement immediately following the loop
#  continue: it causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating
#  pass: it is used when a statement is required syntactically but you do not want any command or code to execute
# i=int(input("Enter a number:"))
# for i in range(1,15):
    # if i==6:
        # break
    # print(i)
# 
# phone_number = "123-456-78uuuuuu90"
# for i in phone_number:
    # if i == "-" or i == "u":
        # continue
    # print(i, end="")

# phone_number = "123-456-78uuuuuu90"
# for i in phone_number:
    # if i == "-" or i == "u":
        # pass
    # print(i, end="")

# List in python: it is a collection of items. it is ordered and changeable. it allows duplicate items. it is written with square brackets
# food = ["rice","beans","bread","pasta",]
# food.insert(0,"meat")
# food.reverse()
# food.index("rice")

# food.append("meat")
# print(food)
# food.remove("rice")
# food.pop() 

# 2D list: 

drink =  ["cocacola","coffe","tea"]
breafast= ["pizza","humberger","spageti"]
dessert =["cake","ice-cream"]
food = [drink,breafast,dessert]
print(food[0][2])
