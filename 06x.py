def manu():
    print("1.計算a的b次方")
    print("2.計算Cn取m")
    print("3.攝氏溫度轉華氏溫度")
    print("4.退出")


def fun1(a, b):
    return a ** b


def factorial(n):
    x = 1
    for i in range(n, 1, -1):
        x *= i
    return x


def fun2(n, m):
    if n >= m:
        return factorial(n) // (factorial(m) * factorial(n - m))
    return "error"


def fun3(c):
    return c * 9 / 5 + 32


def fun4():
    print("退出")


def main():
    while True:
        manu()
        x = input("請選擇功能：")
        if x == "1":
            a, b = map(int, input("輸入 a b：").split())
            print(fun1(a, b))
        elif x == "2":
            n, m = map(int, input("輸入 n m：").split())
            print(fun2(n, m))
        elif x == "3":
            c = float(input("輸入攝氏溫度："))
            print(fun3(c))
        elif x == "4":
            fun4()
            break
        else:
            print("請輸入 1~4")


main()