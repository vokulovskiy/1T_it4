import pandas as pd

# Загружаем данные из файла data.csv
data = pd.read_csv('data.csv')

# Вычисляем среднюю зарплату
average_salary = data['salary'].mean()

# Отбираем сотрудников старше 30 лет
employees_over_30 = data[data['age'] > 30]

# Выводим результаты
print(f"Средняя зарплата всех сотрудников: {average_salary:.2f}")
print("\nСотрудники старше 30 лет:")
print(employees_over_30.to_string(index=False))
