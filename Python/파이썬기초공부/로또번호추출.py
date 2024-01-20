import random

def getRandom():
    number = random.randint(1,45)
    return number

lottoNum = []
while True:
    number = getRandom()
    if number not in lottoNum:
        lottoNum.append(number)
    if len(lottoNum)== 6:
        break

print(lottoNum)
