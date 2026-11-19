def fun1(n,m):    #C多少取多少
    x = 1
    y = 1
    q = 1
    for i in range(n,1,-1):
        x *= i
    for i in range(m,1,-1):
        y *= i
    for i in range(n-m,1,-1):
        q *= i
    return x/(y*q)

n,m = map(int,input().split())
print(fun1(n,m))            