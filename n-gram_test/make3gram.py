import sys

inputtext = sys.stdin.read()

for char in inputtext:
    print(chr(ord(char)))