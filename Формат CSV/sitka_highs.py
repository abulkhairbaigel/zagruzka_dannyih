# Модуль datetime.
# СМОТРЕТЬ СТРАНИЦУ 380 КНИГИ ЭРИКА МЭТИЗА, подзаголовок: "Модуль datetime".  

from pathlib import Path
import csv

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Извлечение максимальных температур.
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

# Нанесение данных на диаграмму.
plt.style.use('seaborn-v0_8-paper')
fig, ax = plt.subplots()
ax.plot(highs, color='red')

# Форматирование диаграммы.
ax.set_title("Ежедневная максимальная температура, Июль 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Температура (Фаренгейт)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()