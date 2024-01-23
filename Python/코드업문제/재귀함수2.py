def a(n, end=1):
    if n < end:
        return
    print(n)
    a(n-1, end)

n = int(input())
a(n)