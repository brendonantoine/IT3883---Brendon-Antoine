# Program Name: Assignment3.py (use the name the program is saved as)
# Course: IT3883/Section 114
# Student Name: Brendon Antoine 
# Assignment Number: Assingment 3
# Due Date: 10/3/2025
# Purpose: This program is an application that converts miles per gallon to kilometers per liter.
# List Specific resources used to complete the assignment. I have used the VSCode auto-formatting and auto-completion tools to help me with the indentation of my code.

import tkinter as tk
from tkinter import ttk, messagebox


MPG_TO_KML_FACTOR = 0.425143707

class FuelConverterApp:
    
    def __init__(self, master):
        self.master = master
        master.title("Fuel Economy Conversion")

        # --- Variables ---
        # StringVar to hold the user's input for MPG
        self.mpg_input = tk.StringVar()
        # StringVar to hold the calculated output for KML
        self.kml_output = tk.StringVar()
        
        # Link the input variable to the update function
        self.mpg_input.trace_add('write', self.live_convert)

        # --- Setup the UI ---
        self.setup_ui()

    def setup_ui(self):
        
        # Create a main frame for padding and organization
        main_frame = ttk.Frame(self.master, padding="20 20 20 20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 1. MPG Input Label and Entry
        ttk.Label(main_frame, text="Miles per Gallon (MPG):").grid(
            row=0, column=0, sticky=tk.W, pady=5, padx=5
        )
        self.mpg_entry = ttk.Entry(
            main_frame, width=15, textvariable=self.mpg_input, justify='right'
        )
        self.mpg_entry.grid(row=0, column=1, pady=5, padx=5)
        self.mpg_entry.focus() 

        # 2. Conversion Display Label
        ttk.Label(main_frame, text="Kilometers per Liter (KM/L):").grid(
            row=1, column=0, sticky=tk.W, pady=5, padx=5
        )

        # 3. KML Output Display
        self.kml_label = ttk.Label(
            main_frame, 
            textvariable=self.kml_output, 
            width=15, 
            anchor='e', 
            background='#e0e0e0',
            relief="sunken"
        )
        self.kml_label.grid(row=1, column=1, pady=5, padx=5, sticky=(tk.W, tk.E))
        
        # Adds note about the conversion factor
        ttk.Label(main_frame, text=f"Conversion Factor: 1 mpg = {MPG_TO_KML_FACTOR} km/l",
                  font=('TkDefaultFont', 8, 'italic')).grid(
            row=2, column=0, columnspan=2, pady=(15, 0)
        )

    def live_convert(self, *args):
        try:
            # 1. Get current input and attempt to convert to float
            mpg_str = self.mpg_input.get()
            
            # Handle empty input immediately
            if not mpg_str:
                self.kml_output.set("")
                return

            mpg_value = float(mpg_str)
            
            # 2. Performs the conversion
            kml_value = mpg_value * MPG_TO_KML_FACTOR
            
            # 3. Updates the output variable, formatted to 4 decimal places
            self.kml_output.set(f"{kml_value:.4f}")

        except ValueError:
            # This block executes if float(mpg_str) fails
            # Display an error message in the output field
            self.kml_output.set("Invalid Input")
            
            
            self.master.after(50, self.clean_input)

    def clean_input(self):
        current_input = self.mpg_input.get()
        cleaned_input = ""
        
        decimal_count = 0
        
        for char in current_input:
            if char.isdigit():
                cleaned_input += char
            elif char == '.' and decimal_count == 0:
                cleaned_input += char
                decimal_count += 1
            # Ignore all other characters (like letters)

        if cleaned_input != current_input:
            # Suppress the update function temporarily to prevent infinite recursion
            self.mpg_input.trace_remove('write', self.mpg_input.trace_info())
            self.mpg_input.set(cleaned_input)
            self.mpg_input.trace_add('write', self.live_convert)
            self.live_convert() # Recalculate with the cleaned input if needed

# --- Main Execution ---
if __name__ == "__main__":
    root = tk.Tk()
    app = FuelConverterApp(root)
    root.mainloop()