# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка. Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, 
т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска сотрудников нашего банка.
## Как установить
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Создайте файл ".env" в вашей деректории проекта откройте его в любом текстовом редакторе.
## Переменные окружения
Замените USER,PASSWORD,HOST,PORT,NAME на свои данные БД.

Включение/выключение режима отладочного кода (по умолчанию False):
```
DEBUG=True
```
## Запуск
Запускать данный проект через командную строку, в которой изначально указывается путь к местонахождению скрипта `manage.py` и далее запуск:
``` cmd
python manage.py runserver
```
## Примечания
Пример работы данного проекта на ОС Windows через cmd:

![GIF 12 07 2024 1-13-02](https://github.com/user-attachments/assets/64bac1d6-fd92-42cc-baf4-9134c8d916f9)
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
