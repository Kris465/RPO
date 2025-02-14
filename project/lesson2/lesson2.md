# Эхо-бот
## Задача 1. 

Разверните рабочее пространство, как было рассказано на прошлом уроке. Вы проделали это дома, так что проблем с тем, чтобы настроить систему контроля версий в классе и подуключить ее к редактору кода, у вас не должно возникнуть. Так же допустимо работать в онлайн-редакторе кода на GitHub. 

## Задача 2. 

Прочитайте про систему контроля версий и выучите первые четыре команды:

    git status
    git add название файла
    git commit -m "сообщение коммита, можно на русском"
    git push

Git — это распределённая система контроля версий, которая позволяет разработчикам отслеживать изменения в коде, совместно работать над проектами и управлять версиями файлов. Вот основные аспекты, которые стоит знать о Git:

▎Основные функции Git:

1. Отслеживание изменений: Git позволяет фиксировать изменения в файлах и отслеживать их историю. Это помогает понять, кто и когда вносил изменения.

2. Ветвление и слияние: Git поддерживает создание веток (branches), что позволяет разработчикам работать над новыми функциями или исправлениями ошибок изолированно от основной кодовой базы. Ветки можно затем сливать (merge) обратно в основную ветку.

3. Распределённая модель: Каждый разработчик имеет полную копию репозитория на своём компьютере, что позволяет работать офлайн и синхронизировать изменения с удалённым репозиторием (например, на GitHub) по мере необходимости.

4. Система коммитов: Изменения фиксируются в виде коммитов (commits), каждый из которых имеет уникальный идентификатор и может содержать сообщение о том, что было изменено.

5. Управление конфликтами: Если несколько разработчиков изменяют одни и те же строки кода, Git поможет разрешить конфликты, предлагая варианты выбора.

▎Основные команды Git:

• Инициализация репозитория: Создаёт новый репозиторий.
```shell
  git init
```

• Клонирование репозитория: Копирует существующий репозиторий на локальный компьютер.

```shell
  git clone <repository_url>
  
```

• Добавление изменений: Добавляет изменения в индекс для последующего коммита.

```shell
  git add <file_name>
```

• Коммит изменений: Фиксирует изменения с сообщением.

```shell
  git commit -m "Сообщение о коммите"
```

• Просмотр статуса: Показывает текущий статус репозитория (изменения, которые готовы к коммиту и т.д.).

```shell
  git status
```

• Просмотр истории коммитов: Показывает историю изменений в репозитории.

```shell
  git log
```

• Переключение между ветками: Позволяет перейти на другую ветку.

```shell
  git checkout <branch_name>
```

• Слияние веток: Сливает изменения из одной ветки в другую.

```shell
  git merge <branch_name>
```

▎Преимущества Git:

• Гибкость: Git подходит как для небольших проектов, так и для крупных командных разработок.

• Безопасность: Все изменения сохраняются локально, что снижает риск потери данных.

• Эффективность: Быстрая работа с большими проектами благодаря распределенной модели.

Git является стандартом де-факто для управления версиями в программной разработке. Он обеспечивает мощные инструменты для совместной работы и управления изменениями, что делает его незаменимым инструментом для разработчиков по всему миру.

## Задача 3.

Создайте файл main.py в репозитории индивидуального проекта и сделайте коммит о том, что работа над индивидуальным проектом начата.

## Задача 4. 

Создайте виртуальное окружение для python. Активируйте его. Добавьте папку виртуального окружения в исключения файла .gitignore. 

Напишите простейший скрипт и запуште изменения. Проверьте, что папка в виртуальным окружением НЕ появилась в удаленном репозитории на GitHub.

## Задача 5.

Прочитайте про программу pip и скачайте библиотеки с помощью пакетного менеджера:

pip — это пакетный менеджер для Python, который позволяет устанавливать, обновлять и управлять библиотеками и зависимостями, используемыми в проектах на Python. Вот основные моменты о pip:

▎Основные функции pip:

1. Установка пакетов: Позволяет устанавливать библиотеки из Python Package Index (PyPI) и других источников. Например:

```shell
   pip install package_name
```

2. Обновление пакетов: Обновляет уже установленные библиотеки до последней версии:

```shell
   pip install --upgrade package_name
```

3. Удаление пакетов: Удаляет установленные библиотеки:

```shell
   pip uninstall package_name
```

4. Список установленных пакетов: Показывает все установленные библиотеки в текущей среде:

```shell
   pip list
```

5. Создание файла зависимостей: Позволяет сохранить список всех установленных пакетов в файл (requirements.txt), что упрощает развертывание проекта на других машинах:

```shell
   pip freeze > requirements.txt
```

6. Установка из файла зависимостей: Устанавливает все пакеты, указанные в файле requirements.txt:

```shell
   pip install -r requirements.txt
```

▎Преимущества pip:

• Простота использования: Команды pip интуитивно понятны и легко запоминаются.

• Широкая поддержка: Поддерживает множество пакетов и библиотек, доступных на PyPI.

• Управление зависимостями: Позволяет легко управлять зависимостями проекта, что особенно полезно в больших приложениях.

Мы будем работать с минимум тремя библиотеками:

- aiogram (https://docs.aiogram.dev/en/latest/)
- loguru (https://loguru.readthedocs.io/en/stable/)
- python-dotenv (https://pypi.org/project/python-dotenv/)

Установите эти библиотеки в вируальное окружение проекта.

## Задача 6. 

Под руководством педагога на примере простейшего калькулятора пронаблюдайте как работают библиотеки loguru и python-dotenv.

## Задача 7.

В телеграме найдите бота с галочкой по имение @BotFather. Следуя подсказкам, создайте своего бота и получите заветный ключ для доступа к API телеграма.

~~~
Справка:
API (Application Programming Interface) — это набор правил и протоколов, который позволяет различным программам взаимодействовать друг с другом. API определяет, как запрашивать данные и функции у другого программного обеспечения, а также как оно должно реагировать на эти запросы.

▎Основные аспекты API:

1. Интерфейс: API предоставляет стандартизированный способ для приложений общаться между собой, скрывая сложные детали реализации.

2. Запросы и ответы: Обычно API работает по принципу «запрос-ответ». Клиент отправляет запрос к API (например, для получения данных), а сервер возвращает ответ (например, данные в формате JSON или XML).

3. Типы API:

   • Web API: Позволяет приложениям взаимодействовать через интернет (например, RESTful API, SOAP).

   • Библиотеки и фреймворки: Предоставляют функции и методы для разработки приложений на определённых языках программирования.

4. Использование: API широко используется для интеграции различных систем, создания мобильных и веб-приложений, а также для доступа к данным и функциональности сторонних сервисов (например, социальных сетей, платежных систем).

▎Примеры использования API:

• Получение данных о погоде из метеорологического сервиса.

• Интеграция с платёжными системами для обработки транзакций.

• Доступ к данным пользователей из социальных сетей.

~~~~~

## Задача 8.

Следуя инструкциям педагога, напишите эхо бота, используя ключ от API тг. Запустите и проверьте его работу.
