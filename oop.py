# # object-oriented programming
#
# class Fruits:
#     def __init__(self):
#         self.name = "apple"
#         self.color = "red"
#
#
# fruits = Fruits()
#
#
# fruits.name = "mango"
# fruits.color = "orange"
#
# print(fruits.name)
# print(fruits.color)




class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color


fruit1 = Fruits('apple', 'red')
fruit2 = Fruits('banana', 'yellow')
fruit3 = Fruits('mango', 'orange')

print(f"Fruit1: {fruit1.name},{fruit1.color}")
print(f"Fruit2: {fruit2.name},{fruit2.color}")
print(f"Fruit3: {fruit3.name},{fruit3.color}")