print("=" * 45)
print("       CALENDAR VERIFICATION SYSTEM")
print("=" * 45)

year = int(input("Enter year: "))

if year <= 0 or year < 1000 or year > 9999:
    print("Error: Enter a valid 4-digit year.")

else:
    if year % 400 == 0:
        status = "LEAP YEAR"
        reason = "Century year divisible by 400"
        days = 366
        february = 29

    elif year % 100 == 0:
        status = "COMMON YEAR"
        reason = "Century year not divisible by 400"
        days = 365
        february = 28

    elif year % 4 == 0:
        status = "LEAP YEAR"
        reason = "Divisible by 4 and not a century year"
        days = 366
        february = 29

    else:
        status = "COMMON YEAR"
        reason = "Not divisible by 4"
        days = 365
        february = 28

    print("=" * 45)
    print("Year:", year)
    print("Status:", status)
    print("Days in Year:", days, "days")
    print("Days in February:", february, "days")
    print("Reason:", reason)
    print("=" * 45)

    #Enter year: 2024
    