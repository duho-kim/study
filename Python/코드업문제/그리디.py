# 파파 파스타 가게는 점심 추천 파스타와 생과일 쥬스 세트 메뉴가 인기가 좋다.
# 이 세트 메뉴를 주문하면 그 날의 3 종류의 파스타와 2 종류의 생과일 쥬스에서 하나씩 선택한다.
# 파스타와 생과일 쥬스의 가격 합계에서 10%를 더한 금액이 대금된다.
# 어느 날의 파스타와 생과일 쥬스의 가격이 주어 졌을 때, 그 날 세트 메뉴의 대금의 최소값을 구하는 프로그램을 작성하라.

pasta = [int(input()) for _ in range(3)]
juice = [int(input()) for _ in range(2)]

minPrice = min(pasta) + min(juice)
setMenuPrice = minPrice + minPrice * 0.1

print("%.1f" % setMenuPrice)