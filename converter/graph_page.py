from tkinter import *
import requests
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def fetch_and_plot(base_currency, amount):
    url = "https://fast-currency-convertor.p.rapidapi.com/api/Fetch-Currency/"
    headers = {
        "x-rapidapi-key": "e7f46694bamsh910269a2d6fd5c8p1d1b42jsne100b95c4ff8",
        "x-rapidapi-host": "fast-currency-convertor.p.rapidapi.com"
    }
    currencies = ['CAD', 'BRL', 'EUR', 'INR', 'USD']
    exchange_rates = []

    for currency in currencies:
        if currency != base_currency:
            querystring = {"amount": str(amount), "fromCurrency": base_currency, "toCurrency": currency}
            response = requests.get(url, headers=headers, params=querystring)
            data = json.loads(response.text)
            # Remove commas from the value before converting to float
            exchange_rates.append(float(data["value"].replace(",", "")))

    # Plot
    fig, ax = plt.subplots()
    ax.bar([c for c in currencies if c != base_currency], exchange_rates, color='skyblue')
    ax.set_title(f'{amount} {base_currency} Compared with Other Currencies')
    ax.set_ylabel('Equivalent Value')
    ax.set_xlabel('Currencies')

    canvas = FigureCanvasTkAgg(fig, master=graph_page)
    canvas.get_tk_widget().pack()
    canvas.draw()


# GUI
def launch_graph_page(base_currency, amount):
    global graph_page
    graph_page = Tk()
    graph_page.geometry('730x500+50+50')
    graph_page.resizable(0, 0)
    graph_page.title('Graphical Representation')

    # Add Back Button
    back_button = Button(graph_page, text="⬅ Back", font=("Arial", 12), bg="light sky blue", fg="white", command=lambda: back_to_main())
    back_button.place(x=10, y=10)

    Label(graph_page, text=f"Base Currency: {base_currency}", font=("Arial", 14)).pack(pady=40)
    Label(graph_page, text=f"Amount: {amount}", font=("Arial", 14)).pack(pady=10)

    fetch_and_plot(base_currency, amount)

    graph_page.mainloop()


def back_to_main():
    graph_page.destroy()
    import currency_converter
