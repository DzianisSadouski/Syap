class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"оклад": wage, "премия": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["оклад"] + self._income["премия"]

данные_сотрудника = {"name": "Иван", "surname": "Иванов", "position": "Менеджер", "wage": 50000, "bonus": 10000}

должность = Position(**данные_сотрудника)

print("Полное имя:", должность.get_full_name())
print("Общий доход:", должность.get_total_income())
