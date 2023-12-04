# Тестовое задание. Django проект с функцией оплаты через Stripe.
#### Работа заключается в том, что при указании конкретного товара(item) или группы товаров(items), при нажатии кнопки купить, происходит перенаправление на форму оплаты через Stripe. Весь функционал реализован через api с возможностью визуализации с помощью простого html шаблона.
##### БД SQLite имеет следующие поля:
- name
- description
- price

##### При отправке GET запроса по /buy/{id}, можно получить Stripe Session Id для оплаты выбранного Item. При отправке GET запроса по /item/{id}, получаем простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy происходит запрос на /buy/{id}, и получение session_id и далее с помощью JS библиотеки Stripe происходит редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)


### Стек технологии:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/) [![SQLite](https://img.shields.io/badge/-SQLite-464646?style=flat-square&logo=SQLite)](https://www.sqlite.org/) [![stripe](https://img.shields.io/badge/-stripe-464646?style=flat-square&logo=stripe)](https://stripe.com/)

## Установка
### Клонировать репозиторий: https://github.com/VRN-lab/test_django_stripe_API

### Cоздать и активировать виртуальное окружение:
- python -m venv venv
- source venv/Scripts/activate
- python -m pip install --upgrade pip

### Установить зависимости из файла requirements.txt: 
- pip install -r requirements.txt

### Создать файл .env и записать SECRET_KEY_STRIPE, который нужно взять в своей учетной записи на сайте stripe.com, пример: 
- SECRET_KEY_STRIPE = sk_test_56594756739:AA1223242353446iISIDP--nq96YKHGmnb706xQLmM

### Так же в .env записать SECRET_KEY от django, он по умолчанию находится в файле setting.py .env, пример:
- SECRET_KEY = django-insecure-56594756739:AA1223242353446iISIDP--nq96YKHGmnb706xQLmM

### Соберать и запустить проект с Docker:
- docker-compose build
- docker-compose up

## Проект доступен по адресу http://45.67.56.69:8000/item/1/
### Для входа в панель администратора необходимо ввести логин и пароль "admin" по http://45.67.56.69:8000/admin

#### Можно переходить к тестированию проекта как через браузер так и через Postman:

### Автор:
#### Назипов Виктор
