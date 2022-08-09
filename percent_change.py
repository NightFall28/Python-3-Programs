def percent():
    original = float(input("Enter your original value: "))
    new = float(input("Enter your new value: "))
    percent_change = ((new - original) / original) * 100
    print("Percent Change: ",percent_change,"%")

percent()
