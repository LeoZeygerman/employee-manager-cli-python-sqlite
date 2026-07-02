from database import add_staff, get_all
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
    find_name = input('Введите имя сотрудника: ')
    workers = get_all()
    for worker in workers:
        if worker.name == find_name:
            worker.show_all()
        else:
            print('Такого работника нет.')
        