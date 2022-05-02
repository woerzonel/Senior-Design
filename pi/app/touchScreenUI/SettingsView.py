#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk


class SettingsView(ttk.Notebook):
    """Settings page that will contain multiple tabs to separate different settings"""

    def __init__(self, parent: tk.Frame, ctrl: tk.Tk):
        ttk.Notebook.__init__(self, parent)
