import tkinter
from tkinter import messagebox

class Long_Distance_Calls:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Long-Distance Call Rates")
        self.rate_categories = {"Daytime (6:00 AM - 5:59 PM)": 0.02, "Evening (6:00 PM - 11:59 PM)": 0.12, "Off-Peak (12:00 AM - 5:59 AM)": 0.05}
        self.rate_var = tkinter.StringVar(value="Daytime (6:00 AM - 5:59 PM)")
        tkinter.Label(self.main_window, text="Select Category:").pack(padx=10, pady=5)
        for category in self.rate_categories.keys():
            tkinter.Radiobutton(
                self.main_window, text=category, variable=self.rate_var, value=category).pack(padx=20)
        tkinter.Label(self.main_window, text="Number of Minutes:").pack(padx=10, pady=5)
        self.minutes_entry = tkinter.Entry(self.main_window, width=10)
        self.minutes_entry.pack(padx=20, pady=5)
        self.calc_button = tkinter.Button(self.main_window, text="Calculate Charge", command=self.calculate_charge)
        self.calc_button.pack(pady=10)
        tkinter.mainloop()

    def calculate_charge(self):
        try:
            selected_category = self.rate_var.get()
            rate = self.rate_categories[selected_category]
            minutes = float(self.minutes_entry.get())
            total_charge = rate * minutes
            messagebox.showinfo("Charge Calculation", f"Total Charge: ${total_charge:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for minutes.")

Long_Distance_Calls()