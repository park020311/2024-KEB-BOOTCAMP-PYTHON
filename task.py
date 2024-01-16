# 섭씨화씨 프로그램을 3번을 누르기 전까지 반복하다가 3번 누르면 탈출
while True:
    menu = input('''1. Fahrenheit -> Celsius   2. Celsius -> Fahrenheit    3. Primenumber Discrimination   4. Primenumber section  ''')
    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius :{((fahrenheit-32.0)*5.0/9.0):.4f}C')
    elif menu == "2":
        celsius = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {celsius}F, Celsius :{((celsius * 9.0 / 5.0) +32.0):.4f}C')
    elif menu == "3":
        number = int(input("Input number : "))
        is_prime = True
        if number < 1:
            print(f'{number} is prime number')
        else:
            i = 2
            while i < number:
                if number % i == 0:
                    is_prime = False
                    break
                i = i + 1
            if is_prime:
                print(f'{number} is prime number')
            else:
                print(f'{number} is NOT prime number!')
    elif menu == "4":
        numbers = input("Input First number Second number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        if n1 > n2:
            n1, n2 = n2, n1
        for number in range(n1, n2 + 1):
            is_prime = True
            if number < 2:
                pass
            else:
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(number, end=" ")
                    print()
    elif menu == "5":
        print("Quit")
        break