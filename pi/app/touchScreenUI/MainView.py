#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk

from app.touchScreenUI.CreateBeerView import CreateBeerView
from app.touchScreenUI.HomeView import HomeView
from app.touchScreenUI.ListBeerView import ListBeerView
from app.touchScreenUI.SettingsView import SettingsView


class MainView(tk.Tk):
    """Controller and Root for the Brewery Menu Application"""

    def __init__(self, controllers: {}, menu_settings: {}, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Brewery Menu v1.0')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # TODO: possible enumerate page names so if a name is changed, it'll be reflected in all places
        #  make it loop through and add proper controller
        for F in (HomeView, SettingsView):
            page_name = F.__name__
            frame = F(parent=container, ctrl=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        page_name = CreateBeerView.__name__
        frame = CreateBeerView(
            parent=container,
            ctrl=self,
            create_beer_ctrl=controllers['create_beer_controller'])
        self.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        page_name = ListBeerView.__name__
        frame = ListBeerView(
            parent=container,
            ctrl=self,
            list_beer_ctrl=controllers['list_beer_controller'])
        self.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomeView")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == 'ListBeerView':
            frame.update_table()
