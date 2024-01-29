def calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years):
    # Calculates the monthly payment for a loan given the loan amount, 
    # annual interest rate, and loan term in years.
    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = annual_interest_rate / 100 / 12

    # Convert loan term from years to months
    loan_term_months = loan_term_years * 12

    # Calculate monthly payment using the formula for a fixed-rate loan
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**-loan_term_months)

    return monthly_payment

def main():
    # Get input from the user
    loan_amount = float(input("Enter the loan amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (%): "))
    loan_term_years = int(input("Enter the loan term in years: "))

    # Calculate the monthly payment
    monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years)

    # Display the result
    print(f"\nLoan Amount: ${loan_amount:.2f}")
    print(f"Annual Interest Rate: {annual_interest_rate:.2f}%")
    print(f"Loan Term: {loan_term_years} years")
    print(f"Monthly Payment: ${monthly_payment:.2f}")

if __name__ == "__main__":
    main()
