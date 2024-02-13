class Person:
    def james(self):
        print("can talk")

    def tom(self):
        print("speaks English")

# kk = Person()
# print(kk.james())

class Parrot(Person):
    def kilo(self):
        print("can walk")

kk = Parrot()
        
print(kk.james())


# yy = Parrot()
# print(yy.kilo())