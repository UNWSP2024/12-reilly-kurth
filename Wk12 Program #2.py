#reilly kurth
#program 2
#4/24/2025

import tkinter

class Joes_Automotive:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive Services")
        self.services = { "Oil Change": 30.00, "Lube Job": 20.00,"Radiator Flush": 40.00,"Transmission Fluid": 100.00,"Inspection": 35.00,"Muffler Replacement": 200.00,"Tire Rotation": 20.00,}
        self.service_vars = {}
        row = 0
        for service, cost in self.services.items():
            var = tkinter.IntVar()
            self.service_vars[service] = var
            tkinter.Checkbutton(self.main_window, text=f"{service} - ${cost:.2f}", variable=var).grid(row=row, column=0, sticky="w", padx=10, pady=5)
            row += 1

        self.calc_button = tkinter.Button(self.main_window, text="Calculate Total", command=self.calculate_total)
        self.calc_button.grid(row=row, column=0, pady=10)
        self.total_label = tkinter.Label(self.main_window, text="Total: $0.00", font=("Arial", 12, "bold"))
        self.total_label.grid(row=row + 1, column=0, pady=10)
        tkinter.mainloop()

    def calculate_total(self):
        total = 0
        for service, var in self.service_vars.items():
            if var.get() == 1:
                total += self.services[service]
        self.total_label.config(text=f"Total: ${total:.2f}")

Joes_Automotive()