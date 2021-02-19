import os

def buy_drink():
    print("コーラ:150,コーヒー:120")
    a = (input("購入する飲みものを入力してください"))
    if a in juice:
        total_price = 0
        while True:
            try:
                b = int(input("投入金額を入力してください"))
                total_price += b
                if total_price > juice[a]:
                    print(a, "を購入しました。")
                    print("お釣りは￥", (total_price - juice[a]), "です")
                    break
                elif total_price == juice[a]:
                    print(a, "を購入しました。")
                    break
                else:
                    print(str(juice[a] - total_price), "円たりません")



            except ValueError:
                print("数値を入力してください。")
    else:
        print("該当商品がありません")



def buying_select():
    while True:
        d = input("購入を続けますか？")
        if d == answer[0]:
            os.system("cls")
            break
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
