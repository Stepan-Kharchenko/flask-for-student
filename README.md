# Teacher site
## О проекте
Это учебный проект, разработанный в качестве дополнения к bot_rep, а также идущий в резюме.
## Описание
Это сайт, написанный на Flask для помощи учителям физики и математики в составлении тестов и управлении ими, в управлении учениками и просмотре статистики.
## Демонстрация
## Структура проекта и краткое описание работы
```
teacher/
    templates/
        login/
            login.html
            registration_forms.html
            registration_end.html
        admin/
            add_exersize.html
            add_end.html
            panel.html
            statistic.html
            add_test.html
            test_end.html
        test/
            start.html
            test.html
            end.html
        base.html
        index.html
        start.html
    scripts/
        admin/
            __init__.py
            add.py
            test.py
        __init__.py
        login.py
        test.py
    images/
    static/
        scripts/
        styles/
            style.css
    app.py
    models.py
    utils.py
    learning.db
    README.md
    secret.env
    .gitignore
```
Краткое описание:
* templates - шаблоны
  * base.html - базовый шаблон, его наследуют все остальные с помощью jinja2
  * admin - шаблоны для админ-панели и всего, что с ней связно
  * login - шаблоны для входа и регистрации
  * test - шаблоны для прохождения теста
  * start.html и index.html - главные после и до регистрации соответственно
* scripts - короткие python скрипты для обработки запросов и рендеринга шаблонов (там по структуре все соответственно так же, как и в шаблонах)
* styles - стили css и скрипты JS (еще не добавлено)
* app.py - точка входа
* learning.db - все таблицы БД
* models.py - модели БД
* utils.py - вспомогательные функции
## Структура БД
![Здесь должны быть структура БД](/images/database_structure.png)
Будет изменена
## Перспективы
В дальнейшем планируется интеграция с bot_rep и диплой
