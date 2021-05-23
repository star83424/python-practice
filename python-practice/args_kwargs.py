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


class ArgsKwargs:
    @staticmethod
    def main():
        kw = {'k1': 10, 'k2': 11}
        # print("------------")
        # fun(1, kw)
        # print("------------")
        # fun(1, *kw)
        # print("------------")
        # fun(1, **kw)
        # print("------------")
        # fun(1, *kw.values())

        fun_sep_kws_with_star(1, 2, kw2=4, kw1=3, kw3=5)  # 1 2 3 4
        fun_sep_kws_with_args_and_then_kwargs(1, 2, 3, 4, 5, kw1=6, kw2=7, kw3=8, kw4=9)
        fun_sep_kws_with_args_and_then_kwargs(1, 2, 3, 4, 5, kw1=6, kw3=7, kw2=8, kw4=9)
