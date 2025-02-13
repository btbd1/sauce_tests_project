Задание для автоматизации тестирования на сайте Sauce Demo (https://www.saucedemo.com/)

Цель:
Разработать автоматизированные тесты для проверки функциональности интернет-магазина.

Описание задания
Тестируемая функциональность:
Основные функции сайта, которые будут покрыты тестами:

1 Авторизация.
2 Добавление товаров в корзину.
3 Оформление заказа.
4 Проверка сортировки товаров.


Тестовые сценарии:

Сценарий 1: Успешная авторизация
Шаги:
Перейти на страницу Sauce Demo.
Ввести корректные данные:
Username: standard_user.
Password: secret_sauce.
Нажать кнопку Login.
Ожидаемый результат:
Пользователь переходит на страницу со списком товаров.
Заголовок страницы: Products.

Сценарий 2: Ошибочная авторизация
Шаги:
Перейти на страницу Sauce Demo.
Ввести некорректные данные:
Username: wrong_user.
Password: wrong_password.
Нажать кнопку Login.
Ожидаемый результат:
Пользователь видит сообщение об ошибке: Epic sadface: Username and password do not match any user in this service.

Сценарий 3: Добавление товаров в корзину
Шаги:
Войти под учетной записью standard_user.
На странице продуктов выбрать два любых товара и нажать кнопку Add to cart.
Нажать на значок корзины в правом верхнем углу.
Ожидаемый результат:
В корзине отображаются оба выбранных товара.
Количество товаров в корзине указано корректно.



Сценарий 4: Удаление товара из корзины
Шаги:
Войти под учетной записью standard_user.
Добавить любой товар в корзину.
Перейти в корзину и удалить товар, нажав кнопку Remove.
Ожидаемый результат:
Товар удален из корзины.
Значок с количеством товаров не отображается (если корзина пуста).

Сценарий 5: Оформление заказа
Шаги:
Войти под учетной записью standard_user.
Добавить один или несколько товаров в корзину.
Перейти в корзину и нажать кнопку Checkout.
Заполнить данные на странице:
First Name: Test.
Last Name: User.
Postal Code: 12345.
Нажать кнопку Continue, а затем Finish.
Ожидаемый результат:
Появляется сообщение: THANK YOU FOR YOUR ORDER.

Сценарий 6: Проверка сортировки товаров
Шаги:
Войти под учетной записью standard_user.
Выбрать сортировку "Price (low to high)" из выпадающего меню.
Ожидаемый результат:
Товары отсортированы по возрастанию цены.
