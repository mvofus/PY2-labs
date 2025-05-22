from typing import Union


class Building:
    """
    Документация на класс.
    Базовый класс для представления зданий.
    """
    def __init__(self, address: str, floors: int, area:  Union[float, int]):
        """
        Инициализация экземпляра класса.
        :param address: Адрес здания
        :param floors: Количество этажей
        :param area: Площадь здания
        
        Примеры:
        >>> building = Building("ул. Пушкина", 5, 100)
        """
        if not isinstance(address, str):
            raise TypeError("Addres must be a string")
        if not isinstance(floors, int):
            raise TypeError("Floors must be an int")
        if not isinstance(area,(int, float)):
            raise TypeError("Invalid type of area")
        if floors <= 0:
            raise ValueError("Floors must be positive")
        if area <= 0:
            raise ValueError("Area must be positive")
        self._address = address  # Инкапсуляция для контроля значения через сеттер        
        self._floors = floors
        self._area = area

    @property
    def address(self) -> str:
        """Получить адресс"""
        return self._address

    @property
    def floors(self) -> int:
        """Получить количество этажей"""
        return self._floors
    
    @property
    def area(self) ->  Union[float, int]:
        """Получить количество этажей"""
        return self._area

    @address.setter  # На случай переименования улицы/города и т.п.
    def address(self, value: str) -> None:
        """Установить адресс с проверкой значения"""
        if not isinstance(self.address, str):
            raise TypeError("Addres must be a string")
        self.address = value

    def __str__(self) -> str:
        return f"Здание по адресу {self.address} ({self.floors} этажей)"

    def __repr__(self) -> str:
        return f"Building(address={self.address!r}, floors={self.floors!r}, area={self.area!r})"

    def calculate_tax(self) -> float:
        """
        Рассчитать ежегодный налог на недвижимость
        
        Возвращает:
            float: Размер налога по базовой ставке в 0.1%
            
        Пример:
        >>> building = Building("ул. Пушкина", 5, 100)
        >>> building.calculate_tax()
        0.1
        """
        return self.area * 0.001
    
    def area_of_floor(self) -> float:
        """
        Получить площадь одного этажа
        
        Возвращает:
            float: Площадь одного этажа
        
        Пример:
        >>> building = Building("ул. Пушкина", 5, 100)
        >>> building.area_of_floor()
        20.0
        """
        return self.area / self.floors


class Skyscraper(Building):
    """
    Класс для представления небоскребов.
    
    Наследует: Building
    
    Дополнительные атрибуты:
        has_observatory (bool): Наличие смотровой площадки
        
    Пример:
       >>> building = Skyscraper("ул. Пушкина", 5, 100, True)
       >>> building.area_of_floor()
       20.0
    
    """
    def __init__(self, address: str, floors: int, area: float, has_observatory: bool):
        """
        Инициализация экземпляра класса.
        :param address: Адрес здания
        :param floors: Количество этажей
        :param area: Общая площадь здания
        :param has_observatory: Наличие смотровой площадки
        
        Пример:
        >>> skyscraper = Skyscraper("Шанхай", 128, 400000, True)
        """
        super().__init__(address, floors, area)
        self.has_observatory = has_observatory

    def __str__(self) -> str:
        """Расширяем строковое представление"""
        base = super().__str__()
        return f"Небоскреб {base}" + (" со смотровой площадкой" if self.has_observatory else "")

    def __repr__(self) -> str:
        """Перегрузка repr с добавлением атрибута"""
        return f"Skyscraper({super().__repr__()}, has_observatory={self.has_observatory!r})"

    def calculate_tax(self) -> float:
        """
        Перегрузка метода расчета налога с учетом повышенной ставки для небоскребов
        
        Причина перегрузки: Небоскребы облагаются дополнительным налогом в 0.05%
        
        Пример:
        >>> burj_khalifa = Skyscraper("Dubai, UAE", 163, 309500, True)
        >>> burj_khalifa.calculate_tax()
        464.25
        """
        return super().calculate_tax() + self.area * 0.0005


class Cottage(Building):
    """
    Класс для представления коттеджей.
    
    Наследует: Building
    
    Дополнительные атрибуты:
        garden_area (float): Площадь садового участка в м²
        
    Пример:
        >>> cottage = Cottage("Московская обл.", 2, 150, 600)
        >>> cottage.area_of_floor()
        75.0
    """
    def __init__(self, address: str, floors: int, area: float, garden_area: float):
        """
        Инициализация экземпляра класса.
        :param address: Адрес здания
        :param floors: Количество этажей
        :param area: Общая площадь здания
        :param garden_area: Площадь садового участка
        
        Пример:
        >>> dacha = Cottage("Московская обл.", 2, 150, 600)
        """
        super().__init__(address, floors, area)
        self.garden_area = garden_area

    def __str__(self) -> str:
        """Расширяем строковое представление"""
        return f"Коттедж {super().__str__()} с участком {self.garden_area} м²"

    def get_total_area(self) -> float:
        """
        Получить общую площадь (дом + участок)
        
        Унаследованная функциональность с расширением
        
        Примеры:
        >>> Cottage("Ленобласть", 1, 90, 350).get_total_area()
        440
        """
        return self.area + self.garden_area
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()