#Wakif Ferdous
#1770041
class Product:

    def __init__(self, productId, productManufacturer, productType, productStatus):

    #Initializing a product

        self.__id = productId
        self.__manufacturer = productManufacturer
        self.__type = productType
        self.__status = productStatus
        self.__cost = 0
        self.__serviceDate = None

    def setCost(self, productCost):

    #Setting the price
        self.__cost = productCost

    def setServiceDate(self, productServiceDate):

    #Setting the service date

        self.__serviceDate = productServiceDate

    def getId(self):

    #Returning the ID

        return self.__id

    def getManufacturer(self):

    #Returning the manufacturer

        return self.__manufacturer

    def getType(self):

    #Returning the type

        return self.__type

    def getStatus(self):

    #Returning the status

        return self.__status

    def getCost(self):

    #Returning the cost

        return self.__cost

    def getServiceDate(self):

    #Returning the service date

        return self.__serviceDate
