import random

print("メッセージをどうぞ、会話を終了したい場合は「さようなら」と送信してください")
res_li =  ["ふーん、それで？","なるほど","いいですね","知らないです"]

while True:
    message = input("")
    if message == "さようなら":
        break

    print("You: ",message)
    response = random.choice(res_li)
    print("Sakura: ",response)