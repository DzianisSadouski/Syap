import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Создание таблицы вопросов
cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        correct_option TEXT
    )
''')

# Заполнение таблицы вопросов данными
questions_data = [
    ('Какое из этих языков программирования является интерпретируемым?', 'Java', 'C++', 'Python', 'C#', 'option3'),
    ('Какое из этих чисел является простым?', '7', '12', '15', '22', 'option1'),
    ('Какое из этих животных не летает?', 'Орел', 'Летучая мышь', 'Пингвин', 'Голубь', 'option3'),
    ('Как называется самый большой океан на Земле?', 'Атлантический', 'Индийский', 'Северный Ледовитый', 'Тихий', 'option4'),
    ('Какая планета является ближайшей к Солнцу?', 'Марс', 'Венера', 'Меркурий', 'Юпитер', 'option3'),
    ('Какой элемент периодической таблицы химических элементов имеет символ "Au"?', 'Серебро', 'Золото', 'Железо', 'Медь', 'option2'),
    ('Как называется наука о изучении звезд и вселенной?', 'Астрология', 'Геология', 'Астрономия', 'Метеорология', 'option3')
]

cursor.executemany('INSERT INTO questions (question, option1, option2, option3, option4, correct_option) VALUES (?, ?, ?, ?, ?, ?)', questions_data)

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()
