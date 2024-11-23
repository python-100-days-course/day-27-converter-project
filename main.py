# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 27 - Intermediate - Tkinter, *args, **kwargs and Creating GUI Programs
# Project - Miles to Km Converter

import tkinter as tk

# Function for converting miles to km and displaying results, triggered on button click
def convert_m_to_km():
    miles = float(miles_input.get()) # get the miles
    km = miles*1.609344 # convert
    km = '{:.2f}'.format(km) # reduce to 2 none zero decimals
    km_value_label.config(text=km) # display the km value

# Create a window
window = tk.Tk()
window.title("Miles to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# x and y padding value for all the components
pad = 10
# Initial Km value
km_value = 0

# <-------> 1st Row Components <------->
# Entry component to enter miles
miles_input = tk.Entry(width=10)
miles_input.insert(tk.END, "0")
miles_input.grid(column=1, row=0, padx=pad, pady=pad)
# Label component - "Miles" text
miles_label = tk.Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0) # used to place the component into the window
miles_label.config(padx=pad, pady=pad)

# <-------> 2nd Row Components <------->
# Label component - "is equal to" text
text_label = tk.Label(text="is equal to", font=("Arial", 12))
text_label.grid(column=0, row=1) # used to place the component into the window
text_label.config(padx=pad, pady=pad)
# Label component - km value
km_value_label = tk.Label(text=km_value, font=("Arial", 12))
km_value_label.grid(column=1, row=1) # used to place the component into the window
km_value_label.config(padx=pad, pady=pad)
# Label component - km text
km_text_label = tk.Label(text="Km", font=("Arial", 12))
km_text_label.grid(column=2, row=1) # used to place the component into the window
km_text_label.config(padx=pad, pady=pad)

# <-------> 3rd Row Component <------->
# Calculate button
button = tk.Button(text="Calculate", command=convert_m_to_km)
button.grid(column=1, row=2)

# Keeps the window on screen and listens for what the user will do to interact with it, stays at the end
window.mainloop()