def question1():
    for i in range(11):
        print(i)

def question2():
    for row in range(1, 6):
        for num in range(1, row+1):
            print(num, end= " ")
        print()

def question3(n):
    total = 0
    for i in range(n+1):
        total = total + i
    print(total)

def question4(n):
    for i in range(1, 11):
        print(i*n)

def q5(newlist):
    for num in newlist:
        if num > 150:
            break
        if num%5 == 0:
            print(num)
    print("tits")

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

def q6(n):
    digit = 0
    print("Without looping: ", len(str(n)))
    while n > 0:
        n = n//10
        digit +=1

    print("Using loops: ", digit)

def q7():
    for row in range(1, 6):
        for num in range(6-row, 0, -1):
            print(num, end= " ")
        print()
def q8(rlist):
    newlist = []
    for num in range(len(rlist)-1, -1, -1):
        newlist.append(rlist[num])
    print(newlist)

rlist = [10, 20, 30, 40, 50]

def q9():
    for i in range(-10, 0, 1):
        print(i)

def q10(n):
    for i in range(n+1):
        print(i)
    print("Done!")

q10(5)
