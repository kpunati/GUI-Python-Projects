import tkinter as tk

service_prices = {
    "Oil Change": 26.00,
    "Lube Job": 18.00,
    "Radiator Flush": 30.00,
    "Transmission Flush": 80.00,
    "Inspection": 15.00,
    "Muffler Replacement": 100.00,
    "Tire Rotation": 20.00
}

def calculate_total():
    total = sum(service_prices[service] for service, var in service_vars.items() if var.get())
    total_label.config(text=f"Total Charges: ${total:.2f}")

root = tk.Tk()
root.title("Maintenance Services Calculator")

service_vars = {service: tk.IntVar() for service in service_prices}

for service, var in service_vars.items():
    checkbox = tk.Checkbutton(root, text=service, variable=var)
    checkbox.pack()

calculate_button = tk.Button(root, text="Calculate Total", command=calculate_total)
calculate_button.pack()

total_label = tk.Label(root, text="Total Charges:")
total_label.pack()

root.mainloop()
