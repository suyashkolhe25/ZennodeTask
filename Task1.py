catalogue = {"Product A" : 20, "Product B" : 40, "Product C" : 50}

quanti_a = int(input("Enter the quantity of A: "))
isWrapped = input("Is this product wrapped as a gift (y/n): ")

wrapping_fee = 0

if isWrapped == 'y':
    wrapping_fee = quanti_a; 

quanti_b = int(input("Enter the quantity of B: "))
isWrapped = input("Is this product wrapped as a gift (y/n): ")

if isWrapped == 'y':
    wrapping_fee += quanti_b; 

quanti_c = int(input("Enter the quantity of C: "))
isWrapped = input("Is this product wrapped as a gift (y/n): ")

if isWrapped == 'y':
    wrapping_fee += quanti_c; 

sub_total = (quanti_a*catalogue["Product A"]) + (quanti_b*catalogue["Product B"])  + (quanti_c*catalogue["Product C"]) 


print("-----------------------BILL-----------------------")
quantity = 0
for key in catalogue.keys():
    print("")
    if (key == "Product A"):
        quantity = quanti_a
    elif (key == "Product B"):
        quantity = quanti_b
    elif (key == "Product C"):
        quantity = quanti_c
    print("Product Name: ", key)
    print("Product Quantity: ", quantity)
    print("Total Amount of Product A: ", quantity*catalogue[key])
    

print("\n--------------------------------------------------")

print("Subtotal: ", sub_total)

def flat_10_discount(sub_total):
    if (sub_total > 200):
        return (sub_total - 10)

def bulk_5_discount(quanti_a, quanti_b, quanti_c):
    price_a = quanti_a*catalogue["Product A"]
    price_b = quanti_b*catalogue["Product B"]
    price_c = quanti_c*catalogue["Product C"]

    if quanti_a > 10 : 
        price_a = (price_a)*0.95
    if quanti_b > 10 : 
        price_b = (price_b)*0.95
    if quanti_c > 10 : 
        price_c = (price_c)*0.95

    return (price_a + price_b + price_c)

def bulk_10_discount(quanti_a, quanti_b, quanti_c, sub_total):
    if ((quanti_a + quanti_b + quanti_c) > 20):
        return sub_total*0.9
    
def tiered_50_discount(quanti_a, quanti_b, quanti_c):
    total = 0
    discounted = 0
    if ((quanti_a + quanti_b + quanti_c) > 30):
        if (quanti_a > 15):
            total = (15*catalogue["Product A"]) + (((quanti_a - 15)*catalogue["Product A"])*0.5)
            discounted = 1

        if (quanti_b > 15):
            if ((total == 0) or (total > (15*catalogue["Product B"]) + (((quanti_b - 15)*catalogue["Product B"])*0.5))):
                total = (15*catalogue["Product B"]) + (((quanti_b - 15)*catalogue["Product B"])*0.5)
                discounted = 2

        if (quanti_c > 15):
            if ((total == 0) or (total > (15*catalogue["Product C"]) + (((quanti_c - 15)*catalogue["Product C"])*0.5))):
                total = (15*catalogue["Product C"]) + (((quanti_c - 15)*catalogue["Product C"])*0.5)
                discounted = 3

        if discounted == 1:
            total += (quanti_b*catalogue["Product B"]) + (quanti_c*catalogue["Product C"])
        elif discounted == 2:
            total += (quanti_a*catalogue["Product A"]) + (quanti_c*catalogue["Product C"])
        elif discounted == 3:
            total += (quanti_a*catalogue["Product A"]) + (quanti_b*catalogue["Product B"])

    return total
        
discount = flat_10_discount(sub_total)
discount_name = "flat_10_discount"
# print("flat 10 discount", discount)

bulk_5 = bulk_5_discount(quanti_a, quanti_b, quanti_c)
# print("bulk 5 discount", bulk_5)
if discount > bulk_5:
    discount = bulk_5
    discount_name = "bulk_5_discount"

bulk_10 = bulk_10_discount(quanti_a, quanti_b, quanti_c, sub_total)
# print("bulk_10 discount", bulk_10)
if discount > bulk_10:
    discount = bulk_10
    discount_name = "bulk_10_discount"

tiered_50 = tiered_50_discount(quanti_a, quanti_b, quanti_c)
# print("tiered_50 disc", tiered_50)
if ((discount > tiered_50) and (tiered_50 != 0)):
    discount = tiered_50
    discount_name = "tiered_50_discount"

print("Discount Name: ", discount_name)
print("Discount Amount: ", (sub_total - discount))

shipping_fee = 0
total_quantity = (quanti_a + quanti_b + quanti_c)
if (total_quantity % 10 != 0):
    shipping_fee = ((((total_quantity)//10)+1)*5)
else:
    shipping_fee = ((((total_quantity)//10))*5)

print("Shipping Fee: ", shipping_fee)
print("Wrapping Fee: ", wrapping_fee)

Total = discount + shipping_fee + wrapping_fee

print("Total: ", Total)
