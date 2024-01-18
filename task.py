#8.6
life ={"animals" : {"cats" : "Henry", "octopi" : "Grumpy", "emus" : "Lucy"},"plants" : {}, "others" : {}}
#8.7
for high_key in life:
    print(high_key)
#8.8

print(life["animals"].keys())
#8.9
print(life["animals"].values())
print(life["animals"]["cats"]) # 여기서는 왜 values()를 붙이면 안되는지?
#8.10
# 딕셔너리 컴프리헨션 교수님 설명

# univ = 'inha university'
# count_alphabet={letter:univ.count(letter) for letter in univ} # dictionary comprehension
# print(count_alphabet)

# univ = 'inha university'
# count_alphabet= dict()
# for letter in univ:
#     count_alphabet[letter] = univ.count(letter)
# print(count_alphabet)

#Assignment 8.10
# squares = {n:pow(n,2) for n in range(10)}
# squares = {n:n*n for n in range(10)}
squares = {n:n**2 for n in range(10)}
print(squares)
