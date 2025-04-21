#3 Implement an ADT and compute space and time complexities

class Employee:
    def __init__(self, name, id, department):
        self.__name = name
        self.__id = id
        self.__department = department

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_department(self, department):
        self.__department = department

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_department(self):
        return self.__department

    def __str__(self):
        print(f'Name: {self.__name}\nId: {self.__id}\nDepartment: {self.__department}')

# Type	Complexity
# Time	O(1)
# Space	O(1)