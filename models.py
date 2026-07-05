class Workers:
    def __init__(self, id, name, last_name, age, post, salary):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.age = age
        self.post = post
        self.salary = salary
        
    def show_all(self):
        print(f'======\nID: {self.id} | Имя: {self.name} | Фамилия: {self.last_name}\nВозраст: {self.age}\nДолжность: {self.post} | Зарплата: {self.salary}\n=====')
        

class Transactions:
    def __init__(self, name, type, amount, reason):
        self.name = name
        self.type = type
        self.amount = amount
        self.reason = reason
        
    def show_history(self):
        print(f'=====\nИмя: {self.name}\nТип: {self.amount}\nРазмер: {self.amount}\nПричина: {self.reason}\n=====')