def calculateFine(ret, due):
    # same before or before: Fine = 0
    # same month but late: Fine = 15 * # days late
    # same year but late: Fune = 500 * # months late
    # late different year: Fine = 10000
    if ret <= due:
        return 0
    if ret[0] > due[0]:
        return 10000
    if ret[1] > due[1]:
        return 500 * (ret[1] - due[1])
    if ret[2] > due[2]:
        return 15 * (ret[2] - due[2])


ret = (2015, 6, 9)
due = (2015, 6, 6)
print(calculateFine(ret, due))
