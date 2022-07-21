def f():
    x=42
def g():
    global x
    x=43
    print("Before calling: ",x)
f()
print("After calling: ",x)
g()
print("x in main: ",x)

                        
