# 백준 17298

import sys
input = sys.stdin.readline

n = int(input())
answer = [0] * n
A = list(map(int, input().split()))
s = []

for i in range(n):
    while s and A[s[-1]] < A[i]:
        answer[s.pop()] = A[i]
    s.append(i)

while s:
    answer[s.pop()] = -1

# result = ""
# for i in range(n):
#     result += str(answer[i]) + " "
result = " ".join(map(str, answer)) # join을 사용하는것이 더 효과적

print(result)