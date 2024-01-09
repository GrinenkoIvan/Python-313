import random
initial = tuple([random.randint(0, 5) for _ in range(10)])
print(initial)
other = tuple([random.randint(-5, 0) for _ in range(10)])
print(other)
upshot = initial + other
print(upshot)
print("0 = ", upshot.count(0))
print("5 = ", upshot.count(5))
print("10 = ", upshot.count(10))
print("1 = ", upshot.count(1))
print("2 = ", upshot.count(2))
print("3 = ", upshot.count(3))