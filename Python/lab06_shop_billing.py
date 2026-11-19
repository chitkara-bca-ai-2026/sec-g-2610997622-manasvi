print("=" * 40)
print("      CLOTHING STORE BILLING SYSTEM")
print("=" * 40)

customer_name = input("Enter Customer Name: ")
garment_name = input("Enter Garment Name: ")
price = float(input("Enter Price of one garment: "))
quantity = int(input("Enter Number of Garments: "))

total_amount = price * quantity

print("\n" + "=" * 40)
print("                  BILL")
print("=" * 40)

print("Customer Name  :", customer_name)
print("Garment Name   :", garment_name)
print("Price per Unit : Rs.", price)
print("Quantity       :", quantity)
print("Total Amount   : Rs.", total_amount)

print("=" * 40)

#Enter Customer Name: ravi kumar
#Enter Garment Name: shirt
#Enter Price of one garment: 500
#Enter Number of Garments: 3
