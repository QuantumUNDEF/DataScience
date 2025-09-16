fd = open("Inventory2.txt", "r") 
products = fd.read().split("\n")
# print(products)
fd.close()
ui_prod_id = input("Enter Product ID: ")
ui_prod_qn = input("Enter Quantity: ")
updated_prod_lst = []
for product in products: 
    prod_details = product.split(',')
    # print(prod_details)
    # print((prod_details[0]) == (ui_prod_id))
    # print(prod_details[0])
    # print(type(prod_details[0]))
    # print(ui_prod_id)
    # print(type(ui_prod_id))
    if((prod_details[0]) == (ui_prod_id) ):
        if((int(ui_prod_qn) <= int(prod_details[3]) )):
            print('-'*50)
            print("Product Name: ",prod_details[1])
            print("Price       : ",prod_details[2])
            print("Quantity    : ",ui_prod_qn)
            print('-'*50)
            print("Billing Amount: ",int(prod_details[2]) * int(ui_prod_qn))
            print('-'*50)
            prod_details[3] = str(int(prod_details[3])- int(ui_prod_qn))
        else:
            print(f"Sorry, we're not have enough quantity.\nWe are having only {prod_details[3]} quantity.\nWould you like to purchase it?")
            ch = input("Press Y or N: ")
            if (ch == 'y' or ch =="Y"):
                print('-'*50)
                print("Product Name: ",prod_details[1])
                print("Price       : ",prod_details[2])
                print("Quantity    : ",ui_prod_qn)
                print('-'*50)
                print("Billing Amount: ",int(prod_details[2]) * int(prod_details[3]))
                print('-'*50)
                prod_details[3] = '0'
            else: 
                print("Thanks")
    updated_prod_lst.append(prod_details)
# print(updated_prod_lst)
lst = []
for i in updated_prod_lst:
    prod = i[0]+','+i[1]+','+i[2]+ ','+ i[3]+'\n'
    lst.append(prod)
# print(lst)
lst[-1] = lst[-1][:-1]       
fd = open("Inventory2.txt","w")
for i in lst:
    fd.write(i)
fd.close()
print("-"*50)
print("Inventory Updated!")