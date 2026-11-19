import math

print("=" * 40)
print("     ENGINEERING CALCULATION TOOL")
print("=" * 40)

value = float(input("Enter a numerical value: "))
exponent = float(input("Enter an exponent: "))
decimal = float(input("Enter a decimal measurement: "))

power = math.pow(value, exponent)
square_root = math.sqrt(value)
ceil_value = math.ceil(decimal)
floor_value = math.floor(decimal)

print("\n--- Results ---")
print("Value              :", value)
print("Exponent           :", exponent)
print("Power (pow)        :", power)
print("Square Root (sqrt) :", f"{square_root:.4f}")
print("Decimal Value      :", decimal)
print("Ceil Value         :", ceil_value)
print("Floor Value        :", floor_value)
print("=" * 40)

#Enter a numerical value: 16
#Enter an exponent: 2
#Enter a decimal measurement: 4.7
