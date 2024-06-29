import tkinter as tk
from tkinter import ttk

class HostelBalanceSheetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hostel Balance Sheet")

        self.style = ttk.Style()
        self.style.configure('TButton', foreground='green',background='black')
        self.style.configure('TLabel', background='lightgray')
        self.style.configure('TEntry', fieldbackground='white')

        # Initialize variables
        self.assets = {}
        self.liabilities = {}
        self.equity = {}

        # Create labels and entry fields for entering data
        self.create_label_and_entry("Asset Name:", self.add_asset)
        self.create_label_and_entry("Asset Value:", self.add_asset_value)
        self.create_label_and_entry("Liability Name:", self.add_liability)
        self.create_label_and_entry("Liability Value:", self.add_liability_value)
        self.create_label_and_entry("Equity Name:", self.add_equity)
        self.create_label_and_entry("Equity Value:", self.add_equity_value)


        self.display_button = ttk.Button(root, text="Display Balance Sheet", command=self.display_balance_sheet, style="TButton")
        self.display_button.pack(pady=10)

        # Create a frame to hold the balance sheet text and add a scrollbar
        self.frame = ttk.Frame(root)
        self.frame.pack(fill="both", expand=True)
        
        self.balance_sheet_text = tk.Text(self.frame, height=20, width=50, wrap=tk.WORD)
        self.balance_sheet_text.pack(side="left", fill="both", expand=True)
        
        self.scrollbar = ttk.Scrollbar(self.frame, command=self.balance_sheet_text.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.balance_sheet_text.config(yscrollcommand=self.scrollbar.set)

    def create_label_and_entry(self, label_text, callback):
        frame = ttk.Frame(self.root)
        frame.pack(padx=10, pady=5, fill="x")

        label = ttk.Label(frame, text=label_text)
        label.pack(side="left", padx=5)

        entry = ttk.Entry(frame)
        entry.pack(side="left", padx=5)

        add_button = ttk.Button(frame, text="Add", command=lambda: callback(entry.get()))
        add_button.pack(side="left", padx=5)

    def add_asset(self, asset_name):
        if asset_name:
            self.assets[asset_name] = 0

    def add_asset_value(self, asset_value):
        if self.assets and asset_value:
            asset_name = list(self.assets.keys())[-1]
            self.assets[asset_name] = float(asset_value)

    def add_liability(self, liability_name):
        if liability_name:
            self.liabilities[liability_name] = 0

    def add_liability_value(self, liability_value):
        if self.liabilities and liability_value:
            liability_name = list(self.liabilities.keys())[-1]
            self.liabilities[liability_name] = float(liability_value)

    def add_equity(self, equity_name):
        if equity_name:
            self.equity[equity_name] = 0

    def add_equity_value(self, equity_value):
        if self.equity and equity_value:
            equity_name = list(self.equity.keys())[-1]
            self.equity[equity_name] = float(equity_value)

    def calculate_total_assets(self):
        return sum(self.assets.values())

    def calculate_total_liabilities(self):
        return sum(self.liabilities.values())

    def calculate_total_equity(self):
        return sum(self.equity.values())

    def display_balance_sheet(self):
        self.balance_sheet_text.delete(1.0, tk.END)
        self.balance_sheet_text.insert(tk.END, "College Hostel Balance Sheet\n", "header")
        self.balance_sheet_text.insert(tk.END, "---------------------------\n")
        self.balance_sheet_text.insert(tk.END, "Assets:\n")
        for asset, value in self.assets.items():
            self.balance_sheet_text.insert(tk.END, "{}: {}\n".format(asset, value))
        self.balance_sheet_text.insert(tk.END, "---------------------------\n")
        self.balance_sheet_text.insert(tk.END, "Total Assets: {}\n\n".format(self.calculate_total_assets()))
        self.balance_sheet_text.insert(tk.END, "Liabilities:\n")
        for liability, value in self.liabilities.items():
            self.balance_sheet_text.insert(tk.END, "{}: {}\n".format(liability, value))
        self.balance_sheet_text.insert(tk.END, "---------------------------\n")
        self.balance_sheet_text.insert(tk.END, "Total Liabilities: {}\n\n".format(self.calculate_total_liabilities()))
        self.balance_sheet_text.insert(tk.END, "Equity:\n")
        for item, value in self.equity.items():
            self.balance_sheet_text.insert(tk.END, "{}: {}\n".format(item, value))
        self.balance_sheet_text.insert(tk.END, "---------------------------\n")
        self.balance_sheet_text.insert(tk.END, "Total Equity: {}\n".format(self.calculate_total_equity()))


        self.balance_sheet_text.tag_configure("header", foreground="blue", font=("Arial", 12, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    app = HostelBalanceSheetApp(root)
    root.mainloop()
