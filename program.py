import os

def buy_drink():
    print("コーラ:150,コーヒー:120")
    a = (input("購入する飲みものを入力してください"))
    if a in juice:
        while True:
            try:
                b = int(input("投入金額を入力してください"))
                if b > juice[a]:
                    print(a, "を購入しました。")
                    print("お釣りは￥", (b - juice[a]), "です")
                    break
                elif b == juice[a]:
                    print(a, "を購入しました。")
                    break
                else:
                    print("投入金額が不足しています")
            except ValueError:
                print("数値を入力してください。")
    else:
        print("該当商品がありません")

def buying_select():
    d = input("購入を続けますか？")
    if d == answer[0]:
        os.system("cls")
    elif d == answer[1]:
        return "END"
    else:
        print("yesかnoを入力してください。")

juice = {"コーラ":150,"コーヒー":120}
answer = ["yes","no"]
endflag = None

while endflag == None:
    buy_drink()
    endflag = buying_select()
print("お疲れ様でした。")
