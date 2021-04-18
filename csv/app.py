import csv

def loadOrder(fileName):
    fileName = open("in.csv", "r")
    data = fileName.readlines()
    name = []
    price = []
    quantity = []
    totalCost = []
    for i in range(len(data)):
        x = data[i].split(" ")
        for i in range(len(data)):
            if i == 0:
                name.append(str(x[i]))
            if i == 1:
                price.append(float(x[i]))
            if i == 2:
                quantity.append(int(x[i]))
    print("\n", "YOUR ORDER", "\n")
    print(f'{"№":2}{"NAME":10}{"PRICE":10}{"QUANT.":8}{"TOTAL COST"}')
    print("-"*42)
    totalOrder = 0
    for i in range(len(data)):
        totalCost.append(price[i] * float(quantity[i]))
        print( f'{i+1} {name[i]:7} {price[i]:7} {quantity[i]:8} {totalCost[i]:10}' )
        print("_"*42, "\n")
        totalOrder += totalCost[i]
    print("TOTAL ORDER", totalOrder, " MDL", "\n" )


loadOrder("in.csv")
    




