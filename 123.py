class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color
        if full is False:
                return f'Размер птицы {self.name} — {self.size}.'
        elif full is True:
            return f'Попугай {name} - заметная птица, '
            f'окрас её перьев - {color}, '
            f'а размер - {size}. Интересный факт: '
            f'попугаи чувствуют ритм, а вовсе не бездумно двигаются под музыку. '
            f'Если сменить компазицию, то и темп движений птицы изменится.'
                

class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus
        if full is False:
            return f'Размер птицы {self.name} — {self.size}.'
        elif full is True:
            return f'Размер пингвина {name} из рода {genus} - {size}. '
                   f'Интересный факт: однажды группа геологов-разведчиков '
                   f'похитила пингвинье яйцо, и их принялась преследовать вся стая, '
                   f'не пытаясь, впрочем, при этом нападать. '
                   f'Посовещавшись, похитители вернули птицам яйцо, и те отстали.'

kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

# Вызов метода у созданных объектов.
kesha.describe()
kowalski.describe(True)