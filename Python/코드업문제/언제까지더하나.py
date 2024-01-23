# 코드업 6079
n = int(input())
result=0
for i in range(1,n):
        result += i
        if result>=n:
            print(i)
            break