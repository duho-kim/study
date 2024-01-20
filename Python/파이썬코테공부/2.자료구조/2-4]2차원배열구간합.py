# 백준 11660

import sys
# 표준 입력 처리속도를 크게 개선할 수 있다
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * (n+1)]
D = [[0] * (n+1) for _ in range(n+1)]

# 원본배열 생성
for i in range(n):
    A_Row = [0] + [int(x) for x in input().split()]
    A.append(A_Row)

# 합배열 생성
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 질의
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)


# # 표의 크기 N과 합을 구할 횟수 M을 입력받음
# N, M = map(int, input().split())

# # 표 데이터 입력받기
# matrix = [list(map(int, input().split())) for _ in range(N)]

# # 누적 합 배열 계산
# prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + matrix[i - 1][j - 1]

# # 쿼리 처리
# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     answer = prefix_sum[x2][y2] - prefix_sum[x2][y1 - 1] - prefix_sum[x1 - 1][y2] + prefix_sum[x1 - 1][y1 - 1]
#     print(answer)
