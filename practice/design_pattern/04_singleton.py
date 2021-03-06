# Singleton

class DataBase():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.__database_url = None
 
    @property
    def database_url(self):
        return self.__database_url
    
    @database_url.setter
    def database_url(self, database_url):
        self.__database_url = database_url

    def connect(self):
        pass

a = DataBase()
b = DataBase()

print(a==b)
print(id(a), id(b))

a.database_url = '128.1.1.1:5678'
print(a.database_url)
print(b.database_url)
