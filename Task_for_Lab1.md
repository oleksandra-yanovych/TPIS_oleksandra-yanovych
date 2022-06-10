# **Лабораторна №1**

-----------------------------------
## Використайте наступні команди

-----------------------------------
### Використання modules

-----------------------------------
```python
# file: greetings.py
def hello():
    print("Hello!")

def hi():
    print("Hi!")

def morning():
    print("Good morning!")
```
Механізм імпорту
```python
# import module
dir()
import greetings
dir()
dir(greetings)
greetings.hello()

# import function
from greetings import hi
dir()
hi()

# renaming
from greetings import morning as always
dir()
always()
```

### Використання packages

--------------------------------------------
#### Структура пакету
типова структура пакету
```text
.                       <- the root project directory
└── phrases             <- a package
    ├── __init__.py     <- special module, says "phrases" is the package
    └── greetings.py    <- a module of "phrases" package
```
Зробити `greetings.py` частиною проекту
```sh
mkdir phrases
mv greetings.py phrases/
touch phrases/__init__.py
```
механізм імпорту
```python
# import package
dir()
import phrases
dir()
help(phrases)
phrases.greetings.hello()

#import module
dir()
from phrases import greetings
dir()
dir(greetings)
greetings.morning()

# import function
from phrases.greetings import hi
dir()
hi()
```
#### Виконання пакету
```text
.                       
└── phrases             
    ├── __init__.py     
    ├── __main__.py     <- special module which defines default execution
    └── greetings.py    
```

```python
cat <<CODE > phrases/__main__.py
from phrases.greetings import morning

if __name__ == "__main__":
    morning()
CODE
```

```sh
python -m phrases
```
#### Макет Python проект

-----------------------------------
простий проект
```text
.                           <- the root project directory
├── emailboot               <- a package
│   ├── __init__.py         <- special module, says "emailboot" is the package
│   ├── __main__.py         <- a default execution
│   ├── extra               <- an inner package
│   │   ├── __init__.py     <- special module, says "extra" is the inner package for "emailboot"
│   │   ├── users.py        <- a module of "extra" package
│   │   └── templates.py    <- a module of "extra" package
│   ├── data                <- an inner directory
│   │   └── template.txt    <- a file
│   ├── actions.py          <- a module of "emailboot" package
│   ├── items.py            <- a module of "emailboot" package
│   └── workflows.py        <- a module of "emailboot" package
├── setup.py                <- a packaging configuration (optional)
├── README.md               <- a description
└── requirements.txt        <- used packages (can be part of setup.py)
```

#### Управління пакетами з `pip`

----------------------------------------
[https://pypi.org](https://pypi.org) публічний репозиторій пакетів.

```sh
python -m pip
python -m pip list -h
python -m pip freeze -h
python -m pip list
python -m pip freeze
python -m pip install virtualenv
python -m pip freeze
python -m pip freeze > requirements.txt
```
#### Управління середовищем з `virtualenv`

-----------------------------------------
```sh
python -m pip install virtualenv
python -m virtualenv
python -m virtualenv venv
source venv/bin/activate
python -m pip install selenium
python -m pip list
deactivate
python -m pip list
```

### Документування коду

--------------------------------------
#### Форматування типів
Імпорт PEPs:
* [https://www.python.org/dev/peps/pep-0257/](https://www.python.org/dev/peps/pep-0257/)
* [https://www.python.org/dev/peps/pep-0287/](https://www.python.org/dev/peps/pep-0287/)

| Тип форматування | Опис | Формальна специфікація |
| ---------------- | ---- | ---------------------- |
| Google docstrings | Форма документації, рекомендована Google | Ні |
| reStructured Text | Офіційний стандарт документації Python | Так |
| NumPy/SciPy docstrings | Комбінація NumPy із перебудованими та Google Docstrings | Так |
| Epytext | Адаптація Epydoc на Python; Чудово підходить для розробників Java | Так |

Рекомндується reStructured Text. [https://www.sphinx-doc.org/en/master/](https://www.sphinx-doc.org/en/master/) є найбільш використованим інструментом для створення документації на основі формату reST.

#### Задокументуйте пакет

```python
# file: phrases/__init__.py
"""
The package contains well-known phrases.

For instance, if you need greetings, run ``from phrases import greetings`` and use them.
"""


# file: phrases/greetings.py
"""This module has greetings only."""
def hello():
    """Prints "Hello!"."""
    print("Hello!")

def hi():
    """
    Says "Hi!".
    Yes, just "Hi!".
    """
    print("Hi!")

def morning():
    print("Good morning!")
```

#### Вивчіть документацію
```python
import phrases
help()
# package
phrases
# module
phrases.greetings
# function
phrases.greetings.hi
phrases.greetings.morning
```

#### Перевірте документацію
```sh
source venv/bin/activate
python -m pip install pydocstyle
python -m pydocstyle phrases
```
Сприймате `extsoft/dp-151@ ef2995c` як рекомендується конфігурацією для `pydocstyle`.

### Посилання

-------------------------------------
* [https://docs.python.org/3/tutorial/modules.html](https://docs.python.org/3/tutorial/modules.html)
* [https://docs.python-guide.org/en/latest/writing/structure](https://docs.python-guide.org/en/latest/writing/structure)
* [https://extsoft.pro/python-project-structure/](https://extsoft.pro/python-project-structure/)
* [https://docs.python.org/3/library/__main__.html](https://docs.python.org/3/library/__main__.html)
* [https://docs.python.org/3/installing/index.html](https://docs.python.org/3/installing/index.html)
* [https://pypi.python.org/pypi/pip](https://pypi.python.org/pypi/pip)
* [https://snarky.ca/why-you-should-use-python-m-pip/](https://snarky.ca/why-you-should-use-python-m-pip/)
* [https://virtualenv.pypa.io/en/stable/](https://virtualenv.pypa.io/en/stable/)
* [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)
* [https://github.com/pyenv/pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
* [https://github.com/bees-hive/pem](https://github.com/bees-hive/pem)
* [https://www.python.org/dev/peps/pep-0257](https://www.python.org/dev/peps/pep-0257)
* [https://www.python.org/dev/peps/pep-0287](https://www.python.org/dev/peps/pep-0287)
* [https://www.sphinx-doc.org/en/master](https://www.sphinx-doc.org/en/master)
* [https://www.pydocstyle.org](https://www.pydocstyle.org)
* [https://extsoft.pro/static-code-analysis-in-python/](https://extsoft.pro/static-code-analysis-in-python/)


### Завдання

------------------------------------------
#### Опис завдання

------------------------------------------
Будь-ласка, напишіть програму, яка буде вітати корстувача, запитувати його/її і друкуватиме це число словами.
Наприклад, якщо користувач дає `9`, програма друкує `nine`. Щоб цього досягти потрібно:
* Знайдіть пакет на PYPI, який може перетворювати числа в слова.
* Додати `requirements.txt`.
* Створити пакет з логікою (він повинен бути розподілений між кількома модулями).
* Додати документацію, яка відповідає стандартним правилам `pydocstyle`.
* Налаштувати виконання за допомогою `python -m ...`.
* Залийте код проекту на GitHub.
* У файлі `README.md` додайте інструкцію з використання вашого пакету.

#### Для звітності
Надішліть посилання на ваш репозиторій на пошту `roman.i.bak@lpnu.ua`.
