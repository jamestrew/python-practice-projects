import csv
import json
import random

# get random first name
# get random last name
# get random occupation
# get random age

first_names = json.loads(open('first_names.json').read())
last_names = json.loads(open('last_names.json').read())
occupation = json.loads(open('occupations.json').read())

with open('people.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(1, 30):
        id_ = i
        first = random.choice(first_names)
        last = random.choice(last_names)
        job = random.choice(occupation)
        age = random.randint(21, 67)

        writer.writerow([id_, first, last, job, age])
