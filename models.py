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
        