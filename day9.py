# print(round(abs(float(input("Enter a number: ")))))   
#  scope: the region of the code where a variable is recognized
#  local variable: a variable declared inside a function
#  global variable: a variable declared outside a function
#  global keyword: it is used to create a global variable inside a function
# name = "abreham"
# def change_name():
    # name = "Delelew"
    # print(name)
# change_name()
# print(name)
# args and kwargs:
# args: it is a special operator we can pass to functions. it gathers remaining arguments as a tuple
# kwargs: it is a special operator we can pass to functions. it gathers remaining keyword arguments as a dictionary

# def sum_all(*args):
    # return sum(args)

# result = sum_all(1, 2, 3, 4)  # Result is 10
# print(result)

# def fav_colors(**kwargs):
    # for person,color in kwargs.items():
        # print(f"{person}'s favorite color is {color}")
        

#  random method in python 

# x = random.randint(1,10)
# print(x)
# y = random.random()
# print(y)

# book = ["fikir eskemekabir","adeferes","oromay","adafena"]
# z = random.choices(book)
# print(z)

#  exception handling in python

# try:
    # numerator = int(input("Enter numerator"))
    # denominator  = int(input("Entere denominator"))
    # result = numerator/denominator
    # print(result)
# except ZeroDivisionError as e:
    # print(e)
    # print("divided by zero is not logical dude")
# except ValueError as e:
    # print(e)
    # print("enter number only please")
# else:
    # print(result)
# finally:
    # print("its fine !!")

#  simple file detection in python

# file = "/home/misikir/Desktop/ICSMIS-IFMIS Integration.docx"
# if os.path.isfile(file):
    # print("The file exists")
    # if os.path.isdir(file):
        # print("The file is a directory")
    # else:
        #   print("The file is not a directory")    
# else:
    # print("The file does not exist")
# try:
    # with open("test.txt") as file:
        # print (file.read())
# except UnicodeDecodeError as e:
    # print(e)
    # print("The file is a binary file")
    # print("The file is open") 
# 
# text = "Hello, my name is Misikir Delelew"
# with open("readme.md","w") as file:
    # file.write(text)
    # print("The file is written")

#  copy file in python
# import shutil
# shutil.copy("readme.md","readme_copy.md")
# print("the file is copied")
import shutil

#  how to  move a file in python
sorcce = "readme.md"
destination = "/home/misikir/Desktop/readme.md"
shutil.move("readme.md","/home/misikir/Desktop/readme.md")
print("The file is moved")
