#자연수 입력받고 0부터 자연수까지의 합계?

# total=0
# while total < 100:
#     number = int(input("숫자입력 : "))
#     for i in range(number+1):
#         total=i+number
#     print(total)

# print("시작")
# """ while num != -1:
#     num = int(input("종료 -1 : ")) """
# while True:
#     num = int(input("종료 -1 : "))
#     if num == -1:
#         break
# print("종료")

# menu = ["게임시작","랭킹보기","게임종료","다시 입력해 주세요"]
# while True:
#     print("[메뉴를 입력하세요]")
#     select = int(input("1. 게임시작 2. 랭킹보기 3. 게임종료>>>"))
#     if select ==1:
#         print(menu[0])
#     elif select==2:
#         print(menu[1])
#     elif select==3:
#         print(menu[2])
#         break
#     else:
#         print(menu[3])

for i in range(1,6):
    print(" "*(i-1) + "*"*(6-i))