# Добавим на график новые данные для получения полной картины погоды в Ситке.
# Нужно будет добавить файл sitka-weather_2021.csv, содержащий погодные данные за целый год.

# Только потом мы сможем сгенерировать диагрумму за год.

from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_simple.csv')    # значение filename было изменено на новый путь
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Извлечение максимальных температур.
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

# Нанесение данных на диаграмму.
plt.style.use('seaborn-v0_8-paper')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Форматирование диаграммы.
ax.set_title("Ежедневная максимальная температура, 2021", fontsize=24)     # изменен заголовок диаграммы.
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Температура (Фаренгейт)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()