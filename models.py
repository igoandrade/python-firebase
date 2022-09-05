class Employee():
    def __init__(self, name=None, email=None, age=None, address=None, employed=None):
        self.name = name
        self.email = email
        self.age = age
        self.address = address
        self.employed = employed

    def from_dict(dic):
        employee = Employee()
        attrs = ['name', 'email', 'age', 'address', 'employed']
        [setattr(employee, attr, dic[attr]) for attr in attrs]
        return employee

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'address': self.address,
            'employed': self.employed
        }

    def __repr__(self):
        return f"<Employee {self.email}>"