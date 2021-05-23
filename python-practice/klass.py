

class Shiba:
    pee_length = 10

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    @classmethod
    def pee(cls):
        print("pee" + "." * cls.pee_length)

    def pee(self):
        print("pee" + "." * self.pee_length)