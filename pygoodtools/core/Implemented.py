from typing import Type, Callable


class Implemented:
    def __init__(self, cls: Type):
        """
        Инициализирует декоратор с классом, в который будут добавляться методы.

        :param cls: Класс, в который будут добавляться методы.
        """
        if not isinstance(cls, type):
            raise TypeError("cls должен быть классом")
        self.cls = cls

    def __call__(self, func: Callable) -> Callable:
        """
        Добавляет функцию в класс как метод.

        :param func: Функция, которая будет добавлена в класс.
        :return: Оригинальная функция.
        """
        if not callable(func):
            raise TypeError("func должен быть вызываемым объектом")
        setattr(self.cls, func.__name__, func)
        return func

    @staticmethod
    def to(_cls: Type) -> Callable[[Callable], Callable]:
        """
        Возвращает декоратор, который добавляет функцию в указанный класс.

        :param _cls: Класс, в который будет добавлена функция.
        :return: Декоратор, добавляющий функцию в класс.
        """
        if not isinstance(_cls, type):
            raise TypeError("_cls должен быть классом")

        def decorator(func: Callable) -> Callable:
            if not callable(func):
                raise TypeError("func должен быть вызываемым объектом")
            setattr(_cls, func.__name__, func)
            return func

        return decorator