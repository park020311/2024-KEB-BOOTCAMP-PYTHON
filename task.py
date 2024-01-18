#9.1
def good():
    print(['Harry','Ron','Hermione'])
good()
#9.2
def get_odds(first = 0, last = 10):
    num =first
    while num < last:
        if(num%2==1):
            yield num
        num+=1
i=0
for x in get_odds():
   i+=1
   if i==3:
       print(x)
#9.3
def test(func):
    def new_function(*args,**kwargs):
        print("함수호출")
        result = func(*args,**kwargs)
        print(result)
        print("함수종료")
        return result
    return new_function
@test
def int_add(a,b):
    return a+b
int_add(3,5)
#9.4
class OopsException(Exception):
   pass
try:
    raise OopsException
except OopsException as err:
    print("Caught an oops")