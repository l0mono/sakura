import sys
import collections
import random

def generater(chr, listdata):
    print(chr, end="")
    
    while True:
        n = random.randint(1, listdata.count(chr))
        i = 0
        for k, v in enumerate(listdata):
            if v == chr:
                i += 1
                if i >= n:
                    break
        if k + 1 >= len(listdata):
            break  
        nextchr = listdata[k + 1]
        print(nextchr, end="")
        if nextchr in ["。", "."]:
            break
        chr = nextchr
    print()


f = open("test.txt","r")
inputtext = f.read()
f.close()

listdata = list(inputtext)

print("Sakura: メッセージをどうぞ")
try:
    while True:
        inputline = input("You: ")
        startch = inputline[random.randint(0,len(inputline) - 1)]
        if not (startch in listdata):
            startch = listdata[random.randint(0,len(listdata) - 1)]
        
        print("Sakura: ",end = "")
        generater(startch,listdata)

except EOFError:
    print("Sakura: バイバイ")


