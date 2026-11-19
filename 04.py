def fun3(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x

n = int(input())
print(fun3(n))   
