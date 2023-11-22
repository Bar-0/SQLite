def say_hello(a):
    print('Hello', a, '!')
name = 'Oleg'
say_hello(name)
name2 = 'Alexander'
say_hello(name2)

import sqlite3

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect('my_phonedatabase.db')

connection.close()
