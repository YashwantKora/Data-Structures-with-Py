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

    def get_name(self, name):
        return self.__name
    
    def get_id(self, id):
        return self.__id
    
    def get_department(self, department):
        return self.__department
    
    def __str__(self):
        print('Name:' + self.__name + \
        '\n Id:' + self.__id + \
        '\n Department:' + self.__department
        )
