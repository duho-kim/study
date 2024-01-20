""" distance=int(input("숫자입력 : "))

if distance >= 200:
    print("탕!")
elif distance >= 100:
    print("억")
else:
    print("슉!")
 """

bag = int(input("가방 가격 입력 : "))
watch = int(input("시계 가격 입력 : "))

total = bag+watch

if total >= 100000:
    discount = total * 0.7
    x = "30%"
elif total >= 50000:
    discount = total * 0.8
    x = "20%"
else:
    discount = total * 0.9
    x = "10%"

print("원래 금액 : "+str(total))
print(x+" 할인 후 금액"+str(discount))