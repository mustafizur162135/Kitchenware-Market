#dto design pattern
class User:

    def __init__(self, email, pw):
        self.__email=email #instance variable
        self.__pw=pw

    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        self.__email=email

    def getPw(self):
        return self.__pw
    def setPw(self, pw):
        self.__pw=pw
