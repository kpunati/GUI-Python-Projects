import tkinter as tk

def conversion():
    celsius = float(celsius_entry.get())
    fahrenheit = (9 / 5) * celsius + 32
    result_label.config(text=str(fahrenheit) + "°F")

root = tk.Tk()
root.title("Celsius to Fahrenheit Program")

instructions_label = tk.Label(root, text="Enter a temperature in Celsius:")
instructions_label.pack()

celsius_entry = tk.Entry(root)
celsius_entry.pack()

convert_button = tk.Button(root, text="Convert", command=conversion)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
