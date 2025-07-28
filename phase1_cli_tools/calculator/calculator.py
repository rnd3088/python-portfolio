def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "エラー：0で割れません"
    return x / y

print("電卓アプリ")
print("1. 加算\n2. 減算\n3. 乗算\n4. 除算")

choice = input("演算を選んでください（1/2/3/4）: ")

if choice not in ["1", "2", "3", "4"]:
    print("無効な入力です")
else:
    try:
        num1 = float(input("１つ目の数を入力: "))
        num2 = float(input("２つ目の数を入力: "))
    except ValueError:
        print("数値を入力して下さい")
    else:
        if choice == "1":
            print("結果:", add(num1, num2))
        elif choice == "2":
            print("結果:", subtract(num1, num2))
        elif choice == "3":
            print("結果:", multiply(num1, num2))
        elif choice == "4":
            print("結果:", divide(num1, num2))
