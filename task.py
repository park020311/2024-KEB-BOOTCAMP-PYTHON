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
#squares = {range(10):range(10)**2 for range(10)} # 시간이 없어서 집가서 마저 공부