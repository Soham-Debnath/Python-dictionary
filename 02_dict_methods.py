# This codes show dictionary functions.

marks = {
    "Harry" : 100,
    "Shubham" : 69,
    "Rohan" : 23,
    0 : "Harry"
}

# print(marks["Harry"]) #100

# print(marks.items()) #Key value pairs in terms of tuple

# print(marks.keys())  #dict_keys(['Harry', 'Shubham', 'Rohan', 0])
# print(marks.values()) #dict_values([100, 69, 23, 'Harry'])

# marks.update({"Harry":99,"Soham":100})
# print(marks)           #{'Harry': 99, 'Shubham': 69, 'Rohan': 23, 0: 'Harry', 'Soham': 100}

# print(marks["Harry"])      # 100
# print(marks.get("Harry"))  # 100

# print(marks.get("Harry2")) # Prints None
# print(marks["Harry2"])    # Returns error

# marks.clear()
# print(marks)    #{}  = empty disctionary

# value= marks.pop("Harry",100)
# print(value)   # 100

# marks.pop("Harry",100)
# print(marks)   # {'Shubham': 69, 'Rohan': 23, 0: 'Harry'}

s = {}
print(s,type(s))
