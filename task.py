#6.2    guess_me 변수에 7을 할당하고, number 변수에 1을 할당한다. number와 guess_me를 비교하는 while문을 작성해보자.
#       number가 guess_me보다 작으면 'too low'를 출력한다. number와 guess_me가 같으면 'found it!'을 출력하고 반복문을 종료한다.
#       number가 guess_me보다 크면 'oops'를 출력하고 반복문을 종료한다. 그리고 반복문의 마지막에 number을 1씩 증가시킨다.
#       문제는 이거인데 원래꺼는 주석처리하고 quess_me를 처음 한번 입력하고 number를 계속 입력해 맞추는 방식으로 문제 변경해보기!
# guess_me = 7
# number = 1
# while True:
#     if number < guess_me:
#         print("too low")
#     elif number == guess_me:
#         print("found it!")
#         break
#     elif number > guess_me:
#         print("oops")
#         break
#     number = number + 1

guess_me = int(input("맞춰야 할 대상을 입력하세요. (최초 1번)"))
while True:
    number = int(input("누구게? "))
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    elif number > guess_me:
        print("too upper")