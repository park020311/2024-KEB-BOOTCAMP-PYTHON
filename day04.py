# #리스트
# li=list()
# print(li)
# print(list('cat'))
# print(list(('ready', 'fire', 'aim')))
subjects = ["데이터베이스","c++","5","Java","Python","Java","9","리눅스"]
print(subjects[::-1])
print(subjects)
#subjects.reverse()
# subjects.sort(reverse = False)
copy_subjects = sorted(subjects)
print(subjects)
print(copy_subjects)
#subjects.remove("Java") # remove는 앞에 있는걸 삭제
#del subjects[2] # del은 원하는 위치에 있는걸 삭제 가능

number = [1,2,3,4]
number[1:3]=[10,20,30]
print(number)