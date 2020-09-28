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
        return self.sound


class Bird(Animal):
    eggs = 0

    def lays_egg(self):
        if self.gender == 'F':
            self.eggs += 1
        else:
            return f'{self.name} refuses to lay eggs. He is a boy'

    def collect_eggs(self):
        if self.eggs:
            self.eggs, temp_eggs = 0, self.eggs
            return f'{self.name} gives {temp_eggs} egg{"s" if temp_eggs > 1 else ""}'
        else:
            return 'No eggs'


class DairyAnimal(Animal):
    milk_inside = 0

    def makes_milk(self, amount=1):
        if self.gender == 'F':
            self.milk_inside += amount
            return
        else:
            return f'{self.name} refuses to make milk. He is a boy'

    def milk(self):
        if self.milk_inside:
            self.milk_inside, temp_milk = 0, self.milk_inside
            return f'{self.name} gives {temp_milk} liter{"s" if temp_milk > 1 else ""} of milk'
        else:
            return 'No milk'


class Goose(Bird):
    species = 'goose'
    sound = 'Honk'


class Chicken(Bird):
    species = 'chicken'

    def makes_sound(self):
        if self.gender == 'M':
            return 'Cock-a-doodle-doo'
        else:
            return 'Cluck'


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
            self.wool, temp_wool = 0, self.wool
            return f'{self.name} gives {temp_wool} kilogramm{"s" if temp_wool > 1 else ""} of wool'
        else:
            return 'No wool yet'


class Goat(DairyAnimal):
    species = 'goat'
    sound = 'Bleat'


farm = AnimalDB()
farm.add_animal(Goose('Серый', 'M', 5))
farm.add_animal(Goose('Белый', 'M', 6))
farm.add_animal(Cow('Манька', 'F', 500))
farm.add_animal(Sheep('Барашек', 'M', 50))
farm.add_animal(Chicken('Ко-Ко', 'F', 2))
farm.add_animal(Chicken('Кукареку', 'M', 2))
farm.add_animal(Goat('Рога', 'F', 25))
farm.add_animal(Goat('Копыта', 'F', 26))
farm.add_animal(Duck('Кряква', 'F', 3))

# Задание 2
for animal in farm.get_animal(): #  список животных с фиксированной шириной колонок
    print(f'{animal.id:_<3}{animal.species:_<9}{animal.name}')

print()

for animal in farm.get_animal(): #  животные шумят
    print(f'{animal.species} {animal.name} says {animal.makes_sound()}')

print()

print(f'Geese list: {[animal.name for animal in farm.get_animal() if animal.species == "goose"]}') #  список всех гусей

print()

[animal.makes_milk(7) for animal in farm.get_animal() if animal.id == 2] #  корова Манька нагуливает молоко
[print(animal.milk()) for animal in farm.get_animal() if animal.id == 2] #  Маньку подоили
