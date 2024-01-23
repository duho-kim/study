def a(n, start=1):
    if start > n:
        return
    print (start)
    a(n, start+1)

n=int(input())
a(n)