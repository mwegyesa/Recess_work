class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        previous_salary = self._salary
        self._salary = new_salary
        return previous_salary

# Create objects of the Employee class
Emp1 = Employee("Comrade", 100000)
Emp2 = Employee("Robert", 500000)
Emp3 = Employee("Suzan", 800000)
Emp4=Employee("Kats", 300000)

# Increase salaries
Emp1_previous_salary = Emp1.set_salary(200000)
Emp2_previous_salary = Emp2.set_salary(600000)
Emp3_previous_salary = Emp3.set_salary(850000)
Emp4_previous_salary=Emp4.set_salary(250000)


# Displaying information about previous and current salary
print(f"{Emp1.get_name()}: My salary was increased from UGX {Emp1_previous_salary} to {Emp1.get_salary()}.")
print(f"{Emp2.get_name()}: My salary was increased from UGX {Emp2_previous_salary} to {Emp2.get_salary()}.")
print(f"{Emp3.get_name()}: My salary was increased from UGX {Emp3_previous_salary} to {Emp3.get_salary()}.")
print(f"{Emp4.get_name()}: My salary was increased from UGX {Emp4_previous_salary} to {Emp4.get_salary()}.")