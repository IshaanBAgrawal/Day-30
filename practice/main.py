# # # Types of errors

# # FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# # KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# # TypeError
# text = "abc"
# print(text + 5)


# Dealing with such errors gracefully or using them for our own benefit

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w")
#     file.write("Something")
# except KeyError as wrong_key:
#     print(f"The key {wrong_key} doesn't exits")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     raise TypeError("fake Error")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height cannot be above 3 meters.")
else:
    bmi = weight / height ** 2
    print(bmi)
