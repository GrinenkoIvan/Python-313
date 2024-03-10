def func(args):
    if len(args) == 0:
        let = 0
        return let
    elif args[0] > 0:
        return func(args[1:])
    else:
        let = 1
        return let + func(args[1:])


print("n =", func([-2, 3, 8, -11, -4, 6, -1]))
