# 코드업6082

n = int(input())
for i in range(1, n+1):
    temp = i
    count = 0
    while temp > 0:
        if temp % 10 == 3 or temp % 10 == 6 or temp % 10 == 9:
            count += 1
        temp //= 10

    if count > 0:
        print('X' * count, end=" ")
    else:
        print(i, end=" ")



