print("Investment Calculator")

investment_amount = float(input("Enter a monthly investment amount between 0 and 50,000.: "))
while investment_amount < 0 or investment_amount > 50000:
    print("The investment amount enter is invalid.  Please try again")
    investment_amount = float(input("Enter a monthly investment amount between 0 and 50,000.: "))

rate = float(input("Enter an investment interest rate between 0 and 15: "))
while rate < 0 or rate > 15:
    print("The rate is too high or too low.  Please try again.")
    rate = float(input("Enter an investment interest rate between 0 and 15: "))

years = int(input("Enter the number of investment years. The number of years must be greater than 0.: "))
while years <= 0:
    print("The number of years is too low.  Please try again.")
    years = int(input("Enter the number of investment years. The number of years must be greater than 0.: "))

months = years * 12
monthly_interest_rate = rate / 12 / 100

future_value = 0

for month in range(1, months + 1):
    future_value += investment_amount
    monthly_interest_amount = future_value * monthly_interest_rate
    monthly_interest_amount = round(monthly_interest_amount, 2)
    future_value += monthly_interest_amount
    if month % 12 == 0:
        current_year = month // 12
        print(f"Year {current_year}: ${round(future_value, 2)}")


print("\nCalculation Summary")
print(f"Investment Duration: {years}")
print(f"Yearly Interest Rate: {rate}%")
print(f"Monthly Investment Amount: ${investment_amount}")
print(f"Future value: ${round(future_value, 2)}")

print("Completed by, Adair Salinas)")