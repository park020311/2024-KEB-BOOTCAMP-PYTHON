# 섭씨화씨 프로그램을 3번을 누르기 전까지 반복하다가 3번 누르면 탈출
while True:
    menu = input("1. Fahrenheit -> Celsius   2. Celsius -> Fahrenheit   3. Quit program : ")
    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius :{((fahrenheit-32.0)*5.0/9.0):.4f}C')
        continue
    elif menu == "2":
        celsius = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {celsius}F, Celsius :{((celsius * 9.0 / 5.0) +32.0):.4f}C')
        continue
    elif menu == "3":
        print("Quit")
        break
