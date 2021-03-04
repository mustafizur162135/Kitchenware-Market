#for each database table create one and define necessary get set methods
class Product:
    #constructor
    def __init__(self, id, name, price, qnt, upldate, imgpath):
        self.__id=id
        self.__name=name
        self.__price=price
        self.__qnt=qnt
        self.__upldate=upldate
        self.__imgpath=imgpath

    def getId(self):
        return self.__id
    def setId(self, id):
        self.__id=id

    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name=name

    def getPrice(self):
        return self.__price
    def setPrice(self, price):
        self.__price=price

    def getQnt(self):
        return self.__qnt
    def setQnt(self, qnt):
        self.__qnt=qnt

    def getUpldate(self):
        return str(self.__upldate)
    def setUpldate(self, upldate):
        self.__upldate=upldate

    def getImgpath(self):
        return self.__imgpath
    def setImgpath(self, imgpath):
        self.__imgpath=imgpath
