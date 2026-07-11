import csv
import json

class Person:
    def __init__(self, name, id):      
        self.name = name               
        self.id = id


class Employee(Person):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, id, salary, bonus):
        super().__init__(name, id, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus


class FileHandler:
    def read_csv(self, filename):
        try:
            with open(filename, "r") as file:
                return list(csv.DictReader(file))
        except Exception as e:
            print("CSV Error:", e)
            return []

    def read_json(self, filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except Exception as e:
            print("JSON Error:", e)
            return []


class ReportGenerator:
    def generate_summary(self, employees):
        report = []
        for emp in employees:
            salary = emp.calculate_salary()
            status = "High Income" if salary > 50000 else "Normal"
            report.append([emp.name, emp.id, salary, status])
        return report

    def save_output(self, report):
        # Fixed newline argument
        with open("final_report.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "ID", "Salary", "Status"])
            writer.writerows(report)


fh = FileHandler()
employee_data = fh.read_csv("employees.csv")
bonus_data = fh.read_json("bonus.json")
employees = []

try:
    for e in employee_data:
        name = e["name"]
        id = e["id"]
        salary = float(e["salary"])
        bonus = bonus_data.get(id, 0)
        employees.append(Manager(name, id, salary, bonus))
except Exception as e:
    print("Data Error:", e)

rg = ReportGenerator()
report = rg.generate_summary(employees)
rg.save_output(report)

print("Final report saved successfully.")