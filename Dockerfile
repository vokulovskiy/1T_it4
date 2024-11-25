# Используем базовый образ Python
FROM python:3.12-slim
# Устанавливаем pandas
RUN pip install pandas
# Устанавливаем рабочую директорию
WORKDIR /app
# Копируем файлы проекта в контейнер
COPY it4_app.py it4_app.py
COPY data.csv data.csv
# Определяем команду для запуска приложения
CMD ["python", "it4_app.py"]
