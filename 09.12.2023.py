from random import randint
tpl1 = tuple(randint(0, 5) for i in range(10))
print(tpl1)
tpl2 = tuple(randint(-5, 0) for x in range(10))
print(tpl2)
tpl3 = tuple(tpl1 + tpl2)
print(tpl3)
print("0 =", tpl3.count(0))
