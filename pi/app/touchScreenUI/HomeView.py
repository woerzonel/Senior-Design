#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk


class HomeView(tk.Frame):
    """Frame that will be shown on start-up and is considered the home page of the application"""

    def __init__(self, parent: tk.Frame, ctrl: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.controller = ctrl
        page_label = tk.Label(self, text="Home")
        page_label.pack(side="top", fill="x", pady=10)

        tk.Button(self, text="Add Beer", command=lambda: ctrl.show_frame("CreateBeerView")).pack()
        tk.Button(self, text="List Beer", command=lambda: ctrl.show_frame("ListBeerView")).pack()
