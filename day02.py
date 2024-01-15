# first_number = int(input("first number : "))
# second_number=int(input("second number : "))
#
# quotient = first_number // second_number
# remainder = first_number % second_number
# print(f'목은 {quotient} 나머지는 {remainder}입니다')

first_number = int(input("first number : "))
second_number=int(input("second number : "))

print(f'몫은 {divmod(first_number, second_number)[0]} 나머지는 {divmod(first_number, second_number)[1]}입니다')