"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
""" Для превого примера была взята первую задачу из 3 урока"""

from memory_profiler import profile
from random import randint

@profile

def RAN():
    NUM_1 = list(range(2, 1000))
    NUM_2 = list(range(2, 1000))
    for elem in NUM_2:
        NUM = 0
        for i in NUM_1:
            if i % elem == 0:
                NUM += 1
        print(f"В диапазоне 2-99 {i} числа кратны {elem}")

RAN()

print()

"""Line #    Mem usage    Increment   Line Contents
================================================
    18     14.2 MiB     14.2 MiB   @profile
    19                             
    20                             def RAN():
    21     14.2 MiB      0.0 MiB       NUM_1 = list(range(2, 1000))
    22     14.2 MiB      0.0 MiB       NUM_2 = list(range(2, 1000))
    23     14.2 MiB      0.0 MiB       for elem in NUM_2:
    24     14.2 MiB      0.0 MiB           NUM = 0
    25     14.2 MiB      0.0 MiB           for i in NUM_1:
    26     14.2 MiB      0.0 MiB               if i % elem == 0:
    27     14.2 MiB      0.0 MiB                   NUM += 1
    28     14.2 MiB      0.0 MiB           print(f"В диапазоне 2-99 {i} числа кратны {elem}")

"""
"""По этим данным можно сделать вывод, что память так же была не задействована. Но объем был большой и как я понял 
оснавная нагрузка легла на процессор. Просьба прояснить, может ли быть такое?"""