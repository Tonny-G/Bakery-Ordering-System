#ODERING SYSTEM FOR CRUSTIES PLACE BAKERY
from datetime import datetime, timedelta

start = 0
end = 0
orderNo = 0
tt = 0

menu = [
    "Sliced Bread", "Coconut Bread", "Donut", "Queen Cake", "Small Chops",
    "Chapati", "Pizza", "Meat Pie", "Sausage Roll", "Black Forest Cake"
]
menuNo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
price = [700, 600, 200, 300, 600, 60, 2000, 400, 250, 4500]
dur = [10, 13, 12, 16, 20, 18, 12, 12, 12, 14]

myorder = []
myprice = []
counter = 0
total = 0
print(" ~~~~~~~~~~~~~~~~~~~~~~~ ")
print("|       WELCOME         |")
print("|         TO            |")
print("| CRUSTIES PLACE BAKERY!|")
print(" ~~~~~~~~~~~~~~~~~~~~~~~ ")
print("    ")
print("Here is our MENU:  ")
print(" ||     ||           ")
print(" \/     \/           ")
print("*******************")
#Display Menu
for i in range(len(menu)):
    print(menuNo[i], menu[i], "----- Ksh", price[i])
print("*******************")
print("       ")
nextOrder = True  #To handle take order prompt

while nextOrder == True:
    valid = True  #To handle Finished Ordering prompt
    #Take order
    okay = True
    while okay == True:
        order = input(
            f"(\x1B[3mPress N for no order\x1B[0m)\nEnter Order number: ")

        if order == "1":
            myorder.append(menu[0])
            myprice.append(price[0])
            counter = counter + 1
            total = total + price[0]
            tt += dur[0]
            okay = False
        elif order == "2":
            myorder.append(menu[1])
            myprice.append(price[1])
            counter = counter + 1
            total = total + price[1]
            tt += dur[1]
            okay = False
        elif order == "3":
            myorder.append(menu[2])
            myprice.append(price[2])
            counter = counter + 1
            total = total + price[2]
            tt = dur[2]
            okay = False
        elif order == "4":
            myorder.append(menu[3])
            myprice.append(price[3])
            counter = counter + 1
            total = total + price[3]
            tt += dur[3]
            okay = False
        elif order == "5":
            myorder.append(menu[4])
            myprice.append(price[4])
            counter = counter + 1
            total = total + price[4]
            tt += dur[4]
            okay = False
        elif order == "6":
            myorder.append(menu[5])
            myprice.append(price[5])
            counter = counter + 1
            total = total + price[5]
            tt += dur[5]
            okay = False
        elif order == "7":
            myorder.append(menu[6])
            myprice.append(price[6])
            counter = counter + 1
            total = total + price[6]
            tt += dur[6]
            okay = False
        elif order == "8":
            myorder.append(menu[7])
            myprice.append(price[7])
            counter = counter + 1
            total = total + price[7]
            tt += dur[7]
            okay = False
        elif order == "9":
            myorder.append(menu[8])
            myprice.append(price[8])
            counter = counter + 1
            total = total + price[8]
            tt += dur[8]
            okay = False
        elif order == "10":
            myorder.append(menu[9])
            myprice.append(price[9])
            counter = counter + 1
            total = total + price[9]
            tt += dur[9]
            okay = False
        elif order == "N" or order == "n":
            okay = False
            valid = False
            nextOrder = False

        else:
            print("Wrong input.")
            okay = True
#Handle error in the Finished ordering prompt
#Loop incase of invalid entry
#valid = True
    while valid == True:
        finished = input("Have you finished ordering Y/N ")

        if finished == "N" or finished == "n":
            nextOrder = True
            valid = False
        elif finished == "Y" or finished == "y":
            nextOrder = False
            valid = False
        else:
            print("Invalid choice. Chose either 'y' or 'N'")
            valid = True
#Print Reciept
y = 0
print("      ")
print("Here is your Reciept:")
print("    ")
print("Ordered Items")
print("***************************")
#Loop over the order to display each
while y < counter:
    print(f"{myorder[y]} Ksh{myprice[y]}")
    y += 1
print("****************************")
print(f"The total price is Ksh {total}")
print("     ")

#Display order number, time it will take
orderNo += 1
start = datetime.now()
'{:%H:%M:%S}'.format(start)
end = start + timedelta(minutes=tt)

print("Order queue No: ", orderNo, "\n", "Will be ready in Min", tt,
      "\n Pick up time:", end)
