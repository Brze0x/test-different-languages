# Запуск автотестов для разных языков интерфейса
В данном тесте мы выполняем следующий сценарий:
- Открываем страницу: http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/
- Проверяется наличие кнопки добавления в корзину


Управление языком интерфейса реализовано путём добавления хука инициализации `pytest_addoption` в файл `conftest.py` в корневой директории проекта. 
При запуске автотестов мы можем передать параметр `--language` с необходимым нам языком интерфейса. 
Пример запуска:
```bash
pytest --language=es test_items.py # запускаем тест с интерфейсом на Испанском языке
```


Предупреждения (DeprecationWarning) связаны с тем что что экземпляр FirefoxProfile() который мы используем в фикстуре browser для добавления пользовательского профиля в рамках данного теста, устарел.
И начиная с Selenium 4 вы должны использовать экземпляр класса Options.
```py
options = webdriver.FirefoxOptions()
options.set_preference("intl.accept_languages", user_language)
```

Это и другие задания вы можете выполнить самостоятельно присоеденившись к курсу [Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575/promo) на платформе [Stepik](https://stepik.org/)