# 백준 10986

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))

S = [0] * n
count = [0] * m

answer = 0

S[0] = A[0]

for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    count[remainder] += 1

for i in range(m):
    if count[i] > 1:
        answer += (count[i]* (count[i]-1) //2)
print(answer)


# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# A = [int(x) for x in input().split()]
# D = [0] * n
# C = [0] * m

# D[0] = A[0]
# for i in range(1, n):
#     D[i] = D[i-1] + A[i]

# C[0] = 1
# count = 0

# for i in range(n):
#     remainder = D[i] % m
#     count += C[remainder]
#     C[remainder] += 1

# print(count)
