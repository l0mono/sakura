import sys
import re

def whatch(ch):
    if re.match("[ぁ-ん]", ch):
        chartype = 0
    elif re.match("[ァ-ン]", ch):
        chartype = 1
    elif re.match("[一-龥]", ch):
        chartype = 2
    else:
        chartype = 3
    return chartype

inputtext = sys.stdin.read()

for i in range(len(inputtext)-1):
    if re.match("[。.,、]", inputtext[i]):
        continue
    print(inputtext[i], end="")
    if whatch(inputtext[i]) != whatch(inputtext[i + 1]):
        print()
