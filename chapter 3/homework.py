print("*************computer bazzar************\n"
    "1:dell = (Rs.20000) 2:toshiba = (Rs.30000) 3:mac = (Rs.50000)")
option = int(input("select your option from :"))
dell_price = 0
toshiba_price = 0
mac_price = 0
quantity = 0
delivery_price = 0
plastic_price = 0
Bag_price = 0
Gift_Box_price = 0
location_price = 0
tax_price = 0


if option ==1:
    quantity = int(input("Enter the quantity:"))    
    dell_price = 20000*quantity
elif option == 2:
   quantity = int(input("Enter the quantity:"))
   toshiba_price = 30000*quantity

elif option == 3:
    quantity = int(input("Enter the quantity:"))
    mac_price = 20000*quantity

else:
    print("invalid")
    exit()

total_price = dell_price + toshiba_price + mac_price

print("1:home = (Rs.1000) 2:pickup = (free)")
delivery_option = int(input("select any option:"))
if delivery_option == 1:
    delivery_price = 1000
else:
    delivery_price = free   
print("1.plastic bags(Rs.500) 2.Bag(Rs.1000) 3.Gift Box(Rs.5000) 4.None")
packing_option = int(input("select any option:"))
if packing_option ==1:
    plastic_price = 500
elif packing_option ==2:
    Bag_price = 1000
elif packing_option ==3:
    Gift_Box_price = 5000

print("location: 1.Kathmandu(13%tax) 2.bhaktapur(free) 3.lalitpur(free)")
location_option = int(input("select any option:"))
if location_option == 1:
    tax_price = total_price*0.13
grand_total = total_price + delivery_price + plastic_price + Gift_Box_price + Bag_price + tax_price
print(f"Total Quantity :{quantity}\n Total:{total_price}\n Tax Amount:{tax_price}\n Grand Total:{grand_total}\n")






# grand_total = int(total_amount+taxable_amount)
# print(f"your total amount is {total_amount}")
# print(f"your taxable amount is {taxable_amount}")
# print(f"your grand total is {grand_total}")









