import tkinter as tk
from tkinter import messagebox

class RestaurantApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurant Management System")

        # Variables
        self.subtotal = tk.DoubleVar()
        self.service_charge = tk.DoubleVar()
        self.state_tax = tk.DoubleVar()
        self.tip_percent = tk.DoubleVar()
        self.tip_amount = tk.DoubleVar()
        self.split = tk.IntVar()
        self.total = tk.DoubleVar()

        # Labels
        tk.Label(self.master, text="Subtotal:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        tk.Label(self.master, text="Service Charge (%):").grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        tk.Label(self.master, text="State Tax (%):").grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        tk.Label(self.master, text="Tip (%):").grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        tk.Label(self.master, text="Split By:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
        tk.Label(self.master, text="Total:").grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)

        # Entry fields
        self.subtotal_entry = tk.Entry(self.master, textvariable=self.subtotal)
        self.subtotal_entry.grid(row=0, column=1, padx=10, pady=5)

        self.service_charge_entry = tk.Entry(self.master, textvariable=self.service_charge)
        self.service_charge_entry.grid(row=1, column=1, padx=10, pady=5)

        self.state_tax_entry = tk.Entry(self.master, textvariable=self.state_tax)
        self.state_tax_entry.grid(row=2, column=1, padx=10, pady=5)

        self.tip_entry = tk.Entry(self.master, textvariable=self.tip_percent)
        self.tip_entry.grid(row=3, column=1, padx=10, pady=5)

        self.split_entry = tk.Entry(self.master, textvariable=self.split)
        self.split_entry.grid(row=4, column=1, padx=10, pady=5)

        self.total_entry = tk.Entry(self.master, textvariable=self.total, state='readonly')
        self.total_entry.grid(row=5, column=1, padx=10, pady=5)

        # Tip buttons
        tk.Button(self.master, text="10%", command=lambda: self.set_tip_percent(10)).grid(row=3, column=2, padx=5, pady=5)
        tk.Button(self.master, text="15%", command=lambda: self.set_tip_percent(15)).grid(row=3, column=3, padx=5, pady=5)
        tk.Button(self.master, text="20%", command=lambda: self.set_tip_percent(20)).grid(row=3, column=4, padx=5, pady=5)

        # Calculate button
        tk.Button(self.master, text="Calculate", command=self.calculate_total).grid(row=6, column=0, columnspan=2, pady=10)

        # Split button
        tk.Button(self.master, text="Split", command=self.split_bill).grid(row=6, column=2, columnspan=2, pady=10)

        # Reset button
        tk.Button(self.master, text="Reset", command=self.reset_values).grid(row=7, column=0, columnspan=2, pady=10)

    def set_tip_percent(self, percent):
        self.tip_percent.set(percent)

    def calculate_total(self):
        try:
            subtotal = float(self.subtotal.get())
            service_charge_percent = float(self.service_charge.get())
            state_tax_percent = float(self.state_tax.get())
            tip_percent = float(self.tip_percent.get())
            split = int(self.split.get())

            service_charge_amount = subtotal * (service_charge_percent / 100)
            state_tax_amount = subtotal * (state_tax_percent / 100)
            tip_amount = subtotal * (tip_percent / 100)

            total_amount = subtotal + service_charge_amount + state_tax_amount + tip_amount

            self.tip_amount.set(tip_amount)
            self.total.set(total_amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def split_bill(self):
        try:
            total_amount = float(self.total.get())
            split = int(self.split.get())

            if split <= 0:
                messagebox.showerror("Error", "Number of people must be greater than zero.")
            else:
                amount_per_person = total_amount / split
                messagebox.showinfo("Split Bill", f"The amount divided by {split} people is ${amount_per_person:.2f} per person.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def reset_values(self):
        self.subtotal.set(0)
        self.service_charge.set(0)
        self.state_tax.set(0)
        self.tip_percent.set(0)
        self.tip_amount.set(0)
        self.split.set(1)
        self.total.set(0)

def main():
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
