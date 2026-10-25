# Практическое задание 2

Основной файл — [numpy-pandas-matplotlib.ipynb](numpy-pandas-matplotlib.ipynb).
В нём заполнены задания pandas, три графика, ответы и реализации NumPy.
Ноутбук выполнен по порядку: результаты и графики уже сохранены.
[HTML-копия](numpy-pandas-matplotlib.html) позволяет посмотреть результат без Jupyter.

Для части NumPy подготовлены [base_functions.py](base_functions.py) и
[base_functions_vectorised.py](base_functions_vectorised.py).
Ячейки `%%writefile` в ноутбуке создают эти же файлы при повторном запуске.

CSV-таблица находится рядом с ноутбуком. Если файла нет, ячейка загрузки скачивает
его по исходной ссылке из задания. Первая ячейка кода устанавливает версии
используемых библиотек из требований курса. При локальном запуске рабочая папка
ядра должна быть папкой `ml_task02`.

Для работы в IDE в корне проекта создано постоянное окружение `.venv`.
В меню выбора ядра ноутбука выберите Python из `.venv/bin/python`.
В нём установлены `ipykernel` и библиотеки задания. Окружение можно создать заново
из корня проекта командами:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r ml_task02/requirements-local.txt
```

Настройка `.vscode/settings.json` указывает этот интерпретатор по умолчанию.
Если для открытого ноутбука уже выбрано другое ядро, переключите его вручную.

## Проверка

- Python 3.12.3, NumPy 2.1.3, pandas 2.2.3, matplotlib 3.10.0, CatBoost 1.2.8.
- Все 26 ячеек кода выполнены без ошибок.
- Скрипт курса `run.py` проверил все шесть групп публичных тестов: `06/06`, `3.0/3.0`.
- В векторизованных функциях отсутствуют циклы, генераторы и списковые включения.
- Проверены сохранение исходных текстовых условий и экспорт в HTML:
  три графика SVG и мем встроены в файл.

Для повторного запуска публичных тестов скачайте их скриптом курса
`download_tests.py`, затем выполните `python run.py public_tests`.
Во время текущей проверки тесты распакованы в `/tmp/ml-task02-tests/public_tests`.

## Источники

- [Исходный шаблон и файлы задания](https://github.com/MSU-ML-COURSE/ML-COURSE-26-27/tree/main/tasks/base_task02).
- [Правила выполнения и сдачи](https://github.com/MSU-ML-COURSE/ML-COURSE-26-27/blob/main/tutorials/tutorial_tasks.md).
- [Работа с проверяющей системой](https://github.com/MSU-ML-COURSE/ML-COURSE-26-27/blob/main/tutorials/tutorial_test_system.md).

В папке `reference` сохранены исходный пустой ноутбук, описание задания и правила.
В соответствии с шаблоном сохранены формулировки, приведены код и текстовые
ответы, а функции NumPy вынесены в два файла с разрешёнными импортами.

Готовый мем про векторизацию NumPy взят с [CodeItBro](https://www.codeitbro.com/blog/funny-python-programming-memes).
Картинка: [assets/numpy_meme_internet.jpg](assets/numpy_meme_internet.jpg).
Источник: [assets/numpy_meme_source.txt](assets/numpy_meme_source.txt).
В ноутбуке картинка хранится во вложении markdown-ячейки и входит в HTML-копию.
