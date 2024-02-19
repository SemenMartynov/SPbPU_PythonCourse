from typing import Tuple
from abc import ABC, abstractmethod


class Transport(ABC):
    """
    Абстрактный базовый класс, представляющий транспортное средство.

    Атрибуты:
        service_org_code (str): Код обслуживающей организации.
        fleet_number (str): Идентификационный номер транспортного средства в фирме.
        max_passenger_capacity (int): Максимально допустимое количество пассажиров.
        coordinates (Tuple[float, float]): Текущие географические координаты транспортного средства.

    Методы:
        __init__: Конструктор класса.
        __str__: Метод для получения удобного строкового представления объекта.
        __repr__: Метод для получения официального строкового представления объекта.
        fare: Абстрактный метод, который должен быть реализован в производных классах.
    """

    def __init__(self, service_org_code: str, fleet_number: str, max_passenger_capacity: int,
                 coordinates: Tuple[float, float]):
        """
        Инициализирует новый экземпляр класса Transport.

        Параметры:
            service_org_code (str): Код обслуживающей организации.
            fleet_number (str): Идентификационный номер транспортного средства.
            max_passenger_capacity (int): Максимальное количество пассажиров.
            coordinates (Tuple[float, float]): Географические координаты транспортного средства.
        """
        self.service_org_code = service_org_code
        self.fleet_number = fleet_number
        self.max_passenger_capacity = max_passenger_capacity
        self.coordinates = coordinates

    def __str__(self) -> str:
        """
        Возвращает строку с описанием класса Transport.

        Returns:
            str: Описание класса Transport.
        """
        return (f"Transport: service organization code: {self.service_org_code}, "
                f"fleet number: {self.fleet_number}, max passenger capacity: {self.max_passenger_capacity}, "
                f"coordinates: {self.coordinates}")

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта для воссоздания идентичной копии.
        """
        return (f"{self.__class__.__name__}(service_org_code={self.service_org_code}, "
                f"fleet_number='{self.fleet_number}', max_passenger_capacity={self.max_passenger_capacity}, "
                f"coordinates={self.coordinates})")

    @abstractmethod
    def fare(self) -> float:
        """
        Абстрактный метод определения стоимости проезда.

        Returns:
            float: Стоимость проезда для данного типа транспорта.
        """
        pass


class RouteTransport(Transport):
    """
    Класс, представляющий маршрутное транспортное средство, производный от класса Transport.

    Атрибуты:
        route_number (str): Номер маршрута.
        has_conductor (bool): Наличие кондуктора на борту.
        start_time (str): Время начала работы маршрута.
        end_time (str): Время окончания работы маршрута.
        ticket_price (float): Стоимость проездного билета.

    Методы:
        __init__: Конструктор класса.
        __str__: Метод для получения удобного строкового представления объекта.
        __repr__: Метод для получения официального строкового представления объекта.
        fare: Метод для определения стоимости проезда, который здесь же и реализуется.
    """

    def __init__(self, service_org_code: str, fleet_number: str, max_passenger_capacity: int,
                 coordinates: Tuple[float, float],
                 route_number: str, has_conductor: bool, start_time: str, end_time: str, ticket_price: float):
        """
        Инициализирует новый экземпляр класса RouteTransport, наследуемый от Transport.

        Параметры:
            service_org_code (str): Код обслуживающей организации.
            fleet_number (str): Идентификационный номер транспортного средства в фирме.
            max_passenger_capacity (int): Максимально допустимое количество пассажиров.
            coordinates (Tuple[float, float]): Текущие географические координаты транспортного средства.
            route_number (str): Номер маршрута.
            has_conductor (bool): Наличие кондуктора.
            start_time (str): Время начала работы маршрута.
            end_time (str): Время окончания работы маршрута.
            ticket_price (float): Стоимость проездного билета.
        """
        super().__init__(service_org_code, fleet_number, max_passenger_capacity, coordinates)
        self.route_number = route_number
        self.has_conductor = has_conductor
        self.start_time = start_time
        self.end_time = end_time
        self.ticket_price = ticket_price

    def __str__(self) -> str:
        """
        Строковое описание маршрутного траспорта.

        Returns:
            str: строка с описанием маршрутного траспорта.
        """
        base_info = super().__str__()
        return (f"{base_info}, route_number={self.route_number}, "
                f"has_conductor: {self.has_conductor}, "
                f"start_time: {self.start_time}, end_time: {self.end_time}")

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: строковое представление объекта для воссоздания идентичной копии.
        """
        base_info = super().__repr__().rstrip(")")
        return (f"{base_info}, route_number={self.route_number}, "
                f"has_conductor={self.has_conductor}, "
                f"start_time='{self.start_time}', end_time='{self.end_time}')")

    def fare(self) -> float:
        """
        Возвращает стоимость проезда для пассажира.

        Returns:
            float: Стоимость проездного билета.
        """
        return self.ticket_price


class Bus(RouteTransport):
    """
    Класс, представляющий автобус, производный от RouteTransport.

    Атрибуты:
        _fuel_capacity (float): Объём топливного бака l (публичное статическое поле).
        _fuel_consumption_rate (float): Расход топлива на 100 км l/100km (публичное статическое поле).
        fuel_remainder (float): Количество топлива в баке l.

    Методы:
        __init__: Конструктор класса.
        __str__: Метод для получения удобного строкового представления объекта.
        __repr__: Метод для получения официального строкового представления объекта.
        fuel_remainder.setter: Метод, позволяющий установить уровень топлива в баке.
        fuel_remainder.getter: Метод, возвращающий уровень топлива в баке.
        calculate_distance_until_refueling: Метод, рассчитывающий сколько км автобус сможет проехать до следующей
        заправки.

    >>> bus = Bus("АП-3", "318И", 50, (55.7558, 37.6173), "А12", True, "05:00", "23:30", 55, 150)
    >>> bus.calculate_distance_until_refueling()
    600.0
    """
    _fuel_capacity = 200.0  # объём топливного бака в литрах
    _fuel_consumption_rate = 25.0  # расход топлива на 100 км в литрах/100км

    def __init__(self, service_org_code: str, fleet_number: str, max_passenger_capacity: int,
                 coordinates: Tuple[float, float],
                 route_number: str, has_conductor: bool, start_time: str, end_time: str, ticket_price: float,
                 fuel_remainder: float):
        """
        Инициализирует новый экземпляр класса Bus.

        Параметры:
            service_org_code (str): Код обслуживающей организации.
            fleet_number (str): Идентификационный номер автобуса в фирме.
            max_passenger_capacity (int): Максимальное количество пассажиров.
            coordinates (Tuple[float, float]): Текущие географические координаты автобуса.
            route_number (str): Номер маршрута.
            has_conductor (bool): Наличие кондуктора.
            start_time (str): Время начала работы маршрута.
            end_time (str): Время окончания работы маршрута.
            ticket_price (float): Стоимость проездного билета.
            fuel_remainder (float): Текущее количество топлива в баке.
        """
        super().__init__(service_org_code, fleet_number, max_passenger_capacity, coordinates, route_number,
                         has_conductor, start_time, end_time, ticket_price)
        self.fuel_remainder = fuel_remainder

    def __str__(self) -> str:
        """
        Строка описывающиая автобус.

        Returns:
            str: строка с описанием автобуса.
        """
        base_info = super().__str__()
        return f"{base_info}, fuel remainder: {self.fuel_remainder}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта для воссоздания идентичной копии.
        """
        base_info = super().__repr__().rstrip(")")
        return f"{base_info}, fuel_remainder={self.fuel_remainder})"

    @property
    def fuel_remainder(self) -> float:
        """Возвращает количество литров оставшегося топлива в баке."""
        return self._fuel_remainder

    @fuel_remainder.setter
    def fuel_remainder(self, value: float):
        """
        Устанавливает количество топлива в баке.

        Параметры:
            value (float): Желаемое количество топлива для установки.

        Возбуждает:
            ValueError: Если заданное количество топлива выходит за допустимые пределы.
        """
        if not 0 <= value <= self._fuel_capacity:
            raise ValueError("Значение остатка топлива должно находиться в диапазоне от 0 до объема топливного бака.")
        self._fuel_remainder = value

    def calculate_distance_until_refueling(self) -> float:
        """
        Рассчитывает и возвращает дистанцию (в километрах), которую автобус сможет проехать до следующей заправки.

        Returns:
            float: Дистанция до следующей заправки в километрах.

        Пример использования:
        >>> bus = Bus("АП-3", "318И", 50, (55.7558, 37.6173), "А12", True, "05:00", "23:30", 55, 150)
        >>> bus.calculate_distance_until_refueling()
        600.0
        """
        distance = (self.fuel_remainder / self._fuel_consumption_rate) * 100
        return distance


class Tram(RouteTransport):
    """
    Класс, представляющий трамвай, производный от RouteTransport.

    Атрибуты:
        contact_with_power_grid (bool): Наличие контакта с электросетью.

    Методы:
        __init__: Конструктор класса.
        __str__: Метод для получения удобного строкового представления объекта.
        __repr__: Метод для получения официального строкового представления объекта.
        is_emergency_stop: Метод для проверки, произошла ли аварийная остановка.

    >>> tram = Tram("ГорЭлектроТранспорт", "303-1", 100, (48.8566, 2.3522), "Е15", True, "06:00", "22:00", 35.0, True)
    >>> tram.is_emergency_stop()
    False
    """

    def __init__(self, service_org_code: str, fleet_number: str, max_passenger_capacity: int,
                 coordinates: Tuple[float, float],
                 route_number: str, has_conductor: bool, start_time: str, end_time: str, ticket_price: float,
                 contact_with_power_grid: bool):
        """
        Инициализирует новый экземпляр класса Tram.

        Параметры:
            service_org_code (str): Код обслуживающей организации.
            fleet_number (str): Идентификационный номер трамвая в фирме.
            max_passenger_capacity (int): Максимальное количество пассажиров.
            coordinates (Tuple[float, float]): Текущие географические координаты трамвая.
            route_number (str): Номер маршрута.
            has_conductor (bool): Наличие кондуктора.
            start_time (str): Время начала работы маршрута.
            end_time (str): Время окончания работы маршрута.
            ticket_price (float): Стоимость проездного билета.
            contact_with_power_grid (bool): Состояние контакта с электросетью.
        """
        super().__init__(service_org_code, fleet_number, max_passenger_capacity, coordinates, route_number,
                         has_conductor, start_time, end_time, ticket_price)
        self.contact_with_power_grid = contact_with_power_grid

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Удобное для восприятия представление объекта.
        """
        base_info = super().__str__()
        return f"{base_info}, contact with power grid: {self.contact_with_power_grid}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта.

        Returns:
            str: Официальное строковое представление объекта для воссоздания идентичной копии.
        """
        base_info = super().__repr__().rstrip(")")
        return f"{base_info}, contact_with_power_grid={self.contact_with_power_grid})"

    def is_emergency_stop(self) -> bool:
        """
        Проверяет наличие аварийной остановки из-за отсутствия контакта с электросетью.

        Returns:
            bool: True, если произошла аварийная остановка и False в противном случае.

        Пример использования:
        >>> tram = Tram("ГорЭлектроТранс", "303-1", 100, (48.8566, 2.3522), "Е15", True, "06:00", "22:00", 35.0, True)
        >>> tram.is_emergency_stop()
        False
        """
        return not self.contact_with_power_grid


class EBus(RouteTransport):
    """
    Класс, представляющий электробус, производный от RouteTransport.

    Атрибуты:
        _max_battery_range_km (float): Максимальное расстояние, которое электробус может преодолеть на полной зарядке
          батареи.
        battery_charge_remainder (float): текущий уровень заряда батареи в процентах.
        contact_with_power_grid (bool): Наличие контакта с электросетью для зарядки.

    Методы:
        __init__: Конструктор класса.
        __str__: Метод для получения удобного строкового представления объекта.
        __repr__: Метод для получения официального строкового представления объекта.
        battery_charge_remainder.setter: Метод, позволяющий установить уровень заряда батареи.
        battery_charge_remainder.getter: Метод, возвращающий уровень заряда батареи.
        calculate_remaining_battery_range: Метод, рассчитывающий оставшийся пробег на текущем заряде батареи.

    >>> ebus = EBus("ГЭТ", "002425", 70, (34.0522, -118.2437), "Э18", True, "04:00", "22:00", 25.0, False, 80.0)
    >>> ebus.calculate_remaining_battery_range()
    24.0
    """
    _max_battery_range_km = 30.0  # Максимальное расстояние на полном заряде батареи

    def __init__(self, service_org_code: str, fleet_number: str, max_passenger_capacity: int,
                 coordinates: Tuple[float, float],
                 route_number: str, has_conductor: bool, start_time: str, end_time: str, ticket_price: float,
                 contact_with_power_grid: bool, battery_charge_remainder: float):
        """
        Инициализирует новый экземпляр класса EBus.

        Параметры:
            service_org_code (str): Код обслуживающей организации.
            fleet_number (str): Идентификационный номер электробуса в фирме.
            max_passenger_capacity (int): Максимальное количество пассажиров.
            coordinates (Tuple[float, float]): Текущие географические координаты электробуса.
            route_number (str): Номер маршрута.
            has_conductor (bool): Наличие кондуктора.
            start_time (str): Время начала работы маршрута.
            end_time (str): Время окончания работы маршрута.
            ticket_price (float): Стоимость проездного билета.
            contact_with_power_grid (bool): Состояние контакта с электросетью для зарядки.
            battery_charge_remainder (float): Текущий уровень заряда батареи.
        """
        super().__init__(service_org_code, fleet_number, max_passenger_capacity, coordinates, route_number,
                         has_conductor, start_time, end_time, ticket_price)
        self.contact_with_power_grid = contact_with_power_grid
        self.battery_charge_remainder = battery_charge_remainder

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Удобное для восприятия представление объекта.
        """
        base_info = super().__str__()
        return (f"{base_info}, contact with power grid: {self.contact_with_power_grid}, "
                f"battery charge remainder: {self.battery_charge_remainder}")

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта.

        Returns:
            str: Официальное строковое представление объекта для воссоздания идентичной копии.
        """
        base_info = super().__repr__().rstrip(")")
        return (f"{base_info}, contact_with_power_grid={self.contact_with_power_grid}, "
                f"battery_charge_remainder={self.battery_charge_remainder}")

    @property
    def battery_charge_remainder(self) -> float:
        """Возвращает текущий уровень заряда батареи."""
        return self._battery_charge_remainder

    @battery_charge_remainder.setter
    def battery_charge_remainder(self, value: float):
        """
        Устанавливает текущий уровень заряда батареи.

        Параметры:
            value (float): Желаемый уровень заряда батареи в процентах.

        Возбуждает:
            ValueError: Если заданный уровень заряда выходит за допустимые пределы.
        """
        if not 0 <= value <= 100:
            raise ValueError("Значение заряда батареи должно быть в пределах от 0% до 100%.")
        self._battery_charge_remainder = value

    def calculate_remaining_battery_range(self) -> float:
        """
        Рассчитывает оставшийся пробег на текущем уровне заряда батареи.

        Returns:
            float: Оставшееся расстояние на текущем заряде батареи в километрах.

        Пример использования:
        >>> ebus = EBus("ГЭТ", "002425", 70, (34.0522, -118.2437), "Э18", True, "04:00", "22:00", 25.0, False, 80.0)
        >>> ebus.calculate_remaining_battery_range()
        24.0
        """
        # Пропорционально масштабируем заряд относительно максимального пробега
        if not self.contact_with_power_grid:  # Если электросеть недоступна, используем батарею
            return (self.battery_charge_remainder / 100) * self._max_battery_range_km
        return 0.0


if __name__ == "__main__":
    # Создание объекта класса Bus
    bus = Bus(
        service_org_code="Автомобильный парк 3",
        fleet_number="B1234",
        max_passenger_capacity=60,
        coordinates=(59.9386, 30.3141),  # Координаты Санкт-Петербурга
        route_number="А123",
        has_conductor=False,
        start_time="06:00",
        end_time="23:00",
        ticket_price=45.0,
        fuel_remainder=100.0
    )

    # Использование методов класса Bus
    print(bus)
    print(repr(bus))
    print(f"Bus fare: {bus.fare():.2f} RUB")
    print(f"Distance until refueling: {bus.calculate_distance_until_refueling():.2f} km")

    # Попытаемся установить неверное значение остатка топлива
    try:
        bus.fuel_remainder = 250.0  # значение превышает _fuel_capacity
    except ValueError as e:
        print(e)

    # Создание объекта класса Tram
    tram = Tram(
        service_org_code="CD456",
        fleet_number="T5678",
        max_passenger_capacity=100,
        coordinates=(48.8566, 2.3522),  # Координаты Парижа
        route_number="3",
        has_conductor=True,
        start_time="05:30",
        end_time="01:00",
        ticket_price=2.25,
        contact_with_power_grid=True
    )

    # Использование методов класса Tram
    print(tram)
    print(repr(tram))
    print(f"Tram fare: {tram.fare():.2f} EUR")
    print(f"Is there an emergency stop? {'Yes' if tram.is_emergency_stop() else 'No'}")

    # Проведем имитацию аварийной остановки
    tram.contact_with_power_grid = False
    print(f"Emergency stop now? {'Yes' if tram.is_emergency_stop() else 'No'}")

    # Создание объекта класса EBus
    ebus = EBus(
        service_org_code="EF789",
        fleet_number="E9012",
        max_passenger_capacity=50,
        coordinates=(34.0522, -118.2437),  # Координаты Лос-Анджелеса
        route_number="E1",
        has_conductor=False,
        start_time="04:00",
        end_time="22:00",
        ticket_price=4.0,
        contact_with_power_grid=False,
        battery_charge_remainder=75.0  # 75% заряд батареи
    )

    # Использование методов класса EBus
    print(ebus)
    print(repr(ebus))
    print(f"EBus fare: {ebus.fare():.2f} USD")
    print(f"Remaining battery range: {ebus.calculate_remaining_battery_range():.2f} km")

    # Попытаемся установить неверное значение заряда батареи
    try:
        ebus.battery_charge_remainder = 110.0  # Значение превышает максимум в 100%
    except ValueError as e:
        print(e)
