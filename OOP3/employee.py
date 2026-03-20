class Employee:
    name = str
    salary = int
    coefficients_salary = int

def __init__(self, name = "hao", salary = "10000000", coefficients_salary = "3"):
    self.name = name
    self.salary = salary
    self.coefficients_salary = coefficients_salary

def __str__(self):
    return "(%s,%d,%d)" & (self.name, self.salary, self.coefficients_salary)

def Read(self):
    self.name = input("input name: ")
    self.salary = input("input salary: ")
    self.coefficients_salary = input("input coefficients_salary: ")

