import re
with open('regex_test.txt') as f:
    data = f.readlines()
#     print(data)
    
pattern = re.compile('([A-Z][\w]+)([ \w ]*)([A-Z][\w]+)')

for name in data:
    match = pattern.match(name)
    if match:
        print(match.group())
    else:
        print('None')

