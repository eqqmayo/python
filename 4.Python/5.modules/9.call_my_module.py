# import mymodule

# greeting = mymodule.greet('eqqmayo')
# print(greeting)

# print(mymodule.goodbye())
# print(mymodule.default_name)

from mymodule import greet, default_name, goodbye as gb

print(greet('dongdong'))
print(default_name)
print(gb())

