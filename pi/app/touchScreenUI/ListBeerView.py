#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.ttk import Treeview

from app.controllers.ListBeerController import ListBeerController


class ListBeerView(Frame):
    def __init__(self, parent: Frame, ctrl: Tk, list_beer_ctrl: ListBeerController):
        Frame.__init__(self, parent)
        controller = ctrl
        self.list_beer_controller = list_beer_ctrl
        self.tree_view = Treeview(self)

        home_button = Button(self, text="Home Page", command=lambda: controller.show_frame("HomeView"))
        home_button.grid(row=0, column=0, columnspan=1, sticky="W")

        page_label = Label(self, text="Beer List")
        page_label.grid(row=1, column=0, columnspan=1, sticky="WE")

    def create_table(self, tv: Treeview):
        tv['columns'] = ('breweryName', 'typeName', 'abv')
        tv.heading("#0", text='Beer', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('breweryName', text='Brewery')
        tv.column('breweryName', anchor='center', width=100)
        tv.heading('typeName', text='Type')
        tv.column('typeName', anchor='center', width=100)
        tv.heading('abv', text='ABV')
        tv.column('abv', anchor='center', width=100)
        tv.grid(sticky=(N, S, W, E))
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def load_table(self, tv: Treeview):
        beer = self.list_beer_controller.get_beer_list()
        for entry in beer:
            tv.insert(
                '',
                'end',
                text=entry['beerName'],
                values=(
                    entry['breweryName'],
                    entry['typeName'],
                    entry['abv']
                ))

    def update_table(self):
        for i in self.tree_view.get_children():
            self.tree_view.delete(i)
        self.create_table(self.tree_view)
        self.load_table(self.tree_view)
