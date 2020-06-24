def simpleArraySum(ar):
    total = 0
    for num in ar:
        total += num

    return total


ar = [1, 2, 3]


def compareTriplets(a, b):
    score = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            score[0] += 1
        elif a[i] < b[i]:
            score[1] += 1
        else:
            pass
    return score


a = [17, 28, 30]
b = [99, 16, 8]


def aVeryBigSum(ar):
    total = 0
    for num in ar:
        total += num
    return total


def diagonalDifference(arr):
    rows = len(arr)
    l_r_sum = 0
    r_l_sum = 0
    for i in range(rows):
        l_r_sum += arr[i][i]
        r_l_sum += arr[i][rows - i - 1]
    return abs(l_r_sum - r_l_sum)


def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    div = len(arr)
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zer += 1

    print("%.6f" % (pos / div))
    print("%.6f" % (neg / div))
    print("%.6f" % (zer / div))


def staircase(n):
    for row in range(n):
        for num in range(n):
            if num < n - row - 1:
                print(" ", end="")
            else:
                print("#", end="")
        print()


def staircasev2(n):
    for i in range(n):
        print(" " * (n - i - 1), "#" * (i + 1))


def miniMaxSum(arr):
    count = len(arr)
    high = 0
    low = 0
    for num in range(count - 1):
        arr.sort()
        low += arr[num]
        arr.sort(reverse=True)
        high += arr[num]
    print(low, high)


def birthdayCakeCandles(arr):
    num = arr.count(max(arr))
    return num


def timeConversion(s):
    if s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:-2]
    elif s[-2:] == "AM":
        return s[:-2]
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    else:
        return str(int(s[:2]) + 12) + s[2:-2]


def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        else:
            leap = False
        leap = True
    return leap


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        print(string[i:i + len(sub_string)])
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count


def getTotalX(a, b):
    magic = 0  # counter for integers that satisfy the condition
    temp = []  # stores all ints that satisfies the first condition
    a.sort()

    # find the LCM between a
    factor = a[0]
    for i in a[1:]:
        factor = math.gcd(factor, i)
    # integer that meets first condition
    for i in range(1, int(b[0] / factor) + 1):
        for j in a:
            if (factor * i) % j != 0:
                flag = False
                break
            flag = True
        if flag:
            temp.append(factor * i)
    print(temp)
    # checks for int that meets second condition
    for i in temp:
        for j in b:
            if j % i != 0:
                flag = False
            flag = True
        if flag:
            magic += 1
    print(magic)


a = [6, 4]
b = [11, 13, 17, 19, 23]
# getTotalX(a, b)

grades = [73, 100, 38, 33]


def gradingStudents(grades):
    """ Rounds grades to the nearest 5% unless the grade is less than 38 """
    fgrades = []  # final grades

    for i in grades:
        if i >= 38 and i % 5 > 2:
            fgrades.append(i + (5 - i % 5))
        else:
            fgrades.append(i)
    return fgrades

# print(gradingStudents(grades))


def countApplesAndOranges(s, t, a, b, apples, oranges):
    """ returns number of apples and oranges landed within [s, t] """
    aCount = 0  # number of apples within [s,t]
    oCount = 0  # number of oranges within [s,t]

    # finding aCount
    for j in [a + i for i in apples]:
        if j >= s and j <= t:
            aCount += 1
    print(aCount)

    # finding oCount
    for j in [b + i for i in oranges]:
        if j >= s and j <= t:
            oCount += 1
    print(oCount)


s = 7
t = 11
a = 5
b = 15
apples = [-2, 2, 1]
oranges = [5, -6]
# countApplesAndOranges(s, t, a, b, apples, oranges)


def kangaroo(x1, v1, x2, v2):
    """ Returns True if kangaroos will reach the same position after the same number of jumps """

    if v2 == v1:
        return "NO"
    jumps = (x1 - x2) / (v2 - v1)
    if (jumps % 1) == 0 and jumps > 0:
        return "YES"
    else:
        return "NO"


x1 = 0
v1 = 3
x2 = 4
v2 = 2

# print(kangaroo(x1, v1, x2, v2))


def breakingRecords(scores):
    """ Returns the number times min and max scores are broken respectively """
    minScore = maxScore = scores[0]
    minCount = maxCount = 0

    for i in scores[1:]:
        if i < minScore:
            minCount += 1
            minScore = i
        if i > maxScore:
            maxCount += 1
            maxScore = i

    return maxCount, minCount

# print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))


def birthday(s, d, m):
    """ Returns the number ways to divide up a chocolate bar """
    ans = 0  # return integer

    for i in range(len(s)):
        sub = []  # sub array such that len(sub) == m
        j = 0
        while len(sub) < m:
            if (i + j) == len(s):
                break
            sub.append(s[i + j])
            j += 1

        if sum(sub) == d:
            ans += 1

    return ans

# print(birthday([1,2,1,3,2], 3, 2))


def birthdayv2(s, d, m):
    ans = 0
    for i in range(len(s) - m + 1):
        if (sum(s[i:i + m])) == d:
            ans += 1
    return ans

# print(birthdayv2([1,2,1,3,2], 3, 2))


def divisibleSumPairs(n, k, ar):
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                ans += 1
    return ans


n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]

# print(divisibleSumPairs(n, k, ar))


def migratoryBirds(arr):
    count = 0
    st = set(arr)
    for i in st:
        if arr.count(i) > count:
            count = arr.count(i)
            ans = i
    return ans


def dayOfProgrammer(year):
    leap = False

    if year < 1918:
        # Julian calender
        if year % 4 == 0:
            leap = True
    else:
        # Gregorian calendar
        if year % 400 == 0:
            leap = True
        elif year % 100 != 0 and year % 4 == 0:
            leap = True
    if year == 1918:
        ans = "26.09.1918"
    elif leap:
        ans = "12.09." + str(year)
    else:
        ans = "13.09." + str(year)

    return ans


def bonAppetit(bill, k, b):
    bill.pop(k)
    actual = sum(bill)

    if b == actual / 2:
        print("Bon Appetit")
    else:
        print(int(b - actual / 2))


def sockMerchant(n, ar):
    from collections import Counter

    ans = 0
    socks = Counter(ar)
    for k in socks:
        ans += socks.get(k) // 2
    return ans


def pageCount(n, p):
    return min(p // 2, n // 2 - p // 2)


def countingValleys(n, s):
    alt = 0  # altitude below sea level
    count = 0
    for i in s:
        if i == "D":
            alt -= 1
        else:
            alt += 1

        if alt == 0 and i == "U":
            count += 1
    return count


def getMoneySpent(keyboards, drives, b):
    options = []
    for i in keyboards:
        options += [(i + j) for j in drives if (i + j) <= b]

    if options == []:
        return -1
    else:
        return max(options)


a = [1, 2, 2, 3, 1, 2]


def pickingNumbers(a):
    a.sort()
    n = len(a)
    ans = 0
    for i in range(n):
        check = [a[j] for j in range(i, n) if abs(a[i] - a[j]) <= 1]
        if len(check) > ans:
            ans = len(check)
    print(ans)


def pickingNumbersv2(a):
    from collections import Counter
    c = Counter(a)
    ans = 0
    for i in range(max(a) + 1):
        ans = max(c[i] + c[i + 1], ans)
    print(ans)


def designerPdfViewer(h, word):
    st = "abcdefghijklmnopqrstuvwxyz"
    height = 0
    for i in word:
        for j in st:
            if i == j:
                height = max(h[st.index(j)], height)

    return height * len(word)


h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = "zaba"


def viralAdvertising(n):
    likes = ans = 2

    for i in range(n - 1):
        shares = likes * 3
        likes = math.floor(shares / 2)
        ans += likes
    return ans


def circularArrayRotation(a, k):
    m = len(a)
    a = a[(m - k) % m:] + a[0:(m - k) % m]
    print(a)


def swap_case(s):
    # three ways
    print(s.swapcase())
    print(''.join([i.lower() if i.isupper() else i.upper() for i in s]))
    new = ''
    for i in s:
        if i.isupper():
            new += ''.join(i.lower())
        else:
            new += ''.join(i.upper())
    print(new)


def print_rangoliOG(size):
    dim = size * 4 - 3
    alpha = "abcdefghijklmnopqrstuvwxyz"[0:size]
    items = list(range(size))
    items = items[:-1] + items[::-1]

    for i in items:
        row = alpha[-(i + 1):]
        row = row[::-1] + row[1:]
        print('-'.join(row).center(dim, '-'))


def print_rangoli(size):
    n = size
    import string
    alpha = string.ascii_lowercase
    result = []
    for i in range(n):
        pattern = "-".join(alpha[i:n])
        pattern = pattern[::-1] + pattern[1:]
        result.append(pattern.center(4 * n - 3, '-'))
    print('\n'.join(result[::-1] + result[1:]))


def solve(s):
    for name in s.split():
        print(name)
        s = s.replace(name, name.capitalize())
    return s


def minion_game(string):
    vowels = "AEIOU"

    s_score = 0
    k_score = 0
    score = len(string)
    for i in range(score):
        if string[i] in vowels:
            k_score += score - i
        else:
            s_score += score - i

    if s_score > k_score:
        print("Stuart", s_score)
    elif s_score < k_score:
        print("Kevin", k_score)
    else:
        print("Draw")


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub = string[i:i + k]  # subsegment ti
        ans = ''.join(dict.fromkeys(sub))
        print(ans)


def climbingLeaderboard(scores, alice):
    scores = list(dict.fromkeys(scores))
    slen = len(scores)

    new_scores = []
    for score in alice:
        if score < scores[-1]:
            new_scores.append(slen + 1)
        elif score > scores[0]:
            new_scores.append(1)
        else:
            new_scores.append(binSearch(scores, score, slen))
    return new_scores


def binSearch(scores, score, slen):
    start = 0
    end = slen

    while True:
        mid = start + (end - start) // 2

        # exit conditions
        if scores[mid] == score:
            return mid + 1
        elif scores[mid] > score and scores[mid + 1] < score:
            return mid + 2
        elif scores[mid] < score and scores[mid - 1] > score:
            return mid + 1

        if score < scores[mid]:
            start = mid + 1
        else:
            end = mid - 1


scores = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]


def permutationEquation(p):
    n = len(p)
    px = []
    py = []
    for i in range(1, n + 1):
        px.append(p.index(i) + 1)
    for j in px:
        py.append(p.index(j) + 1)
    return py


def jumpingOnClouds(c, k):
    i = 0
    n = len(c)
    e = 100
    while True:
        e -= 1
        i = (i + k) % n
        print(i)
        if c[i] == 1:
            e -= 2
        if i == 0:
            return e


def appendAndDelete(s, t, k):
    while k > 0:
        if s == t[:len(s)] and len(t) - len(s) == k or len(s) == 0:
            break
        s = s[:-1]
        k -= 1
    return "Yes" if len(t) - len(s) <= k else "No"


def binMaxConsecutive(n):
    b = bin(n)[2:].split('0')
    l = [len(i) for i in b]
    print(max(l))


def companyLogo():
    from collections import Counter
    s = 'aabbbddcce'
    c = Counter(sorted(s))
    lst = c.most_common


def calendar():
    import calendar
    print(calendar.TextCalendar(firstweekday=6).formatyear(2020))


def time_delta(t1, t2):
    from datetime import datetime
    fmt = '%a %d %b %Y %H:%M:%S %z'
    delta = abs(datetime.strptime(t1, fmt) - datetime.strptime(t2, fmt))
    print(str(delta.total_seconds()))


t1 = "Sat 02 May 2015 19:54:36 +0530"
t2 = "Fri 01 May 2015 13:54:36 -0000"


def anyOrAll(s):
    ans_1 = [i > 0 for i in s]
    ans_2 = [str(i) == str(i)[::-1] for i in s]

    if all(ans_1) and any(ans_2):
        print(True)
    else:
        print(False)


def fibonacci(n):
    # return a list of fibonacci numbers
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]


def fun(s):
    # return True if s is a valid email, else return False
    try:
        username = s.split('@')
        domain, ext = username[1].split('.')
    except:
        return False
    else:
        print(s)
        if username[0] == '' or domain == '':
            return False
        usercheck = [i.isalnum() or i == '_' or i == '-' for i in username[0]]
        domaincheck = [i.isalnum() for i in domain]
        extcheck = True if len(ext) <= 3 else False
        checks = usercheck + domaincheck
        checks.append(extcheck)
        print("user", usercheck)
        print("domain", domaincheck)
        print("ext", extcheck)
        return all(checks)


def twoDArray(arr):
    sums = []
    for i in range(4):
        for j in range(4):
            print(i, j)
            print(arr[i][j:j + 3])
            sums.append(sum(arr[i][j:j + 3]) + sum(arr[i + 2][j:j + 3]) + arr[i + 1][j + 1])

    print(sums)
    print(max(sums))


arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]]


def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    if y1 == y2:
        if m1 > m2:
            return 500 * (m1 - m2)
        elif m1 == m2 and d1 >= d2:
            return 15 * (d1 - d2)
    return 0

def cutTheSticks(arr):

    arr.sort()
    loc = 0
    for i, l in enumerate(arr):
        print(arr)
        if l != loc:
            print(str(len(arr) - i))
            loc = l


def calculate(*scores):
    print(*scores)
    print(sum(scores))
    print(len(scores))
    score = sum(scores) / len(scores)
    print(score)


def printBoard(arr):
    for row in arr:
        print(' '.join(map(str, row)))


def magicCost(magic, s):
    cost = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != magic[i][j]:
                cost += abs(s[i][j] - magic[i][j])
    return cost


def formingMagicSquares():
    magic = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    costs = []

    for i in range(4):
        for i in range(3):
            for j in range(3):
                if i == j:
                    break
                temp = magic[i][j]
                magic[i][j] = magic[j][i]
                magic[j][i] = temp
        costs.append(magicCost(magic, s))

        for i in range(3):
            temp = magic[i][0]
            magic[i][0] = magic[i][2]
            magic[i][2] = temp
        costs.append(magicCost(magic, s))

    print(min(costs))


def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i < len(c) - 1:
        jumps += 1
        if i + 2 < len(c) and c[i + 2] == 1:
            i += 1
        else:
            i += 2
    return jumps


def equalizeArray(arr):
    from collections import Counter
    c = Counter(arr)
    print(c)
    ans = 0
    high = c.most_common(1)[0][0]
    print(high)
    for k, v in c.items():
        if k == high:
            pass
        else:
            ans += v
    return ans


def queensAttack(n, k, r_q, c_q, obstacles):
    ans = 0

    """ first, calculate # of moves without blockers """
    left = (c_q - 1)
    down = (r_q - 1)
    right = (n - c_q)
    up = (n - r_q)
    l_d = min(left, down)
    r_d = min(right, down)
    l_u = min(left, up)
    r_u = min(right, up)

    """ calculates # moves with blockers """
    for ob in obstacles:
        if ob[0] == r_q:  # obstacle in same row
            if ob[1] > c_q:  # right
                right = min(right, right - (n - ob[1]) - 1)
            else:  # left
                left = min(left, left - ob[1])
        elif ob[1] == c_q:  # obstacle in same col
            if ob[0] > r_q:  # above
                up = min(up, up - (n - ob[0]) - 1)
            else:
                down = min(down, down - ob[0])
        elif abs(ob[0] - r_q) == abs(ob[1] - c_q):  # obstacle in diagonals
            if ob[0] > r_q and ob[1] > c_q:  # up, right
                r_u = min(r_u, (ob[0] - r_q) - 1)
            elif ob[0] > r_q and ob[1] < c_q:  # up, left
                l_u = min(l_u, (ob[0] - r_q) - 1)
            elif ob[0] < r_q and ob[1] > c_q:  # down, right
                r_d = min(r_d, (r_q - ob[0]) - 1)
            else:  # down, left
                l_d = min(l_d, (r_q - ob[0]) - 1)

    ans = left + down + right + up + l_u + l_d + r_u + r_d
    return ans


def acmTeam(topic):
    """
    On the first line, print the maximum number of topics a 2-person team can know.
    On the second line, print the number of ways to form a 2-person team that knows the maximum number of topics.
    """
    from itertools import combinations

    combs = list(combinations(topic, 2))
    scores = []
    for comb in combs:
        know = 0
        for i in range(len(comb[0])):
            if comb[0][i] == '1' or comb[1][i] == '1':
                know += 1
        scores.append(know)
    arr = [max(scores), scores.count(max(scores))]

    return arr


class Calculator():
    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return n**p


def biggerIsGreater(w):
    w = list(w)

    p_index = -1
    for i in range(len(w) - 1, 0, -1):
        if w[i] > w[i - 1]:
            p_index = i - 1
            p_value = w[i - 1]
            break

    if p_index < 0:
        return "no answer"

    for i in range(len(w) - 1, 0, -1):
        if w[i] > p_value:
            w[p_index] = w[i]
            w[i] = p_value
            break

    ans = w[:p_index + 1] + w[len(w) - 1:p_index: -1]
    return ''.join(ans)


def readfiles():
    with open("test.txt") as f:
        inputs = f.readlines()

    for i in inputs[1:]:
        print(i.rstrip() + ' --> ' + biggerIsGreater(i.rstrip()))


readfiles()
# test
