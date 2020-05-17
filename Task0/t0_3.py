from datetime import datetime
from functools import total_ordering


@total_ordering
class Hours:
    """ Значение Часа для текущего времени. """
    hours = datetime.now().hour

    def __eq__(self, other):
        return self.hours == other.hours

    def __lt__(self, other):
        return self.hours < other.hours

    def __str__(self):
        return f'Количество часов: {self.hours}'

@total_ordering
class Minutes:
    """ Значиние Минут для текущего времени. """
    minutes = datetime.now().minute

    def __eq__(self, other):
        return self.minutes == other.minutes

    def __lt__(self, other):
        return self.minutes < other.minutes

    def __str__(self):
        return f'Количество минут: {self.minutes}'

@total_ordering
class Day(Hours, Minutes):

    def show_current_time(self):
        """ Выводит текущее время в 24 часовом формате. """
        print(f'{self.hours}:{self.minutes}')

    @staticmethod
    def get_day_time():
        """ Выводит текущее время суток. """
        day_parts = {
            'Утро': (6, 11),
            'День': (11, 17),
            'Вечер': (17, 22),
            'Ночь': (22, 6)
        }
        time = Day().hours * 60 + Day().minutes
        for key, values in day_parts.items():
            if values[0] * 60 < time <= values[1] * 60:
                return key
            else:
                return 'Ночь'

    def __str__(self):
        return f'Точное время: \n{self.hours}:{self.minutes}'

if __name__ == '__main__':
    day_of_time = Day()
    day_of_time.show_current_time()
    print(day_of_time.get_day_time())

