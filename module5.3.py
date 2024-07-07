class House:
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
h2 = House('ЖК Акация', 20)
h1 = h1 + 10
h1 += 10
h2 = 10 + h2
print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)
print(h1 == h2) # __eq__
print(h1.name, h1.number_of_floors)
print(h1 == h2)
print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__