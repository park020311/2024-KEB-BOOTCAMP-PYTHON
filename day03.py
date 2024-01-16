# course = "2024 KEB Bootcamp"
# print(course.replace('KEB','Inha'))
# print(course)
# course=course.replace('KEB','Inha')
# print(course)

course = "* KEB 2024# KEB !Bootcamp KEB....*!#"
print(course.find("KEB"))
print(course.rfind("KEB")) #r은 뒤에서부터
print(course.index("KEB"))
print(course.rindex("KEB"))
print(course.find('Inha')) # -1
print(course.index('Inha')) # ValueError: substring not found
print(course.replace('KEB','Inha', 2)) # 3번째에는 replace를 몇 번 할지 횟수이다.
print(course.strip())
print(course.strip("!#.*")) #  양쪽 끝은 연속적으로 없애지만 아닌것들은 남긴다.