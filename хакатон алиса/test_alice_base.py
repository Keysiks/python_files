import random


class Tester:
    def __init__(self):
        self.attractions = {'11111112': 'ABABABAB',
                            '11111111': 'XYXYXYXY',
                            '11111113': 'OPOPOPOP',
                            '11111114': 'FDHSAFYD',
                            '11111115': 'FHFHFHFH',
                            '11111116': 'UIUIUIUI',
                            '11111117': 'TUTUTUTU',
                            '11111118': 'RERERERE',
                            '11111119': 'QWQWQWQW',
                            '11111120': '83idsusa'}

    def test(self):
        location = random.choice(['Центр', 'Западная поляна', "Шуист", "Тарханы", "Наровчат", "Арбеково"])
        user_id = ''.join([str(random.randint(1, 9)) for i in range(8)])
        attract_id = random.choice(list(self.attractions.keys()))
        return (user_id, attract_id, location)
