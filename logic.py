from database import add_staff, get_all, find_by_name, delete_staff, delete_by_id, find_by_id
from models import Workers

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
    name = input('Введите имя сотрудника, которого хотите найти: ')
    worker = find_by_name(name)
    for workers in worker:
        workers.show_all()
        
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
    
        