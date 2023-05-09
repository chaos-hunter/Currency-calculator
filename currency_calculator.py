import tkinter as tk
import IKE


def convert():
    amount = float(amount_entry.get())
    currency = currency_entry.get().upper()
    currency1 = new_currency_entry.get().upper()
    rate = IKE.get_exchange_rate(currency, currency1)
    new_amount = amount * rate
    result_label.configure(text=f"{amount:.2f} {currency} = {new_amount:.2f} {currency1}")


root = tk.Tk()
root.title("Currency Calculator")

# Create the widgets for the user interface
amount_label = tk.Label(root, text="Amount")
amount_entry = tk.Entry(root)
currency_label = tk.Label(root, text="Base Currency")
currency_entry = tk.Entry(root)
new_currency_label = tk.Label(root, text="New Currency")
new_currency_entry = tk.Entry(root)
button = tk.Button(root, text="Convert", command=convert)
result_label = tk.Label(root, text="")

# Layout the widgets using the grid geometry manager
amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1)
currency_label.grid(row=1, column=0)
currency_entry.grid(row=1, column=1)
new_currency_label.grid(row=2, column=0)
new_currency_entry.grid(row=2, column=1)
button.grid(row=3, column=0, columnspan=2)
result_label.grid(row=4, column=0, columnspan=2)
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=3)
root.geometry("300x300")

root.mainloop()
