# -*- coding: utf-8 -*-

import tkinter as tk

from app.controllers.PeripheralDisplayController import PeripheralDisplayController


class PeripheralDisplay(tk.Tk):
    """Class that controls logic to display to external monitor and update itself"""

    def __init__(self, ctrl: PeripheralDisplayController, display_settings: {}, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Display v1.0")
        self.display_settings = display_settings
        self.ctrl = ctrl

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

