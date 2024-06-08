import pandas as pd
import numpy as np

names = (['Иван', 'Мария', 'Виктор', 'Михаил', 'Анна', 'Юлия', 'Сергей', 'Андрей', 'Оксана', 'Петр'])
subjects = ('math', 'english', 'biology')
random_subjects = np.random.choice(subjects, 10)
grades = np.random.randint(3, 6, 10)

df = pd.DataFrame({'name': names, 'subject': random_subjects, 'grade': grades})

print(df.head())

print(f'\n Средняя оценка по предмету- {df.groupby('subject')['grade'].mean()}')
print(f'\n Медианная оценка по предмету- {df.groupby('subject')['grade'].median()}')
print(f'\n Стандартное отклонение по оценкам- {df['grade'].std()}')

print('\nСрез по математике:')
math_grades = df[df['subject'] == 'math']['grade']
Q1_math = math_grades.quantile(0.25)
Q3_math = math_grades.quantile(0.75)
IQR = Q3_math- Q1_math

print(f'\nПервый квартиль = {Q1_math}, третий квартиль = {Q3_math}, межквартильный размах = {IQR} ')