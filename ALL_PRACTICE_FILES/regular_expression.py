#!/usr/bin/env python3

import re

names = [
    "Finn Bindelle",
    'Geir Anders Berge',
    'Happy CodingRobot',
    'Ronnie  Combrige',
    'Sohill',
    'm!sha'
]

# regex = '^\w+\s+\w+$'
# for name in names:
#     result = re.search(regex, name)
#     if result:
#         print(result)

# regex = 'C\w*'
# for name in names:
#     match = re.search(regex, name)
#     if match:
#         print(name)
#         # print(match.start())
#         # print(match.end())
#         print(match.span())
#         print(match.group())

regex = '^(?P<Jay>\w+)\s+(?P<Mat>\w+)$'
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)
        print(match.group('Jay'))
        print(match.group('Mat'))
        

