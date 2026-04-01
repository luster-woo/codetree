class Student:
    def __init__(self, code, meeting, ti):
        self.code = code
        self.meeting = meeting
        self.ti = ti

secret_code, meeting_point, time = input().split()
time = int(time)
student1 = Student(secret_code, meeting_point,time)
print(f'secret code : {student1.code}')  # 90
print(f'meeting point : {student1.meeting}')  # 90
print(f'time : {student1.ti}')  # 90



# Please write your code here.