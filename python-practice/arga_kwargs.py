def fun(a, *args, **kwargs):
    print("a={}".format(a))
    print(args, type(args))
    print(kwargs, type(kwargs))
    for arg in args:
        print('Optional argument: {}'.format(arg))

    for k, v in kwargs.items():
        print('Optional kwargs argument key: {} value {}'.format(k, v))