animals = ["사자","호랑이","토끼"]

name = animals[0]

print(name)
print(len(animals))

animals.append("원숭이")

print(len(animals))

slicing = animals[1:3]
#오름차순
animals.sort()
#내림차순
animals.sort(reverse=True)
print(animals)

del animals[-1]
print(animals)