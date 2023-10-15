from datetime import datetime

name = input("Enter your name: ")

lists = '''
 rice    Rs 20/kg
 sugar   Rs 30/kg
 salt    Rs 10/kg
 oil     Rs 80/lt
 panner  Rs 110/kg
 maggi   Rs 50/kg
 boost   Rs 90/each
 colgate Rs 70/each '''

price = 0
pricelist = []
totalprice = 0
finalamount = 0
itemlist = []
quantitylist = []
plist = []

itemrates = {'rice':20,'sugar':30,'salt':20,'oil':80,'panner':110,'maggi':50,
             'boost':90,'colgate':70}
option = int(input("for list of items press 1: "))
if option == 1:
    print(lists)
for i in range(len(itemrates)):
    inp1 = int(input("if you want to buy press 1 or 2 for exist: "))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("Enter your items: ")
        quantity = int(input("Enter quantity: "))
        if item in itemrates.keys():
            price = quantity * (itemrates[item])
            pricelist.append((item,quantity,itemrates,price))
            totalprice += price
            itemlist.append(item)
            quantitylist.append(quantity)
            plist.append(price)
            GST = (totalprice * 5)/100
            finalamount = GST + totalprice
        else:
            print("Sorry you entered item is not available")
    else:
        print("You entered wrong number")
    bill = input("Can I bill the items yes or no: ")
    if bill == 'yes':
        pass
        if finalamount != 0:
            print(29*'=','SP Super Market',29*'=')
            print(32*'=','Ullagallu',32*'=')
            print('Name: ',name, 30*' ','Date:', datetime.now())
            print(75*'-')
            print('Sno', 15*' ','Items', 15*' ','Quantity',15*' ','Price',)

            for i in range(len(pricelist)):
                print(i,17*' ',itemlist[i],20*' ',quantitylist[i],20*' ',plist[i])
                print(75*'-')
                print('TotalAmount:',53*' ','Rs',totalprice)
                print('GST Amount: ',53*' ','Rs',GST)
                print(75*'-')
                print('FinalAmount:',53*' ','Rs',finalamount)
                print(75*'-')
                print(28*' ','Thanks for Visiting')
                print(75*'-')