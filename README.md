# Тестовое задание для Ranks

## Описание

Доступ к платежной системе Stripe через страницу покупки товара /item/{id}. На данной странице указана информация о выбранном товаре и кнопка Buy. При нажатии на кнопку Buy происходит запрос на /buy/{id}, получение session_id и далее  с помощью javascript библиотеки Stripe происходит редирект на Checkout форму stripe для оформления оплаты товара.


## Установка и запуск

- Клонируйте новый репозиторий себе на компьютер.
- Разверните в репозитории виртуальное окружение, в папке скачанного репозитория выполните команду: `python -m venv venv` .
- Активируйте виртуальное окружение.
- В виртуальном окружении установите зависимости: `pip install -r requirements.txt` .
- Для запуска сервера введите: `python manage.py runserver`.
- Перед началом использования сайта необходимо выполнить миграции (`python manage.py migrate`), создать суперпользователя (`python manage.py createsuperuser`) и собрать статику (`python manage.py collectstatic`).


## Стек технологий

- asgiref==3.5.1
- autopep8==1.6.0
- certifi==2021.10.8
- charset-normalizer==2.0.12
- click==8.1.3
- colorama==0.4.4
- Django==3.2
- djangorestframework==3.13.1
- djlint==1.0.3
- idna==3.3
- importlib-metadata==4.11.3
- pathspec==0.9.0
- pycodestyle==2.8.0
- pytz==2022.1
- PyYAML==6.0
- regex==2022.4.24
- requests==2.27.1
- sqlparse==0.4.2
- stripe==3.0.0
- toml==0.10.2
- tomli==2.0.1
- tqdm==4.64.0
- tzdata==2022.1
- urllib3==1.26.9
- zipp==3.8.0


## Автор

Рустам Вахитов
