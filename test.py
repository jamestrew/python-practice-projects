import re

emails = [
    "riya@gmail.com",
    "julia@julia.me",
    "sjulia@gmail.com",
    "julia@gmail.com",
    "samantha@gmail.com",
    "tanya@gmail.com"
]

def gmailCheck(email):
    pattern = r"[a-z]+@gmail\.com"
    return re.match(pattern, email)




lst = []
for email in emails:
    if gmailCheck(email):
        lst.append(email)

for name in sorted(lst):
    print(name[:-10])
