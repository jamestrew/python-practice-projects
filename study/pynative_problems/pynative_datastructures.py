listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

def q1(list1, list2):
    # Given a two list. Create a third list by picking an odd-index element
    # from the first list and even index elements from second.

    len1 = len(list1)
    len2 = len(list2)
    length = len1 if len1 > len2 else len2
    newlist = []

    for i in range(length):
        if i%2 != 0:
            newlist.append(list1[i])
        else:
            newlist.append(list2[i])
    print(newlist)

def q1v2(list1, list2):
    newlist = []
    newlist.extend(list1[1::2])
    newlist.extend(list2[0::2])
    print(newlist)


def q2(list1):
    # Given an input list removes the element at index 4
    # and add it to the 2nd position and also, at the end of the list

    print("Original list: ", list1)
    p_num = list1[4]
    p_list = list1.pop(4)
    print("List after removing element at index 4: ", list1)
    list1.insert(2, p_num)
    print("List after adding element at index 2: ", list1)
    list1.append(p_num)
    print("List after adding element at last: ", list1)

def q3(list1):
    # Given a list slice it into a 3 equal chunks and rever each list
    print(list1)
    chunk_length = int(len(list1)/3)
    print()

    for i in range(chunk_length):
        index = i * chunk_length
        chunk = list1[index:index + chunk_length]
        print("Chunk ", i+1, " ", chunk)
        chunk.reverse()
        print("After reversing it", chunk)

def q4(list1):
    # Given a list iterate it and count the occurrence of each element
    # and create a dictionary to show the count of each element

    print("Original list: ", list1)
    countDict = dict()

    for num in list1:
        count = list1.count(num)
        countDict[num] = count

    print(countDict)

def q5(list1, list2):
    # Given a two list of equal size create a set
    # such that it shows the element from both lists in the pair

    print(tuple(zip(list1, list2)))

def q6(set1, set2):
    # Given a following two sets find the intersection
    # and remove those elements from the first set


    intersect = set1.intersection(set2)
    print(intersect)
    diff = set1.difference(set2)
    print(diff)

def q7(set1, set2):
    # Given two sets, Checks if One Set is Subset or superset of Another Set.
    # if the subset is found delete all elements from that set

    print("First set: ", set1)
    print("Second set: ", set2)
    print()

    answer = set1.issubset(set2)
    print("First set is a subset of second set - ", answer)
    if answer:
        set1.clear()
    answer = set2.issubset(set1)
    print("Second set is a subset of first set - ", answer)
    if answer:
        set2.clear()
    print()

    answer = set1.issuperset(set2)
    print("First set is a subset of second set - ", answer)
    answer = set2.issuperset(set1)
    print("Second set is a subset of first set - ", answer)
    print()
    print("First set - ", set1)
    print("Second set - ", set2)


def q8(list1, dict1):
    # Iterate a given list and Check if a given element already exists
    # in a dictionary as a key’s value if not delete it from the list

    list1[:] = [item for item in list1 if item in dict1.values()]
    print(list1)

rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

def q9(dict1):
    # Given a dictionary get all values from the
    # dictionary and add it in a list but don’t add duplicates

    set1 = set(dict1.values())
    list1 = list(set1)
    print(list1)


def q10(list1):
    list1.sort()
    tup1 = tuple(set(list1))
    print("Tuple: ", tup1)
    print("Min: ", min(list1))
    print("Max: ", max(list1))

sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
q10(sampleList)

