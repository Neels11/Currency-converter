from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import requests
import json
import mysql.connector
from datetime import datetime

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Neel@8010",
    database="currency_db"
)
cursor = db.cursor()

# API Functionality
def convert():
    url = "https://fast-currency-convertor.p.rapidapi.com/api/Fetch-Currency/"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    querystring = {"amount": amount, "fromCurrency": currency_1, "toCurrency": currency_2}

    if currency_2 == 'USD':
        symbol = '$'
    elif currency_2 == 'INR':
        symbol = '₹'
    elif currency_2 == 'EUR':
        symbol = '€'
    elif currency_2 == 'BRL':
        symbol = 'R$'
    elif currency_2 == 'CAD':
        symbol = 'CA $'

    headers = {
        "x-rapidapi-key": "e7f46694bamsh910269a2d6fd5c8p1d1b42jsne100b95c4ff8",
        "x-rapidapi-host": "fast-currency-convertor.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = json.loads(response.text)
    con_amount = symbol + data["value"]

    result['text'] = con_amount
    print(con_amount)
    
    # Insert Conversion into Database
    cursor.execute(
        "INSERT INTO conversion_history (from_currency, to_currency, amount, converted_value) VALUES (%s, %s, %s, %s)",
        (currency_1, currency_2, float(amount), con_amount)
    )
    db.commit()

# Show History Page
def show_history():
    history_page = Tk()
    history_page.geometry("800x500")
    history_page.title("Conversion History")

    Label(history_page, text="Conversion History", font=("Arial", 20)).pack(pady=10)

    columns = ("id", "from_currency", "to_currency", "amount", "converted_value", "conversion_date")
    tree = ttk.Treeview(history_page, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    tree.pack(fill=BOTH, expand=True)

    # Fetch Data from DB
    cursor.execute("SELECT * FROM conversion_history ORDER BY conversion_date DESC")
    for row in cursor.fetchall():
        tree.insert("", END, values=row)
        
    history_page.mainloop()


# GUI
def show_graph_page():
    base_currency = combo1.get()
    amount = value.get()
    if base_currency and amount:
        logn.destroy()
        import graph_page
        graph_page.launch_graph_page(base_currency, float(amount))


logn = Tk()
logn.geometry('730x500+50+50')
logn.resizable(0, 0)
logn.title('Convertor')
bgImage = ImageTk.PhotoImage(file='bluw.png')

bgLabel = Label(logn, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(logn, text='Currency Convertor', font=('Tahoma', 23, 'bold'), bg='white', fg='light sky blue')
heading.place(x=220, y=80)

# Main Frame
result = Label(logn, text="", width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivy 15 bold'), bg='white', fg='black')
result.place(x=260, y=160)

currency = ['CAD', 'BRL', 'EUR', 'INR', 'USD']

from_label = Label(logn, text="From", width=7, height=1, pady=0, padx=0, relief="flat", anchor=NW, font='Tahoma', bg='white', fg='light sky blue')
from_label.place(x=270, y=240)
combo1 = ttk.Combobox(logn, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo1['value'] = (currency)
combo1.place(x=260, y=270)

to_label = Label(logn, text="To", width=7, height=1, pady=0, padx=0, relief="flat", anchor=NW, font='Tahoma', bg='white', fg='light sky blue')
to_label.place(x=370, y=240)
combo2 = ttk.Combobox(logn, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo2['value'] = (currency)
combo2.place(x=370, y=270)

value = Entry(logn, width=16, justify=CENTER, font=('Tahoma'), relief=SOLID)
value.place(x=290, y=310)

button_convert = Button(logn, text="Convert", width=15, padx=5, height=1, bg='light sky blue', fg='white', font=('Tahoma'), command=convert)
button_convert.place(x=290, y=350)

button = Button(logn, text="History", width=10, padx=5, height=1, bg='light sky blue', fg='white', font=('Tahoma'), command=lambda: show_history())
button.place(x=260, y=400)

button_graph = Button(logn, text="Graph", width=10, padx=5, height=1, bg='light sky blue', fg='white', font=('Tahoma'), command=show_graph_page)
button_graph.place(x=380, y=400)

logn.mainloop()

