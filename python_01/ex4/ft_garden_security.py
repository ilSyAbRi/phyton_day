class   SecurePlant:
    def __init__(self,name):
        self.name = name
        self.__height = 0
        self.__age = 0

    def set_height(self,height):
        if (height < 0):
            return False
        else:
            self.__height = height
            return True

    def set_age(self, age):
        if (age < 0):
            return False
        else:
            self.__age = age
            return  True

    def get_height(self):
        return  self.__height

    def get_age(self):
        return  self.__age
