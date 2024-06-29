import matplotlib.pyplot as plt

class FinancialAnalyzer:
    def __init__(self, revenue, operating_expenses, interest_income, tax_expenses):
        self.revenue = revenue
        self.operating_expenses = operating_expenses
        self.interest_income = interest_income
        self.tax_expenses = tax_expenses

    def calculate_pbit(self):
        pbit = self.revenue - self.operating_expenses
        return pbit

    def calculate_pbt(self):
        pbit = self.calculate_pbit()
        pbt = pbit + self.interest_income
        return pbt

    def calculate_pat(self):
        pbt = self.calculate_pbt()
        pat = pbt - self.tax_expenses
        return pat

    def calculate_profitability_ratios(self):
        net_margin = (self.calculate_pat() / self.revenue) * 100
        return net_margin

    def display_results(self):
        print("Financial Analysis Results:")
        print(f"Revenue: ${self.revenue}")
        print(f"Operating Expenses: ${self.operating_expenses}")
        print(f"Interest Income: ${self.interest_income}")
        print(f"Tax Expenses: ${self.tax_expenses}\n")

        print(f"PBIT: ${self.calculate_pbit()}")
        print(f"PBT: ${self.calculate_pbt()}")
        print(f"PAT: ${self.calculate_pat()}")
        print(f"Net Margin: {self.calculate_profitability_ratios():.2f}%")

    def plot_results(self):
        labels = ['PBIT', 'PBT', 'PAT']
        values = [self.calculate_pbit(), self.calculate_pbt(), self.calculate_pat()]

        plt.figure(figsize=(8, 5))
        plt.bar(labels, values, color=['blue', 'orange', 'green'])
        plt.title('Financial Analysis Results')
        plt.ylabel('Amount ($)')
        plt.show()

    def save_analysis(self, filename='financial_analysis.txt'):
        with open(filename, 'w') as file:
            file.write("Financial Analysis Results:\n")
            file.write(f"Revenue: ${self.revenue}\n")
            file.write(f"Operating Expenses: ${self.operating_expenses}\n")
            file.write(f"Interest Income: ${self.interest_income}\n")
            file.write(f"Tax Expenses: ${self.tax_expenses}\n\n")

            file.write(f"PBIT: ${self.calculate_pbit()}\n")
            file.write(f"PBT: ${self.calculate_pbt()}\n")
            file.write(f"PAT: ${self.calculate_pat()}\n")
            file.write(f"Net Margin: {self.calculate_profitability_ratios():.2f}%\n")


# Example Usage
if __name__ == "__main__":
    try:
        # Taking user input for financial data
        revenue = float(input("Enter Revenue: "))
        operating_expenses = float(input("Enter Operating Expenses: "))
        interest_income = float(input("Enter Interest Income: "))
        tax_expenses = float(input("Enter Tax Expenses: "))

        # Creating an instance of FinancialAnalyzer
        analyzer = FinancialAnalyzer(revenue, operating_expenses, interest_income, tax_expenses)

        # Displaying results
        analyzer.display_results()

        # Plotting results
        analyzer.plot_results()

        # Save analysis to a file
        analyzer.save_analysis()

    except ValueError:
        print("Invalid input. Please enter numeric values for financial data.")
