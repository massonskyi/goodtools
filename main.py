# import pygoodtools


# print(pygoodtools.NULL)
# print(pygoodtools.nullptr)
# print(pygoodtools.void)


# x: pygoodtools.char = pygoodtools.char('a')
import time
from pygoodtools.arm.objects import ArmTimer


def example_callback():
    print("Timer triggered!")

# Создаем таймер с интервалом 2 секунды
my_timer = ArmTimer(interval=2.0, callback=example_callback)

# Запускаем таймер
my_timer.start()
i = 0
# Даем таймеру проработать 10 секунд, потом останавливаем его
while i < 1000000:
    i+=1
    time.sleep(0.1)
my_timer.stop()