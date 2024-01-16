#6.3    guess_me 변수에 5을 할당하고, for문을 사용하여 range(10)에서 number 변수를 사용한다.
#       number가 guess_me보다 작으면 'too low'를 출력한다. number와 guess_me가 같으면
#       'found it!'을 출력하고 반복문을 종료한다. number가 guess_me보다 크면 'oops'를 출력하고 반복문을 종료한다.
guess_me = 5
for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    elif number > guess_me:
        print("oops")
        break