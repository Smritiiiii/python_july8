my_item = {

    "child1":{
    'name':'milk',
    'price':120,
    'quantity':5
    },

"child2":{
    'name':'wheat',
    'price': 300,
    'quantity':5
},
"child3":{
    'name':'egg',
    'price':35,
    'quantity':15
},
"child4":{
    'name':'bread',
    'price':100,
    'quantity':12
},
"child5":{
    'name':'sugar',
    'price':100,
    'quantity':30
    
    }

}

for x in my_item.items():
    print(x)


name1 = my_item["child1"]["name"] 
name2 = my_item['child2']["name"] 
name3 = my_item['child3']["name"] 
name4 = my_item['child4']["name"] 
name5 = my_item['child5']["name"]  

my_list = [name1, name2 , name3 , name4 , name5]

q1= my_item["child1"]["quantity"] 
q2= my_item['child2']["quantity"] 
q3= my_item['child3']["quantity"] 
q4= my_item['child4']["quantity"] 
q5= my_item['child5']["quantity"] 

my_list2 = [q1, q2, q3, q4, q5]

item_to_quantity = {name1: q1, name2: q2, name3: q3, name4: q4, name5: q5}

total_price= 0 

while True:
    cart = input("Enter the item you want to add to cart: ")
    quantity = int(input("Enter the quantity you want: "))

    if cart in my_list:
        if quantity <= item_to_quantity[cart]:
            price = my_item[f"child{my_list.index(cart) + 1}"]['price']
            total_price += quantity * price
            print(f"Adding {quantity} of {cart} to the cart.")
            item_to_quantity[cart] -= quantity  
        else:
            print("That quantity is not available.")
    else:
        print("The item entered is not available.")

    again = input("Do you want to make another purchase? (Y/N): ")
    if again == "N":
        break


print("\n---- Receipt ----\n")
print(f"\nTotal Price: {total_price}")