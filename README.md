# writing_cleaning_db

# 1 Задание - Linux. Скрипт Bah для копирования фалов на серверы

Файл `script.sh`

## Данный скрипт работает следующим образом:
 - Он итерируется по файлу с хостами
 - Подключается к каждому из них
 - Кладет файл в необходимый путь на хост
 - Если все хосты были доступны, прийдет письмо на почту, что все файлы разнесены по всем адресам
 - Те хосты, к которым не удается подключиться добавляются в массив
 - Далее, если в массиве недоступных хостов есть более, чем 0 записей, массив переводится в файл txt
 - После чего отправляется на указанный email

## Что необходимо для работы:
- server_file: путь до файла с хостами
- file: путь до файла, который копируем
- path_in_host: путь, куда необходимо положить файл на хост
- email: адресс электронной почты, куда необходимо отправлять информацию по недоступным хостам
- для работы email оповещения необходимо установить `mailutils`

## Запуск скрипта
Для запуска скрипта необходимо ввести каманду в терминале `sh script.sh`


# 2 Задание - Python, Docker. Скрипт Python.

## Краткое описание
Данный скрипт раз в минуту генерирует случайные данные, которые записываются в базу данных.
После того, как набирается 30 записей, скрипт удаляет их из базы и начинает запись с новой строки
Расчитан на непрерывную работу.

## Технологии
- python 3.11 
- sqlalchemy 2.0.19
- alembic 1.11.1
- faker 19.1.0
- loguru 0.7.0
- pydantic 1.10.5
- psycopg2-binary 2.9.6
- python-dotenv 1.0.0

#.env файл
В корне проекта необходимо создать .env файл.
Так же есть файл .env.example, в нем указаны все дефолтные значения
Разместите в нем следующие переменные:

- DB_DIALECT=postgresql+pyscopg2
- DB_NAME=<Имя базы данных>
- DB_USER=<Имя базы пользователя>
- DB_PASSWORD=<Пароль базы данных>
- DB_HOST=db
- DB_PORT=<Порт базы данных>
- MAX_OBJECTS_QUERY=<Максимальное количество объектов в бд> 


## Развернуть проект
Клонировать репозиторий
```sh
git clone <ssh ссылка>
```
В дирректории проекта выполните комманду, для запуска контейнера
```sh
sudo docker compose up --build
```

## Данные
В базе данных будет создана одна таблица `free_entry`
У нее есть следующие поля:
- id: уникальный ключ объекта. Присваивается автоматом. Уникален
- data: случайная строка. Генерируется с помощью библиотеки Faker
- date: дата и время записи объекта в бд

## В терминале доступно логирование.
Логируются следующие события:
- Формирование данных
- Запись данных в бд
- Удаление данных из бд
- Получение данных
- Сбой при записе или удалении объектов из бд

## Автор Григорян Арсен
