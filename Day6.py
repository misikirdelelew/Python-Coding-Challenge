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

# drink =  ["cocacola","coffe","tea"]
# breafast= ["pizza","humberger","spageti"]
# dessert =["cake","ice-cream"]
# food = [drink,breafast,dessert]
# print(food[0][2])


#  Day 6 
# tuples : orderd unchangable used to group the same items

# student = ("Misikir","Delelew","Delelew")
# if "Misikir" in student:
    # print("Misikir is in the student tuple")
# 
    # for x in student:
    #   print(x)
# print(student.index("Misikir"))
# print(student.count("Delelew"))
# print(student)

# set: collection which is unorderd: no duplicate items
# set : unordered, unchangeable, no duplicate items

# utensils = {"fork","spoon","knife"}
# dishes = {"bowl","plate","cup","knife"}
# utensils.add("napkin")
# utensils.difference(dishes)
# utensils.intersection(dishes)
# utensils.pop()
# print(utensils)
# x= utensils.union(dishes)
# print(utensils)

#  Dictionary: collection which is unordered, changeable and indexed. written with curly brackets, and they have keys and values
capital = {"Ethiopia":"Addis Ababa","Kenya":"Nairobi","Nigeria":"Abuja"}
# print(capital["Ethiopia"])
# print(capital.get("Nigeria"))
# capital["Ghana"]="Accra"
# print(capital)
# capital.pop("Kenya")
# print(capital)
# capital.update({"Nigeria":"Lagos"})
# print(capital)

# for key in capital.items():
    # print(key,value)
    # print(key)
# 
# for key in capital.keys():
    # print(key)
# for value in capital.values():
    # print(value)

#  Functions: a block of code which only runs when it is called. you can pass data, known as parameters, into a function. a function can return data as a result
# def say_hello():
    # print("Hello!")
# say_hello()
# say_hello()
# say_hello()
