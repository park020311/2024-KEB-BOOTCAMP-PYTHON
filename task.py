#8.1
e2f={"dog" : "chein","cat" : "chat","walrus" : "morse" }
print(e2f)
#8.2
print(e2f["walrus"])
#8.3
f2e=dict(e2f.items())
print(f2e)
#8.4
print(list(e2f.keys())[0])
#8.5
for eng in e2f:
    print(eng)