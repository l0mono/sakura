import sys
import re

inputtext = sys.stdin.read()

outputtext = inputtext.replace("¥n","")
outputtext = re.sub("《.+?》","",outputtext)
outputtext = re.sub("|","",outputtext)
outputtext = re.sub("[#.+?]","",outputtext)

print(outputtext)