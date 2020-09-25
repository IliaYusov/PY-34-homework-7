class AnimalDB:

    def __init__(self):
        self.data = []

    def add_animal(self, animal_instance):
        self.data.append(animal_instance)
        return f'Успешно добавили {animal_instance.name}'
        
    def get_animal(self):
        for animal in self.data:
            yield animal

    def get_all_animals(self):
        return self.data


class Animal:
    count = 0
    sound = '*silence*'  # на случай появления на ферме рыб и черепах

    def __init__(self, name, gender=None, weight=None):
        self.name = name
        self.gender = gender
        self.weight = weight
        self.id = Animal.count  # уникальный номер каждой зверушке, в лучших традициях
        Animal.count += 1

    def eats(self, food):
        self.weight += food / 5  # с прошлого раза калорийность удвоилась

    def makes_sound(self):
        return print(self.sound)


class Bird(Animal):
    eggs = 0

    def lays_egg(self):
        if self.gender == 'F':
            self.eggs += 1
        else:
            print(f'{self.name} refuses to lay eggs. He is a boy')

    def collect_eggs(self):
        if self.eggs:
            print(f'{self.name} gives {self.eggs} egg{"s" if self.eggs > 1 else ""}')
            self.eggs = 0
        else:
            print('No eggs')


class DairyAnimal(Animal):
    milk_inside = 0

    def makes_milk(self, amount=1):
        if self.gender == 'F':
            self.milk_inside += amount
        else:
            print(f'{self.name} refuses to make milk. He is a boy')

    def milk(self):
        if self.milk_inside:
            print(f'{self.name} gives {self.milk_inside} liter{"s" if self.milk_inside > 1 else ""} of milk')
            self.milk_inside = 0
        else:
            print('No milk')        


class Goose(Bird):
    species = 'goose'
    sound = 'Honk'


class Chicken(Bird):
    species = 'chicken'

    def makes_sound(self):
        if self.gender == 'M':
            print('Cock-a-doodle-doo')
        else:
            print('Cluck')


class Duck(Bird):
    species = 'duck'
    sound = 'Quack'


class Cow(DairyAnimal):
    species = 'cow'
    sound = 'Moooo'


class Sheep(Animal):
    species = 'sheep'
    sound = 'Baaaa'
    wool = 0

    def grows_wool(self, amount=1):
        self.wool += amount

    def shear(self):
        if self.wool:
            print(f'{self.name} gives {self.wool} kilogramm{"s" if self.wool > 1 else ""} of wool')
            self.wool = 0
        else:
            print('No wool yet')


class Goat(DairyAnimal):
    species = 'goat'
    sound = 'Bleat'


animal_farm = AnimalDB()
animal_farm.add_animal(Goose('Серый', 'M', 5))
animal_farm.add_animal(Goose('Белый', 'M', 6))
animal_farm.add_animal(Cow('Манька', 'F', 500))
animal_farm.add_animal(Sheep('Барашек', 'M', 50))
animal_farm.add_animal(Chicken('Ко-Ко', 'F', 2))
animal_farm.add_animal(Chicken('Кукареку', 'M', 2))
animal_farm.add_animal(Goat('Рога', 'F', 25))
animal_farm.add_animal(Goat('Копыта', 'F', 26))
animal_farm.add_animal(Duck('Кряква', 'F', 3))

# примеры взаимодействия
for animal in animal_farm.get_animal():
    print(f'{animal.id:_<3}{animal.species:_<9}{animal.name}')

[animal.makes_sound() for animal in animal_farm.get_animal() if animal.id == 2]
[animal.makes_milk(7) for animal in animal_farm.get_animal() if animal.id == 2]
[animal.milk() for animal in animal_farm.get_animal() if animal.id == 2]

[animal.makes_sound() for animal in animal_farm.get_animal() if animal.species == 'goose']


# Задание 2
total_weight = sum(animal.weight for animal in animal_farm.get_animal())
max_weight = sorted([(animal.weight, animal.name) for animal in animal_farm.get_animal()])[-1]
print(f'Общий вес животных: {total_weight} килограмм')
print(f'Самое тяжелое животное: {max_weight[1]} - {max_weight[0]} килограмм')
