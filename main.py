import random


class Human:
    def __init__(self, name='Human', job=None, home=None, car=None, wifename='Human', happiness=0, child=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.wife = wifename
        self.happiness = happiness
        self.child = child

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_home(self):
        self.home = House()

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness
        self.satiety -= 5

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 50
            self.car.fuel += 100
        elif manage == 'food':
            print('Bought food')
            self.money -= 20
            self.home.food += 20
        elif manage == 'delicacies':
            print('Happy')
            self.money -= 20
            self.satiety += 5
            self.gladness += 2

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        self.money -= 50

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 100

    def get_family(self):
        if self.fm is True:
            self.name_w = random.choice(list(name_list))
            self.fm = family_list[self.wife]['name']
            self.child = random.choice(list(child_list))
            self.child_name = family_list[self.child]['child_name']
            if self.child.child_name == 1 or 3:
                True
            if self.child.child_name == 2 or 4:
                False
        if self.fm is False:
            print('Unhappy...')
            return False

    def days_indexes(self, day):
        day = f"Today the {day} of {self.name}'s life"
        print(f'{day:=^50}')
        human_indexes = self.name + "'s indexes"
        print(f'{human_indexes:-^50}')
        print(f'Money = {self.money}')
        print(f'Satiety = {self.satiety}')
        print(f'Gladness = {self.gladness}')

        home_indexes = 'Home indexes'
        print(f'{home_indexes:-^50}')
        print(f'Food = {self.home.food}')
        print(f'Mess = {self.home.mess}')

        car_indexes = f"{self.car.brand} car indexes"
        print(f'{car_indexes:-^50}')
        print(f'Fuel = {self.car.fuel}')
        print(f'Strength = {self.car.strength}')

        family_indexes = f"Family indexes"
        print(f'{family_indexes:-^50}')
        print(f'Wife = {self.wife.name}')
        if self.child.childname is True:
            print(f'Child gender = Male')
        if self.child.childname is False:
            print(f'Child gender = Female')
        print(f'Child name = {self.child.child_name}')


    def is_alive(self):
        if self.gladness < 0:
            print('Depression...')
            return False
        if self.satiety < 0:
            print('Dead....')
            return False
        if self.money < -500:
            print('Bankrupt...')
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print('Settled in the home')
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't a job, going to get a job {self.job.job}"
                  f"with salary {self.job.salary}")
        self.days_indexes(day)
        if self.satiety < 20:
            print('Time eat')
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 10:
                print('I clean home')
                self.clean_home()
            else:
                print("Time chill")
                self.chill()
        elif self.money < 5:
            print('Time work')
            self.work()
        elif self.car.strength < 10:
            print('I need to repair my car')
            self.to_repair()
        dice = random.randint(1, 4)
        if dice == 1:
            print("Let's go chill")
            self.chill()
        elif dice == 2:
            print('Start working')
            self.work()
        elif dice == 3:
            print('Cleaning time!')
            self.clean_home()
        elif dice == 4:
            print('Time fo treats')
            self.shopping(manage='delicacies')


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= 10
            self.strength -= 1
            return True
        else:
            print('The car cannot move')
            return False


class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness = job_list[self.job]['job_gladness']

class Family:
    def __init__(self, family_list):
        self.family = random.choice(list(family_list))
        self.fm = family_list[self.happiness]['index']
        if self.fm is True:
          self.name_w = random.choice(list(name_list))
          self.fm = family_list[self.wife]['name']
          self.child = random.choice(list(child_list))
          self.child_name = family_list[self.child]['child_name']
          if self.child.child_name == 1 or 3:
            True
          if self.child.child_name == 2 or 4:
            False
        if self.fm is False:
            print('Unhappy...')
            return False




job_list = {'C++': {'salary': 90, 'job_gladness': 3},
            'Python': {'salary': 50, 'job_gladness': 10},
            'Java': {'salary': 70, 'job_gladness': 7},
            'PHP': {'salary': 40, 'job_gladness': 5}}

brands_of_car = {"BMW": {'fuel': 100, 'strength': 100, 'consumption': 6},
                 "Lada": {'fuel': 50, 'strength': 30, 'consumption': 9},
                 "Ford": {'fuel': 80, 'strength': 150, 'consumption': 8},
                 "Audi": {'fuel': 70, 'strength': 120, 'consumption': 7}}

family_list = {'1': {'index': True},
            '2': {'index': False}}

name_list = {"Anna": {'name': 1},
            "Lubov'": {'name': 2},
            "Angelina": {'name': 3},
            "Sofia": {'name': 4}}

child_list = {"Maxim": {'childname': 1},
            "Lubov'": {'childname': 2},
            "Kirill": {'childname': 3},
            "Sofia": {'childname': 4}}

nick = Human(name='Nick')
for day in range(1, 8):
    if nick.live(day) == False:
        break
