# Выведем каждый заголовок и его позицию в списке

from pathlib import Path
import csv

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Функция enumerate() возвращает индекс каждого элемента и его значение при переборе списка.
for index, column_header in enumerate(header_row):
    print(index, column_header)