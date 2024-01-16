class User :
    def __init__(self,first,last,age,gender) :
        self.first_name = first
        self.last_name = last
        self.age = age
        self.gender = gender
        self.login_attempts = 0
    def describe_user(self) :
        print(f"User name is {self.last_name}{self.first_name}")
        print(f"\nUser age is {self.age}, User gender is {self.gender}")
    def greet_user(self) :
        print("Hello!")
    def increment_login_attempts(self) :
        self.login_attempts += 1
    def reset_login_attempts(self) :
        self.login_attempts = 0
YangYifeng = User('Yifeng','Yang',23,'M')
YangYifeng.describe_user()
YangYifeng.greet_user()
YangYifeng.increment_login_attempts()
YangYifeng.increment_login_attempts()
YangYifeng.increment_login_attempts()
YangYifeng.increment_login_attempts()
print(YangYifeng.login_attempts)
YangYifeng.reset_login_attempts()
print(YangYifeng.login_attempts)