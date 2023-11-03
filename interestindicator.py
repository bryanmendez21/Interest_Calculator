def main():
    # collect the necessary inputs: principal, interest rate, years
    principal = float(input("input the loan amount: "))
    apr = float(input("the annual interest rate: "))
    years = int(input("input amont of years: "))

    # calculate the monthly payment
    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = (
        principal
        * monthly_interest_rate
        / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
    )

    # show to the user
    print("the monthly payment for this loan is: $ %.2f" % monthly_payment)


print("this is a monthly payment loan calculator")
print("")
run = ["c", "C"]
# runs program
while True:
    proceed = input("press c to continue or q to quit: ")
    if proceed in run:
        main()
    elif proceed == "q" or "Q":
        break
