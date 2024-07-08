class House:

    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
            else:
                print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors
        print(h1)
        print(h2)

    def __str__(self):
        return (f'Название: {name}, кол-во этажей: {number_of_floors}')
        print(len(h1))
        print(len(h2))

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __iadd__(self, other):
        return self

    def __radd__(self, other):
        return self

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# h1 = h1 + 10
# h1 += 10
# h2 = 10 + h2
# print(h1.name, h1.number_of_floors)
# print(h2.name, h2.number_of_floors)
# print(h3.name, h3.number_of_floors)
del h2
del h3
print(House.houses_history)
# print(h1 == h2) # __eq__
# print(h1.name, h1.number_of_floors)
# print(h1 == h2)
# print(h1.name, h1.number_of_floors)
# print(h2.name, h2.number_of_floors)
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__