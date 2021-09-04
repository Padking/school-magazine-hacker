# School magazine hacker

Урок № 3 модуля "Знакомство с Django: ORM" от Devman.

## Описание

Скрипт-хакер школьного журнала.
Позволяет изменять сведения школьного журнала, который ведётся в рамках [электронного дневника школы](https://github.com/devmanorg/e-diary)


### Особенности

- сопрягается с сайтом электронного дневника школы,
- исправляет [плохие](https://github.com/Padking/school-magazine-hacker/wiki#notions) оценки ученика на хорошие,
- удаляет замечания ученика, полученные от учителей,
- создаёт похвалу ученику от учителя к случайному [уроку](https://github.com/Padking/school-magazine-hacker/wiki#notions) конкретного предмета.

## Сценарии использования

**Нумерация согласуется со [сценариями](https://gist.github.com/dvmn-tasks/4b354a1f1d7da0267a5922b195dc2d80#file-md)**

### № 1
Школьник Ваня хочет исправить свои оценки. Сайт электронного дневника уже давно настроен и работает на отдельном сервере. У Вани есть к нему доступ. Он уже научился скачивать и загружать файлы на сервер. Также он умеет открывать консоль и запускать там команды.

**Шаги (см. [раздел "Установка"](https://github.com/Padking/school-magazine-hacker/wiki#Установка)):**
- 1, 2, 3, 8 (запуск, исправить цифру)

### № 2
Ваня альтруист. Может помочь друзьям (одноклассникам), любому из обратившихся за помощью.

**Шаги (см. [раздел "Установка"](https://github.com/Padking/school-magazine-hacker/wiki#Установка)):**
- 1, 2, 3, 4, 8

### № 6
Если хочется доработать сайт электронного дневника в связке со скриптом.

**Шаги (см. [раздел "Установка"](https://github.com/Padking/school-magazine-hacker/wiki#Установка)):**
- 1, 5, 6, 7, 8

### Требования к окружению

* Python 3.7 и выше,
* Linux/Windows,
* Переменные окружения (ПеО).

Проект настраивается через ПеО, достаточно указать их в файле `.env`.
Передача значений ПеО происходит с использованием [environs](https://pypi.org/project/environs/).

#### Параметры проекта

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`ALLOWED_HOSTS`| Разрешённые хосты |`['0.0.0.0', '127.0.0.1', 'localhost']`|
|`DEBUG`| Режим отладки |`False`|
|`DJANGO_SETTINGS_MODULE`| Файл `script.py` |`project.settings`|
|`SECRET_KEY`| Уникальное непредсказуемое значение |-|

#### Параметры подключения к БД

По умолчанию, используется СУБД SQLite.

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`DB_SQLITE_NAME`| Имя БД | - |

### Установка

1. Клонирование проекта:
```bash
git clone https://github.com/Padking/school-magazine-hacker.git
cd school-magazine-hacker
```

2. `mv script.py` <path_to_target_site_where_manage.py_exist>

3. Изменить название предмета, по которому будем хвалить:

`subject` = 'Здесь название предмета, например, Математика'

4. Изменить фамилию и имя друга:

`first_and_last_name` = 'Здесь фамилия и имя друга, например, Фролов Иван'

5. Создание каталога виртуального окружения (ВО)*:

`mkvirtualenv -p` <path> <virtualenv's_name>

6. Cвязывание каталогов ВО и проекта:

`setvirtualenvproject` <virtualenv's_path> <project's_path>

7. Запуск сайта:
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

8. Запуск скрипта:
```bash
python script.py
```






\* с использованием [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)
