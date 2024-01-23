# 백준 1517

# 데이터의 양이 10,000이 넘어가면 N^2으로 풀면 안된다
# 버블 정렬은 시간 복잡도가 N^2이므로 병합정렬을 사용해야 한다

# 한번에 swap에 한칸 이동

import sys
input = sys.stdin.readline


# param s : start
# param e : end
def merge_sort(s,e):
    global result
    if e-s < 1:
        return
    m = int(s+(e-s)/2)
    merge_sort(s,m)
    merge_sort(m+1,e)
    for i in range(s, e+1):
        temp[1] = A[i]

    k = s
    index1 = s
    index2 = m+1
    while index1 <=m and index2 <=e:
        if temp[index1] > temp[index2]: # 뒷그룹 데이터가 더 작을 경우
            A[k] = temp[index2]
            result += index2-k # 앞에 남아있는 데이터의 갯수
            k += 1
            index2 += 1
        else:   # 앞그룹 데이터가 더 작을 경우
            A[k] = temp[index1] 
            k += 1
            index1 += 1
    while index1 <= m:
        A[k] = temp[index1]
        k += 1
        index1 +=1
    while index2 <= e:
        A[k] = temp[index2]
        k += 1
        index2 += 1

N = int(input())
A = list(map(int, input().split()))
result = 0
A.insert(0,0) # 수열에서 1부터 시작하고 싶은데 index는 0부터 시작해서 추가함
temp = [0] * int(N+1) # 정렬할 때 잠시 사용하는 배열
merge_sort(1,N)
print(result)
