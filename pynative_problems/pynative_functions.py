def q1(name, age):
    print(name, age)

def q2(*num): # asterisks allow for variable length of arguments
    for i in num:
        print(i)

def q3(a, b):
    return a+b, a-b

def q4(name, salary = 9000):
    print(name, "salary is ", salary)

def q6(n):
    if n == 0:
        return 0
    return n + q6(n-1)

#q7
q7 = q1

def q8():
    for i in range(4, 30):
        if i%2 == 0:
            print(i)

def q9(alist):
    num = 0
    for i in alist:
        if i >= num:
            num = i
    print(num)
    print(max(alist)) # preferred method
    alist.sort() # suitable for maybe finding the second biggest num
    print(alist[-1])

q9([4, 6, 8, 24, 12, 2])
