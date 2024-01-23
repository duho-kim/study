# 코드업6095
baduk = [[0]*19 for _ in range(19)]
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    baduk[x-1][y-1] = 1

for i in baduk:
    for j in i:
        print(j, end=' ')
    print()
