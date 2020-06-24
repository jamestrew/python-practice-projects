topic = ["10101", "11100", "11010", "00101"]
n = len(topic)
com = []
for i in range(n - 1):
    for j in range(i + 1, n):
        l = bin(int(topic[i], 2) | int(topic[j], 2))
        com.append(l.count('1'))

print(max(com), com.count(max(com)))
