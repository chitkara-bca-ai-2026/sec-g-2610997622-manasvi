print("=" * 45)
print("          DATA CONVERSION UTILITY")
print("=" * 45)

product_name = input("Enter Product Name : ")
price = float(input("Enter Price        : "))
quantity = int(input("Enter Quantity     : "))

total_price = price * quantity
amount_str = str(total_price)

print("\n" + "-" * 50)
print("              TYPE CASTING SUMMARY")
print("-" * 50)
print("Variable        Value        Python Type")
print("-" * 50)

print("product_name   ", product_name, " ", type(product_name))
print("price          ", price, " ", type(price))
print("quantity       ", quantity, " ", type(quantity))
print("total_price    ", total_price, " ", type(total_price))
print("amount_str     ", amount_str, " ", type(amount_str))

print("\n" + "-" * 45)
print("                  TAX INVOICE")
print("-" * 45)
print("Product Name     :", product_name)
print("Price per Unit   : Rs.", price)
print("Quantity         :", quantity)
print("-" * 45)
print("Invoice Total    : Rs.", amount_str)
print("=" * 45)

#Enter Product Name : laptop
#Enter Price        : 45000.50
#Enter Quantity     : 2