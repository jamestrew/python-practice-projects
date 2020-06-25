def question1(x, y):
    product = x * y

    if product > 1000:
        return x + y
    else:
        return product

def question2():
    total = 0
    prev = 0
    for i in range(10):
        total = i + prev
        print("Current Number ", i, " Previous Number ", prev, "Sum: ", total)
        prev = i

def question3(text):
    for letter in range(0, len(text), 2):
        print("Index[", letter, "] - ", text[letter])


def question4(text, n):
    if n >= len(text):
        print("n must be less than the length of the string")
        return

    return text[n:]

def question5(newlist):
    if newlist[0] == newlist[-1]:
        print("the result is true")
    else:
        print("the result is false")

lt = [10, 20, 30, 40, 1]

def question6(numlist):
    for i in numlist:
        if i%5 == 0:
            print(i)

def question7(str):
    count = str.count("Emma")
    print("'Emma' appeared ", count, " times.")

#question7("Emma is a good developer. Emma is a writer. Emma is my old boss.")

def question8():
    rows = 6
    for num in range(rows):
        for i in range(num):
            print(num, end = " ")
        print()

def question9(num):
    flipped = 0
    digits = len(str(num))
    count = 0

    import math

    while num > 0:
        flipped = (flipped * 10) + num % 10
        num = num//10

    print()
    print("Final: ", flipped)


number = 123
question9(number)

def question10(list1, list2):
    list3 = []
    for i in list1:
        if i%2 != 0:
            list3.append(i)
    for i in list2:
        if i%2 == 0:
            list3.append(i)

    print(list3)

#question9([10, 20, 23, 11, 17], [13,43, 24, 36,  12])
