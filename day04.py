#튜플
t1 = (5) # 튜플은 쉼표가 들어가야함
t2 = 5,
t3 = (5,)
t4 = (5,7)
t5 = 5,7
t6 = "python", "kim" # packing
print(type(t1))
print(type(t2))
print(type(t3))
print(type(t4))
print(type(t5))
print(type(t6),t6[1])
subject, prof = t6 # unpacking # 주의점 언패킹할 때 좌변과 우변의 개수가 같아야함
                               # (t6를 예시로 하면 python , kim2개니까 subject, prof 2개로 받아야함)
print(subject)
print(prof)
t7 = ()
t8 = (tuple())
print(type(t7)) #공백은 예외로 쉼표 없어도 튜플
print(type(t8))
print(type(9,), type((9,)))
t9 = 1, 2, 3
t10 = 1, 2, 2, 1
print(t9 == t10)
print(t9 < t10)
print(t9 > t10)
t11 = 4.43,
t12 = 3.97, 4.1, 3.27
print(id(t11))
t11 += t12
print(t11)
print(id(t11)) # 할당받고 나서는 주소가 달라짐