# Вместо того чтобы копаться в данных и искать отсутствующее значение, мы напрямую обработаем ситуации с отсутсвием данных.

# При чтении данных из csv-файла будет выполняться код проверки ошибок для обработки исключений,
# которые могут возникнуть при разборе наборов данных. Вот как это делается: 

from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Извлечение дат, минимальных и максимальных температур из файла.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:    # при анализе каждой строки данных мы пытаемся извлечь дату, tmax и tmin.
        high = int(row[3])
        low = int(row[4])
    except ValueError:     # если каких-либо данных не хватает, Python выдает ошибку.
        print(f"Missiong data for {current_date}")   # мы обрабатваем ошибку - выводим сообщение с датой, где нет данных.
    # После вывода ошибки цикл продолжает обработку след. порции данных. 
    else:    # если все данные, относящиеся к некоторой дат, прочитаны без ошибок, то выполняется блок else.
        # Данные присоединяются к соотсветствующим спискам.
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Создание диаграммы высоких и низких температур.
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Форматирование диаграммы.
title = "Ежедневная максимальная и минимальные температуры, 2021\nДолина Смерти, Калифорния"   # изменяем название заголовка.
ax.set_title(title, fontsize=20)    # меняем размер шрифта.
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Температура (Фаренгейт)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()