def fun2(s,e):
    total=0
    for i in range(s,e+1):
        total+=i
    return total
s,e = map(int,input().split()) 
print(fun2(s,e))