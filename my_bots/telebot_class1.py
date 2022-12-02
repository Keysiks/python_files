import random


class Telebotgamer:
    def __init__(self):
        self.music = []
        self.i = 0
        self.capitals_answer = ''
        self.game_num_contry = 0
        self.right_capital_num = 0
        self.countryes = ['Австрия', 'Албания', 'Андорра', 'Белоруссия', 'Бельгия', 'Болгария', 'Босния', 'Ватикан',
                       'Венгрия', 'Великобритания', 'Германия', 'Греция', 'Дания', 'Ирландия', 'Исландия', 'Испания',
                       'Италия', 'Латвия', 'Литва', 'Лихтенштейн', 'Люксембург', 'Македония', 'Мальта', 'Молдавия',
                       'Монако', 'Нидерланды', 'Норвегия', 'Польша', 'Португалия', 'Румыния', 'СанМарино', 'Сербия',
                       'Словакия', 'Словения', 'Украина', 'Финляндия', 'Франция', 'Черногория', 'Чехия', 'Хорватия',
                       'Швейцария', 'Швеция', 'Эстония']

        self.country_capital = {'Австрия': 'Вена', 'Албания': 'Тирана', 'Андорра': 'АндорралаВелья',
                                'Белоруссия': 'Минск', 'Бельгия': 'Брюссель', 'Болгария': 'София', 'Босния': 'Сараево',
                                'Ватикан': 'Ватикан', 'Венгрия': 'Будапешт', 'Великобритания': 'Лондон',
                                'Германия': 'Берлин', 'Греция': 'Афины', 'Дания': 'Копенгаген', 'Ирландия': 'Дублин',
                                'Исландия': 'Рейкьявик', 'Испания': 'Мадрид', 'Италия': 'Рим', 'Латвия': 'Рига',
                                'Литва': 'Вильнюс', 'Лихтенштейн': 'Вадуц', 'Люксембург': 'Люксембург',
                                'Македония': 'Скопье', 'Мальта': 'Валлетта', 'Молдавия': 'Кишинев', 'Монако': 'Монако',
                                'Нидерланды': 'Амстердам', 'Норвегия': 'Осло', 'Польша': 'Варшава',
                                'Португалия': 'Лиссабон', 'Румыния': 'Бухарест', 'СанМарино': 'СанМарино',
                                'Сербия': 'Белград', 'Словакия': 'Братислава', 'Словения': 'Любляна', 'Украина': 'Киев',
                                'Финляндия': 'Хельсинки', 'Франция': 'Париж', 'Черногория': 'Подгорица',
                                'Чехия': 'Прага', 'Хорватия': 'Загреб', 'Швейцария': 'Берн', 'Швеция': 'Стокгольм',
                                'Эстония': 'Таллинн'}
        self.running_game_100 = True
        self.running_game_country_capital = True
        self.games = ["угадай число от 1 до 100 за 7 ходов", "black jal", "страна-столица"]
        self.number = random.randint(1, 100)
        self.mems = ['мем1.jpg', 'мем2.jpeg', 'мем3.jpeg']
        self.points_black_jak = {"v": 2, "d": 3, "k": 4, "t": 11}
        for i in range(2, 11):
            self.points_black_jak[str(i)] = i

    def get_memas(self):
        return self.mems[random.randint(0, len(self.mems) - 1)]

    def get_music(self):
        return self.mems[random.randint(0, len(self.music) - 1)]

    def game_num_100(self, ques):
        self.i += 1
        if self.running_game_100 is False:
            return 'game_end'
        elif self.i == 8:
            self.running_game_100 = False
            self.i = 0
            return 'lost'
        elif "равно" in ques:
            if int(ques.split()[1]) == self.number:
                self.running_game_100 = False
                return 'win'
            return False
        elif 'больше' in ques:
            if int(ques.split()[1]) < self.number:
                return True
            return False
        elif 'меньше' in ques:
            if int(ques.split()[1]) > self.number:
                return True
            return False

    def black_jak_game_beginning(self):
        keys = self.points_black_jak.keys()
        return [self.points_black_jak[random.choice(list(keys))] for i in range(2)]

    def black_jak_card(self):
        keys = self.points_black_jak.keys()
        return self.points_black_jak[random.choice(list(keys))]

    def get_games(self):
        return self.games

    def change_running(self):
        self.running_game_100 = True

    def game_country_capital_desk(self):
        on_desk = []
        country = self.countryes[random.randint(0, len(self.countryes) - 1)]
        answer = self.country_capital[country]
        self.capitals_answer = answer
        on_desk.append(answer)
        while len(on_desk) != 4:
            a = self.country_capital[self.countryes[random.randint(0, len(self.countryes) - 1)]]
            if a not in on_desk:
                on_desk.append(a)
        random.shuffle(on_desk)
        return [on_desk, country]

    def get_capitals_answer(self):
        return self.capitals_answer

    def black_jal_game(self):
        pass