#import random
import random

class OopsException(Exception):
    pass

# numbers = list()
# for i in range(5):
#     numbers.append(random.randint(1,100))
numbers = [random.randint(1,100) for i in range(5)]
print(numbers)
try:
    pick = int(input(f"Input index (0~{len(numbers)-1}) : "))
    print(numbers[pick]) # numbers는 총 0~4 까지 할당되었기 때문에 5 이상을 입력하면 에러
    raise OopsException("Oops")
except IndexError as err:
    print(f"Out of range : Wrong index number\n{err}")
except ValueError as err:
    print(f"Input Only Number !\n{err}")
# except OopsException as err:
#     print(f"Oops Oops {err}")
except Exception as err:
    print(f"Error occurs\n{err}")
else:
    print(f"program terminate")