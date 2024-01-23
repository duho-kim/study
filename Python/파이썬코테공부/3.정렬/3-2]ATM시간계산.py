# 백준 11399

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = [0] * N # A의 합배열

# 삽입정렬
for i in range(1,N):
    insert_point = i # 현재 인덱스 만듦
    insert_value = A[i] # 현재 값
    for j in range(i-1, -1, -1):
        if A[j] <A[i]:
            insert_point = j+1
            break
        if j == 0:
            insert_point = 0

    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    A[insert_point] = insert_value

# 합배열
S[0] = A[0]
for i in range(1,N):
    S[i] = S[i-1] + A[i]

# 합배열 모두 더하기
sum = 0
for i in range(N):
    sum += S[i]

print(sum)