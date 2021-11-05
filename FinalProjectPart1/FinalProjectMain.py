#Wakif Ferdous
#1770041

from Product import *
from datetime import *


def initializeProducts():

    #Opening the manufacturer's list and then putting the products in a dictionary.

    products = {}
    csvFile = open("ManufacturerList.csv", "r")

    for csvLine in csvFile:
        parameters = csvLine.rstrip("\n").split(",")

        productId = int(parameters[0])
        productManufacturer = parameters[1]
        productType = parameters[2]
        productStatus = parameters[3]

        products[productId] = Product(productId, productManufacturer, productType, productStatus)

    csvFile.close()
    return products


def initializeProductCosts(products):

    #Opening the prices list and assigning prices to the products

    csvFile = open("PriceList.csv", "r")

    for csvLine in csvFile:
        parameters = csvLine.rstrip("\n").split(",")

        productId = int(parameters[0])
        productCost = int(parameters[1])

        if productId in products.keys():
            products[productId].setCost(productCost)

    csvFile.close()


def initializeProductServiceDates(products):

    #Opening the service date csvFile and assigning the service date to product

    csvFile = open("ServiceDatesList.csv", "r")

    for csvLine in csvFile:
        parameters = csvLine.rstrip("\n").split(",")

        productId = int(parameters[0])
        productServiceDate = datetime.strptime(parameters[1], "%m/%d/%Y")

        if productId in products.keys():
            products[productId].setServiceDate(productServiceDate)

    csvFile.close()


def writeProductsToCsvFile(csvFilename, products):

    #Creating a CSV file and writing the list of products to that file

    csvFile = open(csvFilename, "w")

    for product in products:
        csvFile.write(str(product.getId()) + ",")
        csvFile.write(product.getManufacturer() + ",")
        csvFile.write(product.getType() + ",")
        csvFile.write(str(product.getCost()) + ",")
        csvFile.write(datetime.strftime(product.getServiceDate(), "%m/%d/%Y") + ",")
        csvFile.write(product.getStatus())
        csvFile.write("\n")

    csvFile.close()


def createInventoryReport(products):

    #Creating a report by writing the products to a CSV File sorted by manufacturer and by type

    products = list(products.values())

    for i in range(len(products) - 1):
        for j in range(i + 1, len(products)):
            if products[i].getManufacturer() > products[j].getManufacturer():
                products[i], products[j] = products[j], products[i]
            elif products[i].getManufacturer() == products[j].getManufacturer() and products[i].getType() > products[j].getType():
                products[i], products[j] = products[j], products[i]

    writeProductsToCsvFile("FullInventory.csv", products)


def createProductsByTypeReport(targetProductType, products):

    #Creating a report that contains a specific product type and writing it to a CSV file

    targetProducts = []

    for product in products.values():
        if product.getType() == targetProductType:
            targetProducts.append(product)

    for i in range(len(targetProducts) - 1):
        for j in range(i + 1, len(targetProducts)):
            if targetProducts[i].getId() > targetProducts[j].getId():
                targetProducts[i], targetProducts[j] = targetProducts[j], targetProducts[i]

    writeProductsToCsvFile(targetProductType.capitalize() + "Inventory.csv", targetProducts)


def crateProductsReport(products):

    #Creating a report for each product

    productTypes = []

    for product in products.values():
        if product.getType() not in productTypes:
            productTypes.append(product.getType())

    for productType in productTypes:
        createProductsByTypeReport(productType, products)


def createProductPastServiceDateReport(products):

    #Creating a report where products have their service date lapsed

    todayDate = datetime.strptime(date.today().strftime("%m/%d/%Y"), "%m/%d/%Y")

    #Filtering those which have lapsed
    pastServiceDateProducts = list()

    for product in products.values():
        if product.getServiceDate() < todayDate:
            pastServiceDateProducts.append(product)

    #Arranging the products by date
    for i in range(len(pastServiceDateProducts) - 1):
        for j in range(i + 1, len(pastServiceDateProducts)):
            if pastServiceDateProducts[i].getServiceDate() > pastServiceDateProducts[j].getServiceDate():
                pastServiceDateProducts[i], pastServiceDateProducts[j] = pastServiceDateProducts[j], pastServiceDateProducts[i]

    writeProductsToCsvFile("PastServiceDateInventory.csv", pastServiceDateProducts)


def createDamagedProductsReport(items):

    #Creating a report for all damaged products

    #Getting damaged products
    damagedProducts = list()

    for product in items.values():
        if product.getStatus() == "damaged":
            damagedProducts.append(product)

    #Arranging by price
    for i in range(len(damagedProducts) - 1):
        for j in range(i, len(damagedProducts)):
            if damagedProducts[i].getCost() < damagedProducts[j].getCost():
                damagedProducts[i], damagedProducts[j] = damagedProducts[j], damagedProducts[i]

    writeProductsToCsvFile("DamagedInventory.csv", damagedProducts)


if __name__ == '__main__':

    #Loading the products and creating the necessary reports

    products = initializeProducts()

    initializeProductCosts(products)
    initializeProductServiceDates(products)

    createInventoryReport(products)
    crateProductsReport(products)
    createProductPastServiceDateReport(products)
    createDamagedProductsReport(products)
