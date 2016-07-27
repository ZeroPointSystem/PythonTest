import csv
from tkinter import *
from tkinter import ttk

from matplotlib import pyplot as plt


class ComboBoxDemo(ttk.Frame):
    def __init__(self, countries):
        ttk.Frame.__init__(self, name='demo')

        self.pack(expand=Y, fill=BOTH)
        self.master.title('Refugees')
        self.isapp = True

        panel = Frame(self)
        panel.pack(side=TOP, fill=BOTH, expand=Y)

        cbp = ttk.Labelframe(panel, text='Countries')

        cb = ttk.Combobox(cbp, values=tuple(countries), state='readonly')

        self.cb = cb

        cb.pack(pady=5, padx=10)

        cbp.pack(in_=panel, side=TOP, pady=5, padx=10)

        cb.bind('<<ComboboxSelected>>', self.onCountrySelected)

    def onCountrySelected(self, event):

        selectedCountry = self.cb.get()

        plt.title(selectedCountry)

        x_series = []
        y_series = []

        for pair in plotDictionary.get(selectedCountry):

            y = list(pair.values())[0]

            if y != '*' and y != '':
                x_series.append(int(list(pair.keys())[0]))
                y_series.append(int(y))

        plt.title(selectedCountry)

        plt.plot(x_series, y_series)
        #
        plt.show()

plotDictionary = {str: [{int: int}]}

# fileDictionary = {'Refugees (incl. refugee-like situations)': [],
#                   'Year': [],
#                   'Stateless persons': [],
#                   'Internally displaced persons (IDPs)': [],
#                   'Others of concern': [],
#                   'Total Population': [],
#                   'Returned IDPs': [],
#                   'Country / territory of asylum/residence': [],
#                   'Origin': [],
#                   'Asylum-seekers (pending cases)': [],
#                   'Returned refugees': []}

with open('C:/Users/Zetro/Downloads/unhcr_popstats_export_persons_of_concern_all_data.csv') as file:

    for row in csv.DictReader(file):

        nextCountry = row['Country / territory of asylum/residence']
        year = row['Year']
        refugees = row['Refugees (incl. refugee-like situations)']

        if nextCountry in plotDictionary:
            plotDictionary.get(nextCountry).append({year: refugees})
        else:
            plotDictionary[nextCountry] = [{year: refugees}]

ComboBoxDemo(plotDictionary.keys()).mainloop()
