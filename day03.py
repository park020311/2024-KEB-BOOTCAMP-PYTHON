# # preview
# subjects = "python c++ database linux"
# print('%e' % 0.7045)
# print(subjects.isalnum())
# subject = input("수강신청과목 입력 : ")
# try:
#     print(f"해당 과목이 존재합니다. 위치는 {subjects.index(subject)}번 인덱스입니다.")
# except ValueError:
#     print('해당과목이 존재하지 않습니다')
# print('%d%%'% 100)
# print("Our cat %s weighs %s pounds" % (100,50))

# subjects = {'python': 'kim', 'c++': 'sung', 'data structure': 'kim', 'database': 'kang'}
# print("{0[python]} {0[data structure]}".format(subjects))

#prime number
number = int(input("Input number : "))
cnt = 0
i = 1
while i<=number:
    if number % i == 0:
        cnt = cnt + 1
    i= i + 1
if cnt == 2:
    print(f"{number} is prime number")
else:
    print(f"{number} is NOT prime number")







