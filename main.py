from database import add_staff, get_all, create_base, delete_staff
from models import Workers
from logic import add_staff_by_user, show_all, find_worker, delete_worker

while True:
    try:
        create_base()
        print('===Employee Manager===')
        print('Варианты действий:')
        print('1.Добавить сотрудника')
        print('2.Найти сотрудника')
        print('3.Список всех сотрудников')
        print('4.Удалить сотрудника')
        print('5.Выйти')
        choice = int(input('Введите номер действия: '))
        
        if choice == 1:
            add_staff_by_user()
            
        elif choice == 2:
            find_worker()
        
        elif choice == 3:
            show_all()
            
        elif choice == 4:
            delete_worker()
            
        
    except ValueError:
        print('Ошибка при вводе!')