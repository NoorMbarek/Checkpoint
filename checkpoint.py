import tkinter as tk

def convert_temp():
    fahrenheit = float(entry_fahrenheit.get())
    celsius = (fahrenheit - 32) * 5/9
    label_celsius.config(text=f"{celsius:.2f} \u00B0C")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create the Fahrenheit entry and label
label_fahrenheit = tk.Label(root, text="Fahrenheit")
label_fahrenheit.grid(row=0, column=0)

entry_fahrenheit = tk.Entry(root)
entry_fahrenheit.grid(row=0, column=1)

# Create the Celsius label
label_celsius = tk.Label(root, text="\u00B0C")
label_celsius.grid(row=1, column=0)

# Create the Convert button
button_convert = tk.Button(root, text="Convert", command=convert_temp)
button_convert.grid(row=2, column=0, columnspan=2)

# Run the main loop
root.mainloop()
