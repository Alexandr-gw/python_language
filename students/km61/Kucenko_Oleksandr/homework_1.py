#task1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Напишіть програму, яка отримує три числа і друкує їх суму.
Кожне число користувач вводить у окремому рядку.
"""

fst_usr_nmb=input('Введите первое число: ')
scd_usr_nmb=input('Введите второе число: ')
thr_usr_nmb=input('Введите третье число: ')
print('Суммой трёх чисел будет: ',fst_usr_nmb+scd_usr_nmb+thr_usr_nmb)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Напишіть програму, яка отримує довжини двох катетів
прямокутного трикутника та виводить його площу.
Користувач вводить довжини катетів у окремих рядках.
"""

fst_usr_nmb=int(input('Введите длину первого катета: '))
scd_usr_nmb=int(input('Введите длину второго катета: '))

print('Площадь прямоугольного треугольника равна: ',(fst_usr_nmb*scd_usr_nmb)/2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
N студентів отримали K яблук і розподілити їх між собою порівну.
Неподілені яблука залишились у кошику.
Скільки яблук отримає кожен студент?
Скільки яблук залишиться в кошику?
"""
count_of_stud=int(input('Введите количество студентов : '))
count_of_apple=int(input('Введите количество яблок: '))

print('Каждый студент получит по: ',int(count_of_stud/count_of_apple),'В корзинке останется: ',count_of_apple-count_of_stud*(count_of_stud/count_of_apple))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Нехай число N - кількість хвилин, відрахованих після півночі.
Скільки годин і хвилин буде показувати цифровий годинник,
якщо за відлік взяти 00:00?
"""

count_of_min=int(input('Введите количество минут: '))
print('В ',count_of_min,'минут(ы) входит: ',int((count_of_min/60)-(int(count_of_min/1440))*24),'ч ',count_of_min%60,'мин .')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Напишіть програму, яка вітає користувача, друкуючи слово "Hello",
ім'я користувача і знак оклику після нього. Наприклад “Hello, Mike!”
"""

user_name=str(input('Введите ваше имя : '))
print('Hello ,',user_name,'!')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Напишіть програму,
яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:
The next number for the number 179 is 180.
The previous number for the number 179 is 178.
"""

user_number=int(input('Введите ваше число : '))
print('Число перед ',user_number,' это ',user_number-1)
print('Число после ',user_number,' это ',user_number+1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Школа вирішила сформувати три нові групи учнів та надати їм окремі класи.
У кожному класі необхідно встановити столи для учнів, у розрахунку,
що за одним столом може сидіти не більше двох учнів.
Яку мінімальну кількість столів необхідно придбати?
"""
count_of_pupils=int(input('Введите количество учеников: '))
print('Понадобится: 'int(count_of_pupils/2)+1 ,' парт.')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~