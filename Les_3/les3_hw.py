# Даны 2 числа a  и b. Получить их сумму разность и произведение

a = 7
b = 5

print(a + b)
print(a - b)
print(a * b)

# даны числа x и y.  Получить x-y/1+xy

x = 12
y = 7

exspression = (x - y)/(1 + (x*y))

print(f'Результат {exspression}')

# Даны 2 числа, найти среднее арифметическое и среднее геометрическое этих чисел

c = 6
d = 9

full_summ = (c+d)/2
full_geom = (c*d)**0.5
print("Full summ is equal:" + str(full_summ))
print("Full geometr is equal:" +str(full_geom))

#даны катеты прямоугольного треугольникаю Найти его гипотенузу и площадь

side_1 = 4
side_2 = 5

hyp_sq = (side_1**2 + side_2**2)
hyp = hyp_sq**0.5

square_size = (side_1*side_2)/2

print(f"Hyp is equal: {hyp}")
print("Square of riangle is: " + str(square_size))


