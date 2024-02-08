math = int(input("Score in Math: "))
eng =   int(input("Score in English: "))
kis =   int(input("Score in Kiswahili: "))
bio =   int(input("Score in Biology: "))
chem=   int(input("Score in Chemistry: "))


if math > 100 or  math < 0:
    print("Invalid input")

if eng > 100 or eng < 0:
    print("Invalid input")

if kis > 100 or kis < 0:
    print("Invalid input")

if bio > 100 or bio < 0:
    print("Invalid input")

if chem > 100 or chem < 0:
    print("Invalid input")


print(f"Average score:{(math+eng+kis+bio+chem)/5}")


if (math+eng+kis+bio+chem)/5 > 0 and (math+eng+kis+bio+chem)/5 <40:
    print("Grade : E")

elif (math+eng+kis+bio+chem)/5 > 39 and (math+eng+kis+bio+chem)/5 < 51:
    print("Grade: D")

elif (math+eng+kis+bio+chem)/5 > 50 and (math+eng+kis+bio+chem)/5 < 61:
    print("Grade: C")

elif (math+eng+kis+bio+chem)/5 > 60 and (math+eng+kis+bio+chem)/5 < 71:
    print("Grade: B")

elif (math+eng+kis+bio+chem)/5 > 70 and  (math+eng+kis+bio+chem)/5 < 100:
    print("Grade: A")