def manu():
    print("1.計算a的b次方")
    print("2.計算Cn取m")
    print("3.攝氏溫度轉華氏溫度")
    print("4.退出")
    def fun1(a,b):
        a,b = map(int,input().split())
        y = (a**b)
        return y
    def fun2(n,m):
        if n>m:
            x = 1
            for i in range(n,1,-1):
                x *= i
            print(fun2(n)/(fun2(m)*fun2(n-m)))
        else:
            print("error")  
    def fun3(f):
        f = int(input())
        c = (f-32)*5/9
        print(c)
    def fun4():
        print("退出")              