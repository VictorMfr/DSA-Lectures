"""
    HashMaps are like the SetMaps but with the difference that they store
    key value pairs.
    
    I've known that there're built-in functions for HashMaps in Javascript, but
    in python, they use it as dictionaries
"""

# 1. Create a hashmap
my_dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# 2. Access to value (using key)
print(my_dictionary["brand"]) 

# 3. Agregar o actualizar
my_dictionary["color"] = "red"
my_dictionary["year"] = 2023 

# 4. Delete
del my_dictionary["modelo"]

# 5. secure method .get()
# If key doesn't exists, returns None instead of an error
price = my_dictionary.get("price", "Not available")