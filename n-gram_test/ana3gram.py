import sys
import collections
import pprint

inputtext = sys.stdin.read()

ngram = []
for i in range(len(inputtext)-2):
    ngram.append(inputtext[i:i+3])

result = collections.Counter(ngram)
pprint.pprint(result)
