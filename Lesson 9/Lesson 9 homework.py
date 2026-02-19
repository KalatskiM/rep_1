#распечатайте полное название месяца из этой даты
import datetime
import statistics
from idlelib.replace import replace

date_str = 'Jan 15, 2023 - 12:05:33'
# date_str = date_str.replace("'", '')
# print(date_str)


month_from_date = datetime.datetime.strptime(date_str, '%b %d, %Y - %H:%M:%S')
month_only = month_from_date.strftime('%B')
print(month_only)

# Распечатайте дату в таком формате: "15.01.2023, 12:05"

new_format = month_from_date.strftime('%d.%m.%Y, %H:%M')
print(new_format)






# найти и распечатать из коллекции температур самую высокую температуру, самую маленькую температуру и среднюю
# выписаит высокие и низкие температуры. высокая если больше 28 градусов. найти среднюю из высоких температур

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]


print(max(temperatures))
print(min(temperatures))
print(round(statistics.mean(temperatures), 2))

hot_weather = filter(lambda x: x > 28, temperatures)
hot_weather = list(hot_weather)
average_from_hot = sum(hot_weather)/len(hot_weather)

print(list(hot_weather))
print(round(average_from_hot, 2))
