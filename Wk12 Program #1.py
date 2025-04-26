#reilly kurth
#program 1
#4/24/2025

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Calculate Miles per Gallon")

        #widget for gas that the car can hold
        self.gallons_label = tkinter.Label(self.main_window, text= "Enter the amount of gas in gallons that the car holds:")
        self.gallons_entry = tkinter.Entry(self.main_window)

        #number of miles on a full tank
        self.miles_label = tkinter.Label(self.main_window, text="Number of miles car can be driven on a full tank:")
        self.miles_entry = tkinter.Entry(self.main_window)

        #calculate miles per gallon
        self.mpg_button = tkinter.Button(self.main_window, text="Calculate MPG", command=self.calculate_mpg)
        self.mpg_label = tkinter.Label(self.main_window, text="Miles Per Gallon:")

        self.gallons_label.grid(row=0, column=0, padx=10, pady=10)
        self.gallons_entry.grid(row=0, column=1, padx=10, pady=10)

        self.miles_label.grid(row=1, column=0, padx=10, pady=10)
        self.miles_entry.grid(row=1, column=1, padx=10, pady=10)

        self.mpg_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.mpg_label.grid(row=3, column=0, columnspan=2, pady=10)

        tkinter.mainloop()

    def calculate_mpg(self):
        try:
            gallons = float(self.gallons_entry.get())
            miles = float(self.miles_entry.get())
            if gallons <= 0 or miles <= 0:
                self.mpg_label.config("Error: Enter a number greater than 0")
            else:
                mpg = miles/gallons
                self.mpg_label.config(text=f"MPG: {mpg:.2f}")
        except ValueError:
            self.mpg_label.config("Error: Enter valid numbers")

my_gui = MyGUI()
