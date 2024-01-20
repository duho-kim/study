class Dog:
    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수 초기화
        self.age = age

    def wow(self):
        print(f"내 애완견 이름은 {self.name}, 나이는 {self.age}")
# 객체 생성
my_dog = Dog("Buddy", 5)
my_dog.wow()