def q1(string):
    # Given a string of odd length greater 7,
    # return a string made of the middle three chars of a given String
    middle = int(len(string)/2)
    print(string[middle-1:middle+2])

def q2(s1, s2):
    # Given 2 strings, s1 and s2,
    # create a new string by appending s2 in the middle of s1
    middle = int(len(s1)/2)
    print(s1[:middle]+s2+s1[middle:])

def q3(s1, s2):
    # Given 2 strings, s1, and s2 return a new string
    # made of the first, middle and last char each input string
    s1first = s1[:1]
    s2first = s2[:1]
    s1last = s1[-1]
    s2last = s2[-1]
    s1middle = s1[int(len(s1)/2)]
    s2middle = s2[int(len(s2)/2)]

    print(s1first+s2first+s1middle+s2middle+s1last+s2last)

def q4(input_string):
    # arrange String characters such that lowercase letters should come first
    lowercase = []
    uppercase = []

    # split lower/upper cases into two lists
    for letter in input_string:
        if letter.islower():
            lowercase.append(letter)
        else:
            uppercase.append(letter)

    # combine and print
    print(''.join(lowercase+ uppercase))

def q5(string):
    # Given a string input Count all lower case,
    # upper case, digits, and special symbols

    lowercount = 0
    uppercount = 0
    numcount = 0
    specialcount = 0

    for letter in string:
        if letter.islower():
            lowercount += 1
        elif letter.isupper():
            uppercount += 1
        elif letter.isdigit():
            numcount += 1
        else:
            specialcount += 1

    print("Lowercases: ", lowercount)
    print("Uppercases: ", uppercount)
    print()
    print("Total letters: ", lowercount + uppercount)
    print("Digits: ", numcount)
    print("Specials: ", specialcount)

def q6(s1, s2):
    # Given two strings, s1 and s2, create a mixed String
    s2rev = s2[::-1]
    length1 = len(s1)
    length2 = len(s2)
    length = length1 if length1 > length2 else length2

    string = ""

    for i in range(length):
        if i < length1:
            string = string + s1[i]
        if i < length2:
            string = string + s2rev[i]
    print(string)

def q7(s1, s2):
    # check if all the chars in the string1 are there in s2.
    # characters position doesn’t matter.

    if s1 in s2:
        print("s1 is in s2")
    else:
        print("dicks")

def q8(string):
    # Find all occurrences of “USA” in given string ignoring the case
    slist = string.split()
    count = 0
    for word in slist:
        if "usa" in word.lower():
            count += 1
    print(count)

def q8v2(string):
    string = string.lower()
    count = string.count("usa")
    print(count)

def q9(s1):
    slist = s1.split()
    total = 0
    classes = 0

    for char in slist:
        if char.isdigit():
            classes += 1
            total += float(char)

    print("Average grade: ", total/classes)

def q10(string):
    import collections
    from collections import Counter

    count = Counter(string)
    print(count)

def q10v2(string):
    countDict = dict()
    for char in string:
        count = string.count(char)
        countDict[char] = count
    print(countDict)

q10v2("pynativepynvepynative")


