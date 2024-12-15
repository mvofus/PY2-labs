"""
Пример:
>>> car = Car("RED", 100, 50, 1)
>>> car.calculate_occupied_volume(1)
49
"""
from typing import Union

class Film:
    """
    Документация на класс.
    Класс описывает страницу фильма на стримминговом сервисе.
    """
    def __init__(self, title: str, running_time_min: int, rating: float):
        """
        Инициализация экземпляра класса.
        :param title: Название фильма
        :param running_time_min: Длительность фильма
        :param rating: Рейтинг фильма
        """
        if not isinstance(title, str):
            raise TypeError("Invalid type of title")
        if not isinstance(running_time_min, int):
            raise TypeError("Invalid type of running time (min)")
        if not isinstance(rating, float):
            raise TypeError("Invalid type of rating")
        self.tite = title  # Название фильма
        self.running_time_min = running_time_min  # Длительность фильма
        self.rating = rating  # Рейтинг фильма
        self.timestamp = 0  # Временная отметка воспроизведения
        self.status = "PAUSED"  # Статус воспроизведения
    def play(self) -> None:  # меняет состояние на воспроизведение
        """ Метод воспроизведения"""
        self.status = "PLAYING"
        ...
    def pause(self) -> None: # меняет состояние на паузу и записывает таймстемп в минутах для продолжения воспроизведения
        """ Метод паузы."""
        self.status = "PAUSED"
        self.timestamp = self.get_timestamp()
    def get_timestamp(self) -> int:  # возвращает int таймстемп в минутах
        """Метод получения таймстемпа"""
        timestamp = get_video_player_timestamp()
        if timestamp > self.running_time_min:
            raise ValueError("Timestamp must be less than the running_time_min")
        return timestamp

def get_video_player_timestamp() -> int: # Получить время воспроизведения из api видеоплеера
    """ Метод получения отметки от апи плеера. """
    ...


class Car:
    """
    Документация на класс.
    Класс описывает автомобиль.
    """
    def __init__(self, color: str, tank_capacity: float, occupied_volume: float, consumption: float):
        """
        Инициализация экземпляра класса.
        :param color: Цвет автомобиля
        :param tank_capacity: Объём бака автомобиля
        :param occupied_volume:  Объём топлива в баке
        :param consumption: Потребление топлива
        """
        if not isinstance(color, str):
            raise TypeError
        if not isinstance(tank_capacity, (int, float)):
            raise TypeError
        if not tank_capacity > 0:
            raise ValueError
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if  occupied_volume < 0 or occupied_volume > tank_capacity:
            raise ValueError
        if not isinstance(consumption, (int, float)):
            raise TypeError
        if not consumption > 0:
            raise ValueError
        self.color = color  # Цвет
        self.tank_capacity = tank_capacity  # Объём бака
        self.occupied_volume = occupied_volume  # Объём топлива в баке
        self.consumption = consumption  # Потребление топлива в расчёте на расстояние
    def calculate_occupied_volume(self, path: Union[int, float]) -> float:  # Рассчитывает оставшийся после поездки объём топлива
        """
        Метод расчёта оставшегося после поездки объёма топлива.
        :param path: Дальность пути
        :return: Объём оставшегося топлива
        Пример:
        >>> car = Car("RED", 100, 50, 1)
        >>> car.calculate_occupied_volume(1)
        49
        """
        if not isinstance(path, (int, float)):
            raise TypeError
        return self.occupied_volume - path * self.consumption

    def recolor(self, new_color: str) -> None:  # задаёт новый цвет машины
        """ Метод перекраски машины. """
        if not isinstance(new_color, str):
            raise TypeError
        ...


class Phone:
    """
    Документация на класс.
    Класс описывает телефон.
    """
    def __init__(self, charge_level: Union[int, float]):
        """
         Инициализация экземпляра класса.
        :param charge_level: Уровень заряда телефона
        """
        self.MAX_CHARGE = 100  # уровень заряда в %
        """ Максимальный заряд телефона. """
        self.MIN_CHARGE = 0  # уровень заряда в %
        """ Минимальный заряд телефона. """
        if not isinstance(charge_level, (int, float)):
            raise TypeError
        if self.MAX_CHARGE < 0 or charge_level > self.MAX_CHARGE:
            raise ValueError
        self.charge_level = charge_level
    def charge(self, new_charge_level) -> None:
        """ Метод заряжания телефона. """
        if not isinstance(new_charge_level, (int, float)):
            raise TypeError
        if new_charge_level < self.MIN_CHARGE or new_charge_level > self.MAX_CHARGE or self.charge_level < new_charge_level:
            raise ValueError("Can not charge up to this level!")
        self.charge_level = new_charge_level
    def discharge(self, new_charge_level) -> None:
        """ Метод разряжания телефона. """
        if not isinstance(new_charge_level, (int, float)):
            raise TypeError
        if new_charge_level < self.MIN_CHARGE or new_charge_level > self.MAX_CHARGE or self.charge_level > new_charge_level:
            raise ValueError("Can not charge down to this level!")
        self.charge_level = new_charge_level


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

