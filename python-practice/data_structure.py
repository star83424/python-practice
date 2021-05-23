def set_operation():
    a = set('abracadabra')
    b = set('alacazam')
    print(a)  # unique letters in a
    # {'a', 'r', 'b', 'c', 'd'}
    print(a - b)  # letters in a but not in b
    # {'r', 'd', 'b'}
    print(a | b)  # letters in a or b or both
    # {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
    print(a & b)  # letters in both a and b
    # {'a', 'c'}
    print(a ^ b)  # letters in a or b but not both
    # {'r', 'd', 'b', 'm', 'z', 'l'}


def zip_example():
    questions = ['name', 'quest', 'favorite color', "xxxxxx"]
    answers = ['lancelot', 'the holy grail', 'blue']
    for x, y in zip(questions, answers):
        print(x, y)


def set_of_str():
    a = set('abracadabra')
    print([x for x in a if x not in "asdfg"])
    print(tuple(x for x in a if x not in "asdfg"))
    print({x for x in a if x not in "asdfg"})


def generator():
    vec = [-4, -2, 0, 2, 4]
    gen = (x * 2 for x in vec)
    print(type(gen))
    print(type([gen]))


def tuple_example():
    tup = 111,
    print(tup)


def range_example():
    r = range(10)
    print(type(r), r.start, r.stop, r.step)


def dict_example():
    dic = {"a": 1, "b": 2, "c": 3}
    for k in dic:
        print(k)

    for k in dic.values():
        print(k)

    for k in dic.items():
        print(k, type(k))

    for k, v in dic.items():
        print(k, v)


class DataStructure:
    @staticmethod
    def main():
        # 20210524
        # generator()

        # tuple_example()

        # range_example()

        # set_of_str()

        # set_operation()

        # zip_example()

        dict_example()

