#9.1
# def good():
#     print(['Harry','Ron','Hermione'])
# good()
def good() -> list:
    """
    chapter9 things to do.91
    :return: list
    """
    harry_porter = input().split()
    return harry_porter
print("input ")
print(good())
#9.2
# def get_odds(first = 0, last = 10):
# #     num =first
# #     while num < last:
# #         if(num%2==1):
# #             yield num
# #         num+=1
# # i=0
# # for x in get_odds():
# #    i+=1
# #    if i==3:
# #        print(x)
def get_odds(n) -> int:
    """
    1부터 n까지의 홀수를 발생시키는 제네레이터
    :param n:
    :return:
    """
    for i in range(1,n+1,2):
        yield i
cnt = 0
odds = get_odds(9)
for odd in odds:
    cnt = cnt + 1
    if cnt == 3:
        print(f'Third number is {odd}')
#9.3
# def test(func):
#     def new_function(*args,**kwargs):
#         print("함수호출")
#         result = func(*args,**kwargs)
#         print(result)
#         print("함수종료")
#         return result
#     return new_function
# @test
# def int_add(a,b):
#     return a+b
# int_add(3,5)
def test(f):
    """
    데코레이터 함수, 함수 시작하면 start 출력, 함수 끝나면 end 출력
    :param f: function
    :return: closure function
    """
    def test_in(*args,**kwargs):
        print('start')
        result = f(*args,**kwargs)
        print('end')
        return result
    return test_in
@test
def greeting():
    print("안녕하세요~")
greeting()
#9.4
# class OopsException(Exception):
#    pass
# try:
#     raise OopsException
# except OopsException as err:
#     print("Caught an oops")