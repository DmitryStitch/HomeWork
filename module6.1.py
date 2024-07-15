class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Predator(Animal):
    def eat(self,food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Flower(Plant):
    def eat(food):
        pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


Lion = Predator('Лев')
Rat = Mammal('Крыса')
Rose = Flower('Роза')
Apple = Fruit('Яблоко')

print(Lion.name)
print(Rose.name)

print(Lion.alive)
print(Rat.fed)
Lion.eat(Rose)
Rat.eat(Apple)
print(Lion.alive)
print(Rat.fed)

