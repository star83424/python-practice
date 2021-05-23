"""
*args 和 **kwargs 和 * 和 key-word param 用法練習
https://skylinelimit.blogspot.com/2018/04/python-args-kwargs.html
"""


def fun(a, *args, **kwargs):
    print("a={}".format(a))
    print(args, type(args))
    print(kwargs, type(kwargs))
    for arg in args:
        print('Optional argument: {}'.format(arg))

    for k, v in kwargs.items():
        print('Optional kwargs argument key: {} value {}'.format(k, v))


def fun_sep_kws_with_star(a, b=20, *, kw1, kw2=40, kw3):
    print(a, b, kw1, kw2, kw3)


def fun_sep_kws_with_args_and_then_kwargs(a, b=20, *args, kw1, kw2=40, **kwargs):
    print(a, b, args, kw1, kw2, kwargs)

