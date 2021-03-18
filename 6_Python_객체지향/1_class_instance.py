class User:
    # init 메소드, 특수 메소드
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    # 인스턴스 메소드 생성
    def say_hello(self):
        print("안녕하세요. 저는 {}입니다.".format(self.name))

    def login(self, my_email, my_password):
        if (self.email == my_email and self.password == my_password):
            print("로그인 성공!!")
        else:
            print("로그인 실패..")

    def check_name(self, name):
        # 파라미터로 받는 name이 유저의 이름과 같은지 boolean으로 리턴
        return self.name == name


user_1 = User("chan", "chanan_park", "12345") # User 인스턴스 생성
user_2 = User("jung", "yoonjung0106", "98765")
'''
user_1.name = "chan" # 인스턴스 변수 정의
user_1.email = "chanan_park"
user_1.password = "12345"

user_2.name = "jung"
user_2.email = "yoonjung0106"
user_2.password = "98765"
'''
print(user_1.email)
print(user_2.email)

# 두개는 동일한 기능을 함
User.say_hello(user_1)
user_2.say_hello()

user_1.login("chanan_park", "12345")
user_2.login("yoonjung0106", "9876")

print(user_1.check_name("chan"))
print(user_2.check_name("chan"))

print(user_1)
print(user_2)