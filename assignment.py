#Kathy Nguyen
#PM
#Shopping Cart System with Dictionary


products = {
    "Carbonara Buldak Ramen": 3.00,
    "Da Vien Ube Matcha": 7.00,
    "Little Caesars Pizza": 10.00,
    "Seafood Boil": 25.00,
    "Water": .50,
}
#products and their prices must be listed with the same index
shopping_cart = {}
user_choice = 0
#so it forces u into menu

#option 1 item display
def display_items(products):
        for index, (key, value) in enumerate(products.items(), start=1):
            print("-------------------------")
            print(f"{index}. {key} ${value:.2f}")

        #formatting so its #. PRODUCT $price

#option 2 add products
def add_product(products):
    product_num = 0
    print("What item would you like to add to cart?")
    print("")
    for index, (key, value) in enumerate(products.items(), start=1):
               print("--------------------------------")
               print(f"{index}. {key} ${value:.2f}")
   
    product_num = int(input("Enter product number: "))
    #check the condiitons first before adding it into cart with while loop
    while product_num > 5 or product_num < 1:
        print("Invalid number! Please try again")
        product_num = int(input("Enter product number: "))
        #must loop until it actually add a product
    
    foods = list(products)

    item_to_add = foods[product_num - 1]

    quantity = int(input("How many do you want to add?: " ))
    
    if item_to_add not in shopping_cart:
        shopping_cart[item_to_add] = quantity
    else:
        shopping_cart[item_to_add] += quantity
        
    print(quantity, "", item_to_add,  "was added to your cart")
    
    #because index for a list starts at 0, the number the user adds will be off, hence why we add 1

    

#option 3 remove products from cart
def remove_cart(products):
    print("------------------")
    print("CURRENT SHOPPING CART")
    print("------------------")
    # len() == 0 to check if it has 0 elements because this list has strings (can't = 0)
    if len(shopping_cart) == 0:
        print("Shopping cart empty, add something first!")
        return
    #sends the user back to the main menu because they cant do anything from here
    
    for index, (key, value) in enumerate(shopping_cart.items(), start=1):
        print("--------------------------------")
        print(f"{index}. {key} {value}")
    product_remove = int(input("Enter product you want to remove: "))
    
    currentfood = list(shopping_cart)
    #below is index of the item we want to remove
    #removing it from our current food list
    remove = currentfood[product_remove - 1]
    
    if remove not in shopping_cart:
         print("Item is not in the cart")
    else:
        shopping_cart[remove] -= 1
        print(f"Removed 1 {remove} from your cart! {shopping_cart[remove]} left!")
         



def check_cart(products):
     #display the current cart
    print("------------------")
    print("CURRENT SHOPPING CART")
    print("------------------")
    print("Product                      Unit Price          Quantity         Line Total")
    print("--------------------------------------------------------------------------------------------------------")
    subtotal = 0
    total_items = 0
    for index, (key, value) in enumerate(shopping_cart.items(), start=1):
    
        price = products[key]
        #key of products is price in the product dictionary
        line_total = shopping_cart[key]*price
        subtotal += line_total
        total_items += value
        print(f"{index:<3}. {key:<24}  ${price:<15.2f}    {value:<14}      ${line_total:<.2f}")
        #just for aesthetics so they align well
    
            
    
    print("Total Items: ", total_items)
    print(f"Subtotal: ${subtotal:.2f}")
    #display 2 decimals

         


#total fucntionn
def total_price(products):
    subtotal = 0
    print("-------------------")
    print("CURRENT TOTAL")
    # price = 0
    print("-------------------")
    for item, quantity in shopping_cart.items():
        # print(item)
        price = products[item]
            #key of products is price in the product dictionary
        line_total = shopping_cart[item]*price
        subtotal += line_total
    print("$", subtotal)
    
    return subtotal

#set to 0 so it can be added into later
while user_choice != 6:
    #menu
    print("-------------------------------")
    print("SMART SHOPPING CART")
    print("-------------------------------")
    print(" ")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Current Shopping Cart")
    print("5. View Current Total")
    print("-------------------------------")
    print("6. Checkout!")
    user_choice = int(input("Enter your choice based off the numbers: "))
    #menu above always prints then asks where user wants to go
    #each choice below goes to designated function
    if user_choice == 1:
        display_items(products)
    elif user_choice == 2:
        add_product(products)
    elif user_choice == 3:
        remove_cart(products)
    elif user_choice == 4:
        check_cart(products)
    elif user_choice == 5:
        total = total_price()
    while user_choice < 1 or user_choice > 6:
        print("INVALID NUMBER, PLEASE TRY AGAIN")
        user_choice = int(input("Enter your choice based off the numbers: "))

#this imports the current month/day/year
import datetime
current_date = datetime.datetime.now().strftime("%m/%d/%Y")

final_total = 0
subtotal = 0
def checkout(subtotal, final_total, shopping_cart):
    print("==============================")
    print("CHECKOUT")
    print("==============================")
    print("")
    print(current_date)
    print("------------------------------")
    subtotal = total_price(products)


    #must check if theres even anything before we start
    #returns the user back to the main menu
    if len(shopping_cart) == 0:
        print("NOTHING IN CART TO CHECKOUT! Please add something to checkout")
        return
    #NO discount 
    if subtotal < 10: 
        subtotal = total
        print("Subtotal: $", subtotal)
        print("Discount: N/A")
        print("Final Total: $",final_total)
    #5% discount
    elif 10 <= subtotal < 20:
        final_total = subtotal - subtotal*0.05
        print("Subtotal: $", subtotal)
        print("Discount: 5%")
        print("Final Total: $",final_total)
    #10% discount
    elif 20 <= subtotal < 40:
        final_total = subtotal - subtotal*0.1
        print("Subtotal: $", subtotal)
        print("Discount: 10%")
        print("Final Total: $",final_total)
    #15% discount
    elif subtotal >= 40:
        final_total = subtotal - subtotal*0.15
        print("Subtotal: $", subtotal)
        print("Discount: 15%")
        print("Final Total: $",final_total)
#function callback
checkout(subtotal, final_total, shopping_cart)
print("")
print("==============================")
print("Thank you for shopping :D")