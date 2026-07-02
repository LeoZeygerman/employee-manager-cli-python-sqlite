from database import add_staff, get_all
from models import Workers
while True:
    try:
        print('===Employee Manager===')
        print('Варианты действий:')
        print('1.Добавить сотрудника')
        print('2.Найти сотрудника')
        print('3.Список всех сотрудников')
        print('4.Удалить сотрудника')
        print('5.Выйти')
        choice = int(input('Введите номер действия: '))
        
        
    except ValueError:
        print('Ошибка при вводе!')