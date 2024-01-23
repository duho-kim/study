def H(a,b):
    if a>b:
        return
    if a%2!=0:
        print(a, end=' ')
    H(a+1,b)

a, b = map(int, input().split())

H(a,b)