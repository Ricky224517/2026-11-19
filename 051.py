def fun3(n):      
    x = 1
    for i in range(n,1,-1):
        x *= i
    return x

n,m = map(int,input().split())
print(fun3(n)/(fun3(m)*fun3(n-m)))