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

Dom = House('ЖК Эльбрус', 30)
print(Dom.name, Dom.number_of_floors)
Dom.go_to(5)
Dom.go_to(42)
