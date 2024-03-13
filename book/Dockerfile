FROM python:3.10
ENV PYTHONUNBUFFERED 1

# Копируем requirements.txt в образ
COPY requirements.txt /tmp/requirements.txt

# Устанавливаем зависимости
RUN pip install -r /tmp/requirements.txt

# Создаем директорию для кода
RUN mkdir /book
WORKDIR /book

# Копируем все содержимое в текущую директорию в образ
ADD . /book/

# Открываем порт 5000
EXPOSE 5000


