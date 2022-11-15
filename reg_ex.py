import re

with open('regex_test.txt') as f:
    data = f.readlines()
    print(data)
    


pattern = re.compile(r'([A-Z][a-z]+) ([A-Z][a-z]+|[A-Z]+) ([A-Z][a-z]+)')




for name in data:
    match = pattern.match(name)

    if match:
        print(match.group())
    else:
        print('None')

