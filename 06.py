def main():
    manu()

def manu():
    while True:
        x = input()
        if x == "4":
            print("退出")
            break
        else:
            if x == "1":
                a,b = map(int,input().split())
                y = (a**b)
                print(y)
            elif x == "2":
                n,m = map(int,input().split())
                if n>m:
                    x = 1
                    for i in range(n,1,-1):
                        x *= i
                    print(manu(n)/(manu(m)*manu(n-m)))
                else:
                    print("error")  
            elif x == "3":
                f = int(input()) 
                c = (f-32)*5/9
                print(c)      
main()                       
                    
