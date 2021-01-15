class Employee:
    emCount = 0
    '所有员工的基类'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emCount += 1
        print('普通员工')

    def __del__(self):
        print("销毁")

    def showEmployeeCount(self):
        print("现在员工数量为：%d" % Employee.emCount)

    def showEmployee(self):
        print("员工的姓名为 {name} 工资为 {salary}".format(name=self.name, salary=self.salary))


# 创建第一个员工对象
employee1 = Employee("员工1", 4000)

# 创建第二个员工对象
employee2 = Employee("员工2", 5000)

employee1.showEmployee()
employee2.showEmployee()
print(Employee.emCount)

# 添加员工属性
employee1.age = 27
# 修改员工属性
employee1.age = 28
print(employee1.age)
del employee1.age

# 关于属性的方法
hasattr(employee1, 'age')
setattr(employee1, 'age', 27)
print(employee1.age)
getattr(employee1, 'age')
delattr(employee1, 'age')

del employee1


# 类的继承,可以继承多类
class specialEmployee(Employee):
    def __init__(self, name, salary):
        super(specialEmployee, self).__init__(name, salary)
        print('特殊员工')


s_employee = specialEmployee("特殊员工", 5000)
print(s_employee.showEmployee())
