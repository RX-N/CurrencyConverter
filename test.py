import tkinter as tk
from tkinter import ttk
import csv
import requests


def load_currency_codes(file_path):
    currency_codes = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            currency_codes.append(row[0])
    return currency_codes


def convert_currency():
    key = '40H98M3QLBHI1OUH'
    frm = from_currency_var.get()
    to = to_currency_var.get()

    fnc = 'CURRENCY_EXCHANGE_RATE'
    base_url = 'https://www.alphavantage.co/query'
    url = f'{base_url}?function={fnc}&from_currency={frm}&to_currency={to}&apikey={key}'

    try:
        r = requests.get(url)
        data = r.json()
        rate = float(data['Realtime Currency Exchange Rate']
                     ['5. Exchange Rate'])
        amount = float(amount_entry.get())
        converted_amount = amount * rate
        result_label.config(text=f"{amount} {frm} = {converted_amount} {to}")
    except requests.exceptions.RequestException as e:
        result_label.config(text="Error: Failed to fetch conversion rate.")


def reverse_currencies():
    frm = from_currency_var.get()
    to = to_currency_var.get()
    from_currency_var.set(to)
    to_currency_var.set(frm)


# Create the main window
window = tk.Tk()
window.title("Currency Converter")

# Set the style
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0")
style.configure("TButton", background="#008080", foreground="white")

# Load currency codes from CSV
currency_codes = load_currency_codes('PhysicalCurrencyList.csv')

# Create labels, entry fields, and button
amount_label = ttk.Label(window, text="Amount:", style="TLabel")
amount_label.grid(row=0, column=0, padx=10, pady=10)

amount_entry = ttk.Entry(window)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

from_currency_label = ttk.Label(window, text="From Currency:", style="TLabel")
from_currency_label.grid(row=1, column=0, padx=10, pady=10)

from_currency_var = tk.StringVar(window)
# Default currency is the first code in the CSV
from_currency_var.set(currency_codes[0])

from_currency_menu = ttk.Combobox(
    window, textvariable=from_currency_var, values=currency_codes)
from_currency_menu.grid(row=1, column=1, padx=10, pady=10)

to_currency_label = ttk.Label(window, text="To Currency:", style="TLabel")
to_currency_label.grid(row=2, column=0, padx=10, pady=10)

to_currency_var = tk.StringVar(window)
# Default currency is the second code in the CSV
to_currency_var.set(currency_codes[1])

to_currency_menu = ttk.Combobox(
    window, textvariable=to_currency_var, values=currency_codes)
to_currency_menu.grid(row=2, column=1, padx=10, pady=10)

convert_button = ttk.Button(window, text="Convert",
                            command=convert_currency, style="TButton")
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
reverse_button = ttk.Button(window, text="Reverse",
                            command=reverse_currencies, style="TButton")
reverse_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(window, text="", style="TLabel")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
window.mainloop()
