candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

for i in range(len(candyList)):
    print('[{}] {}'.format(i, candyList[i]))

def check_index(candy_index):
    try:
        candy_index = int(candy_index)
        try:
            candy_cart.append(candyList[int(candy_index)])
            return True
        except:
            return False
    except:
        return False


cont = True
maxc = len(candyList) - 1
candy_cart = []
candy_index = input('Enter number for your candy selection: ')
checkindex = check_index(candy_index)
while cont == True:
    while (checkindex == True) and (cont == True):
            cont = bool(input("More Candy?\nType anything for more, press enter to stop:  \n"))
            if cont == True:
                candy_index = input('Enter number for your candy selection:  ')
                checkindex = check_index(candy_index)
    while (checkindex == False) and (cont == True):
        print("Entered Invalad integer\nMust be number between 0 and {}\n".format(maxc))
        candy_index = input('Enter number for your candy selection: ')
        checkindex = check_index(candy_index)
print('\n\nYour selections are: {}'.format(candy_cart))
