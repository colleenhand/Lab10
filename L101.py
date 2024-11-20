#The authors' names are: Colleen and Anna
def my_get_method(dictionary, key, default):
    if key in dictionary:
        return dictionary[key]
    else:
        return default

fruits = {"apple":1, "banana":2, "orange":4}

print(my_get_method(fruits, "apple", 0))
print(my_get_method(fruits, "peach", 0))

