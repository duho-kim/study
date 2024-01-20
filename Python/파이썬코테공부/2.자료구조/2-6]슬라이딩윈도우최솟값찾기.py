# 백준 11003
# 슬라이딩 윈도우
# 연속된 부분 배열에 대한 특정 계산 (예: 최소값, 최대값, 평균)
# 슬라이딩 윈도우와 정렬을 사용하면 될 것 같지만 범위가 커서
# 정렬 사용하면 사간복잡도가 커진다
# 덱으로 사용하면 된다?
#--------------------------------------------------------------
# 1.최소값 가능성 없는 데이터 삭제(1, 5, 2) 뒤를 기준으로 5 삭제
# 2.윈도우 크기 밖 데이터 삭제
#--------------------------------------------------------------
from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
now = list(map(int, input().split()))
mydeque = deque()

for i in range(N):
    # 현재 요소가 덱의 마지막 요소보다 작으면, 덱에서 해당요소 삭제
    # 덱이 항상 윈도우 내 최소값을 가지도록 유지하기 위함
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    # 현재요소와 인덱스를 덱에 추가
    mydeque.append((now[i],i))

    # 덱의 첫 번째 요소가 윈도우 범위를 벗어난 경우 덱에서 삭제
    if mydeque[0][1] <= i-L:
        mydeque.popleft()
    # 덱의 첫번째 요소 출력(현재 윈도우의 최소값)
    print(mydeque[0][0], end=' ')
