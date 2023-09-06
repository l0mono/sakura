import random

print("メッセージをどうぞ、会話を終了したい場合は「さようなら」と送信してください")
res_li =  ["ふーん、それで？","なるほど","いいですね","知らないです"]

try:
    while True:
        inputline = input("あなた: ")
        if inputline == "さようなら":
            break
        
        response = random.choice(res_li)
        print("Sakura: ",response)

except EOFError:
    print("Sakura: バイバイ〜！")