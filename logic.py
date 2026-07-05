from database import add_staff, get_all, find_by_name, delete_staff, delete_by_id, find_by_id
from second_database import add_fine_bonus, create_base_fine
from models import Workers, Transactions

def add_staff_by_user():
    try:
        print('==Добавление сотрудника==')
        name = input('Введите имя сотрудника: ')
        last_name = input('Введите фамилию сотрудника: ')
        age = int(input('Введите возраст сотрудника: '))
        post = input('Введите должность сотрудника: ')
        salary = int(input('Введите зарплату сотрудника: '))
        worker = Workers(None, name, last_name, age, post, salary)
        worker.show_all()
        add_staff(worker)
    except ValueError:
        print('Ошибка при вводе!')
        
        
def show_all():
    workers = get_all()
    for worker in workers:
        worker.show_all()
        
def find_worker():
    name = input('Введите ID сотрудника, которого хотите найти: ')
    worker = find_by_id(name)
    for workers in worker:
        workers.show_all()
    print('Выберите, что хотите сделать: ')
    print('1. Добавить штраф или бонус.')
    print('2. Посмотреть историю бонусов и штрафов.')
    print('3. Выйти')
    choice = int(input('Ваш выбор: '))
    if choice == 1:
        print('1.Добавить штраф')
        print('2.Добавить бонус')
        fine_bonus = int(input('Ваш выбор: '))
        if fine_bonus == 1:
            type = 'Штраф'
            amount = int(input('Введите размер штрафа: '))
            reason = input('Введите причину штрафа: ')
            worker = add_fine_bonus(name,type,amount,reason)
            for workers in worker:
                workers.show_history()
            
        elif fine_bonus == 2:
            type = 'Бонус'
            amount = int(input('Введите размер бонуса: '))
            reason = input('Введите причину бонуса: ')
            worker = add_fine_bonus(name,type,amount,reason)
            worker.show_history()
            for workers in worker:
                workers.show_history()
        
        
def delete_worker():
    name = input('Введите имя или ID сотрудника, которого хотите удалить: ')
    worker = find_by_name(name)
    worker_id = find_by_id(name)
    if name.isdigit():
        delete_by_id(name)
        for workers in worker_id:
            print(f'Сотрудник {workers.name} удален!')
        
    else:
        delete_staff(name)
        for workers in worker:
            print(f'Сотрудник {workers.name} удален!')
    
        