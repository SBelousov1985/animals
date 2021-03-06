import random


class Animals:
    age_hours = 0
    weight = 0  # kg
    hunger = 0
    sex = True  # True - female, False - male

    def __init__(self, age=0, weight=0, sex=None):
        self.age_hours = age * 365 * 24
        if weight == 0:
            self.weight = self.get_random_weight()
        else:
            self.weight = weight
        if sex is None:
            self.sex = bool(random.randint(0, 1))
        else:
            self.sex = sex

    def __gt__(self, other):
        return self.age_hours > other.age_hours

    def __ge__(self, other):
        return self.age_hours >= other.age_hours

    def get_random_weight(self):
        return random.randint(10, 1000000) / 100

    def eat(self, hunger_pt):
        self.hunger -= hunger_pt
        if self.hunger < 0:
            self.hunger = 0

    def voice(self):
        raise NotImplementedError('Определите voice в классе %s.' % self.__class__.__name__)

    def live(self, hours, weight_pt=0):
        self.age_hours += hours
        self.weight += weight_pt

    def get_age(self):
        return round(self.age_hours / 24 / 365, 2)


class Ungulates(Animals):
    _artiodactyls = False

    def is_artiodactyls(self):
        return self._artiodactyls

    def get_random_weight(self):
        return random.randint(1000, 350000) / 100

    def voice(self):
        return super().voice()


class Cow(Ungulates):
    _artiodactyls = True

    def __add__(self, other):
        if self.sex + other.sex == 1:
            return Cow()

    def get_random_weight(self):
        return random.randint(2000, 100000) / 100

    def voice(self):
        return "moo"


class Goat(Ungulates):
    _artiodactyls = True

    def __add__(self, other):
        if self.sex + other.sex == 1:
            return Goat()

    def get_random_weight(self):
        return random.randint(1000, 20000) / 100

    def voice(self):
        return "baaaaah"


class Sheep(Ungulates):
    _artiodactyls = True

    def __add__(self, other):
        if self.sex + other.sex == 1:
            return Sheep()

    def get_random_weight(self):
        return random.randint(1000, 20000) / 100

    def voice(self):
        return "baaaaah"


class Pigs(Ungulates):
    _artiodactyls = True

    def __add__(self, other):
        if self.sex + other.sex == 1:
            return Pigs()

    def get_random_weight(self):
        return random.randint(1000, 20000) / 100

    def voice(self):
        result = []
        for i in range(random.randint(1, 3)):
            result.append("oink")
        return " ".join(result)


class Birds(Animals):
    _waterfowl = False
    able_to_fly = True

    def is_waterfowl(self):
        return self._waterfowl

    def get_random_weight(self):
        return random.randint(0.1, 15000) / 100

    def voice(self):
        return super().voice()


class Duck(Birds):
    _waterfowl = True

    def __add__(self, other):
        if self.sex + other.sex == 1:
            return Duck()

    def get_random_weight(self):
        return random.randint(10, 1000) / 100

    def voice(self):
        result = []
        for i in range(random.randint(1, 3)):
            result.append("quack")
        return "-".join(result)


class Chicken(Birds):
    able_to_fly = False

    def __add__(self, other):
        if self.sex + other.sex == 1:
            return Chicken()

    def get_random_weight(self):
        return random.randint(50, 500) / 100

    def voice(self):
        result = []
        for i in range(random.randint(1, 3)):
            result.append("cluck")
        return "-".join(result)


class Goose(Birds):
    _waterfowl = True

    def __add__(self, other):
        if self.sex + other.sex == 1:
            return Goose()

    def get_random_weight(self):
        return random.randint(10, 1000) / 100

    def voice(self):
        return "honk"


cow1 = Cow()
cow2 = Cow(3)

pig1 = Pigs(4, 3, True)
pig2 = Pigs(3, 5, False)
pig3 = pig1 + pig2

duck1 = Duck()
duck2 = Duck()
