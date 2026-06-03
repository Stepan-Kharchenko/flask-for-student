# Teacher site
## О проекте
Это учебный проект, разработанный в качестве дополнения к bot_rep, а также идущий в резюме.
## Описание
Это сайт, написанный на Flask для помощи учителям физики и математики в составлении тестов и управлении ими, в управлении учениками и просмотре статистики.
## Структура проекта и краткое описание работы
```
teacher/
    templates/
        login/
            lofin.html
            registration_forms.html
        admin/
            add_exersize.html
            panel.html
            statistic.html
        base.html
        index.html
        start.html
    scripts/
        admin/
            __init__.py
            add.py
        __init__.py
        login.py
        test.py
    images/
    static/
    app.py
    models.py
    utils.py
    learning.db
    README.md
    secret.env
    .gitignore
```
## Структура БД
![Здесь должны быть структура БД](/images/database_structure.png)
## Перспективы
В дальнейшем планируется интеграция с bot_rep
