import tkinter as tk

def calculate_mpg():
    try:
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())
        mpg = miles / gallons
        result_label.config(text=f"MPG: {mpg:.2f}")
    except ValueError:
        result_label.config(text='Invalid Input')

root = tk.Tk()
root.title("MPG Calculator")

gallons_label = tk.Label(root, text="Enter gallons of gas:")
gallons_label.grid(row=0, column=0, padx=10, pady=5)
gallons_entry = tk.Entry(root)
gallons_entry.grid(row=0, column=1, padx=10, pady=5)

miles_label = tk.Label(root, text="Enter miles on a full tank:")
miles_label.grid(row=1, column=0, padx=10, pady=5)
miles_entry = tk.Entry(root)
miles_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_mpg)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
