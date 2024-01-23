# 코드업6098
import sys
input = sys.stdin.readline

# 갈수있는곳:0, 벽:1, 먹이:2
# 오른쪽 또는 아래로만 이동
# 2,2에서 먹이까지 이동경로 예상
a = [list(map(int, input().split())) 
     for _ in range(10)]

x = 1
y = 1
while True:
    if a[x][y+1] != 1:
        a[x][y] = 9
        y += 1
    elif a[x][y] != 1:
        a[x][y] = 9
        x += 1
    else:
        break
    if a[x][y] == 2:
        a[x][y] = 9
        break
for i in range(10):
    for j in range(10):
        print(a[i][j], end=' ')
    print()

