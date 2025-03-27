

#!/usr/bin/env python3

import sys

sys.stdin = open("smapout.txt", "r")
sys.stdout = open("redout.txt", "w")

current_grupe = None
ma = None  # Максимальный вес одной посылки
mi = None  # Минимальный вес одной посылки
avg = None  # Средний вес одной посылки
bendras_svoris = 0  # Общий вес
bendras_siuntu_skaicius = 0  # Общее количество посылок

# Обрабатываем данные
for line in sys.stdin:
    line = line.strip()
    
    try:
        grupe, svoris, siuntu_skaicius = line.split('\t')
        svoris = float(svoris)
        siuntu_skaicius = int(siuntu_skaicius)
    except ValueError:
        continue  # Пропускаем строки с ошибками

    # Если количество посылок 0, заменяем его на 1
    if siuntu_skaicius == 0:
        siuntu_skaicius = 1  

    siuntos_svoris = svoris / siuntu_skaicius  # Вес одной посылки

    # Если группа та же
    if grupe == current_grupe:
        bendras_svoris += svoris
        bendras_siuntu_skaicius += siuntu_skaicius
        ma = max(ma, siuntos_svoris)
        mi = min(mi, siuntos_svoris)
    else:
        # Выводим результаты для предыдущей группы
        if current_grupe is not None:
            avg = bendras_svoris / bendras_siuntu_skaicius
            print(f"{current_grupe}\tMax: {ma:.3f}\tMin: {mi:.3f}\tAvg: {avg:.3f}")

        # Начинаем новую группу
        current_grupe = grupe
        ma = siuntos_svoris
        mi = siuntos_svoris
        bendras_svoris = svoris
        bendras_siuntu_skaicius = siuntu_skaicius

# Выводим последнюю группу
if current_grupe is not None:
    avg = bendras_svoris / bendras_siuntu_skaicius
    print(f"{current_grupe}\tMax: {ma:.3f}\tMin: {mi:.3f}\tAvg: {avg:.3f}")