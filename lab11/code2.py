# LAB 11
import psycopg2
from psycopg2 import Error
import csv

try:
    
    connection = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='*Danik3009!@*',
            host='localhost',
            port='5432'
        )
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Phonebooklab (
            fname TEXT,
            phone TEXT
        );
    """)
    print("""
    Выберите действие:
    1 — Загрузить данные из CSV
    2 — Ввести данные вручную
    3 — Обновить имя или номер
    4 — Получить данные из таблицы
    5 — Удалить данные
    6 — Просмотр с LIMIT и OFFSET
        """)    
    number = int(input())
    if number == 1:
        with open('data2.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader) 
            for row in reader:
                cursor.execute(
                "INSERT INTO Phonebooklab VALUES (%s, %s)",
                row
            )
    elif number ==2:
        print("Сколько людей вы хотели бы добавить. Напишите цифру")
        numnam = int(input())
        for i in range(numnam):
            print("Введите имя потом номер")
            name1 = input()
            number1 = input()
            postgres_insert_name= """ INSERT INTO Phonebooklab (fname,phone) VALUES (%s,%s)"""
            record_to_insert = (name1, number1)
            cursor.execute(postgres_insert_name, record_to_insert)     
        
    elif number ==3:    
        print("Что бы вы хотели поменять. Если имя то введите 1. Если номер то введите цифру 2")
        updatenum = int(input())
        if updatenum == 1:
            print("Введите номер телефона пользователя в которм вы хотие поменять имя")
            number1 = input()
            print("Введите новое имя")
            name1 = input()
            command = "UPDATE Phonebooklab SET fname=%s WHERE phone=%s"
            cursor.execute(command, (name1, number1))
            print("Имя успешно изменен")
        elif updatenum ==2:
            print("Введите имя пользователя в которм вы хотие поменять номер телефона")
            name1 = input()
            print("Введите новый номер")
            number1 = input()
            command = "UPDATE Phonebooklab SET phone=%s WHERE fname=%s"
            cursor.execute(command, (number1, name1))
            print("Номер успешно изменен")
    elif number ==4:
        print("Фильтр по имени цифра 1. Фильтр по номеру цифра 2. Вывести все цифра 3 ")
        nuuuuuum= int(input())
        if nuuuuuum == 1:
            print("Введите имя по которому нужно фильтровать")
            name3 = input()
            command = "SELECT * FROM Phonebooklab WHERE fname=%s"
            cursor.execute(command, (name3,))
            print(cursor.fetchall())
        elif nuuuuuum==2:
            print("Введите имя по которому нужно фильтровать")
            number3 = input()
            command = "SELECT * FROM Phonebooklab WHERE phone=%s"
            cursor.execute(command, (number3,))
            print(cursor.fetchall())
        elif nuuuuuum==3:
            command = "SELECT * FROM Phonebooklab"
            cursor.execute(command)
            print(cursor.fetchall())
    elif number ==5:
        print("Удалить по имени цифра 1. Удалить по номеру цифра 2")
        nuuuuuum= int(input())
        if nuuuuuum == 1:
            print("Введите имя по которому нужно удалить")
            name4 = input()
            command = "DELETE FROM Phonebooklab WHERE fname=%s"
            cursor.execute(command, (name4,))
        elif nuuuuuum==2:
            print("Введите имя по которому нужно удалить")
            number4 = input()
            command = "DELETE FROM Phonebooklab WHERE phone=%s"
            cursor.execute(command, (number4,))
    elif number == 6:
        
        print("Введите цифры для limit и offset")
        numer = int(input())
        numer1 = int(input())
        mycursor = connection.cursor()
        command = "SELECT * FROM Phonebooklab LIMIT %s OFFSET %s"
        mycursor.execute(command, (numer, numer1))
        print(mycursor.fetchall())
        
    connection.commit()

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")