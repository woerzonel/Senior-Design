#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.filedialog
from pathlib import Path
from tkinter import *

from app.controllers.CreateBeerController import CreateBeerController


class CreateBeerView(tk.Frame):
    """Frame where user will input beers into the database"""

    def __init__(self, parent: tk.Frame, ctrl: tk.Tk, create_beer_ctrl: CreateBeerController):
        tk.Frame.__init__(self, parent)
        self.create_beer_controller = create_beer_ctrl
        self.beer_name_var = StringVar()
        self.brewer_var = StringVar(self.master)
        self.notes_var = []
        self.beer_type_var = StringVar(self.master)
        self.abv_var = StringVar()
        controller = ctrl
        breweries = self.create_beer_controller.get_breweries()
        notes = self.create_beer_controller.get_notes()
        beer_types = self.create_beer_controller.get_beer_types()

        home_button = tk.Button(self, text="Home Page", command=lambda: controller.show_frame("HomeView"))
        # home_button.pack(side="top", pady=10)
        home_button.grid(row=0, column=0, sticky="W")  # <- need to be formatted nicer

        page_label = tk.Label(self, text="Add a Beer")
        # page_label.pack(side="top", pady=10)
        # page_label.grid(row=0, column=1, sticky="W")
        page_label.grid(row=0, column=1, columnspan=5, sticky="WE")  # <- needs to be formatted nicer

        # beer name
        # TODO: figure out how to bring up virtual keyboard
        tk.Entry(self, textvariable=self.beer_name_var).grid(row=1, column=1)
        tk.Label(self, text="Beer Name").grid(row=1, column=0)

        # brewery
        OptionMenu(self, self.brewer_var, *breweries).grid(row=2, column=1)
        # ComboBox(self, textvariable=self.brewer_var, brewery_names).grid(row=2, column=1)  # attempt at ComboBox
        tk.Label(self, text="Brewery Name").grid(row=2, column=0)

        # notes TODO: change to side-by-side option picker
        tk.Label(self, text="Notes").grid(row=3, column=0)
        tk.Entry(self, textvariable=notes).grid(row=3, column=1)

        # beer type
        OptionMenu(self, self.beer_type_var, *beer_types).grid(row=4, column=1)
        tk.Label(self, text="Beer Type").grid(row=4, column=0)

        # ABV
        tk.Entry(self, textvariable=self.abv_var).grid(row=5, column=1)
        tk.Label(self, text="ABV").grid(row=5, column=0)

        # submit button
        tk.Button(self, text="Submit", command=self.do_submit).grid(row=6)

        tk.Button(self, text="Import From File", command=self.import_from_file).grid(row=7)

    def do_submit(self):
        regex = re.compile('^\d{1,2}(\.\d*)?$')
        abv = self.abv_var.get()
        if regex.match(abv):
            print('is a valid num')
            self.create_beer_controller.create_individual_beer(
                self.beer_name_var.get(),
                self.brewer_var.get(),
                self.notes_var,  # TODO: list selection interface
                self.beer_type_var.get(),
                float(abv))
        else:
            print('not a valid num')

    def import_from_file(self):
        home = str(Path.home())  # get platform independent home directory
        file_name = tkinter.filedialog.askopenfilename(
            initialdir=home,
            title='Select File to Import',
            filetypes=(('CSV', '*.csv'), ('EXCEL', '*.xlsx')))  # returns absolute path to file including name
        self.create_beer_controller.create_multiple_beer(file_name)
