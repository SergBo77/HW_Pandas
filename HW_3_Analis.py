import pandas as pd
import numpy as np

names = (['Иван', 'Мария', 'Виктор', 'Михаил', 'Анна', 'Юлия', 'Сергей', 'Андрей', 'Оксана', 'Петр'])
subjects = ('math', 'english', 'biology')
random_subjects = np.random.choice(subjects, 10)
grades = np.random.randint(3, 6, 10)

df = pd.DataFrame({'name': names, 'subject': random_subjects, 'grade': grades})

print(df.head())

print(f"Средняя оценка - {df.groupby('subject')['grade'].mean()}")


