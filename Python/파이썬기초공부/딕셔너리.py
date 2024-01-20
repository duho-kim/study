data = {
    "result" : "승리",
    "champion" : "티모",
    "kill" : 0,
    "death" : 99,
    "assist" : 0 
}

print(data["result"])

# 딕셔너리 함수 kyes(), values(), items()

# print(data.keys())
# print(data.values())
# print(data.items())

for key in data.keys():
    print(key)
