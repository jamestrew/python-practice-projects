def q1(a, b):
    print(str(a*b))

def q2():
    print("My", "name", "is", "James", sep = "**")

def q3(n):
    print("%o" % (n))

# string specifiers

def q4():
    n = 458.54123456
    print("%.2f" % n)

def q5():
    newlist = []
    for i in range(5):
        newlist.append(input("Enter a float: "))
    print(newlist)

def q6():
    with open("test.txt", "r") as file:
        lines = file.readlines()
        count = len(lines)
        print(lines)
        print(count)
    with open("newFile.txt", "w") as file:
        count = 1
        for line in lines:
            if count == 5:
                pass
            else:
                file.write(line)
            count +=1

def q7():
    str1, str2, str3 = input("Enter three strings: ").split()
    print(str1, str2, str3)

def q8():
    quantity = 3
    totalMoney = 1000
    price = 450

    print("I have {0} dollars so I can buy {1} footballss for {2:.2f} dollars".format(totalMoney, quantity, price))

def q9():
    file = open("test.txt", "r")
    text = file.read()
    file.close()
    if text:
        print("File not empty")
    else:
        print("File empty")

def q10():
    with open("test.txt", "r") as file:
        lines = file.readlines()
        print(lines[3])

q10()

