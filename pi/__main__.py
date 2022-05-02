#!/usr/bin/python
# -*- coding: utf-8 -*-

import configparser as config_parser
import os as os
import platform as plat
import threading as threading

from app.controllers.CreateBeerController import CreateBeerController
from app.controllers.ListBeerController import ListBeerController
from app.controllers.SettingsController import SettingsController
from app.peripheral_display.PeripheralDisplay import *
from app.touchScreenUI.MainView import MainView


def check_monitors_popup():
    pop = tk.Tk()
    pop.title('!')
    label = tk.Label(pop, text='Please check that display monitor is plugged in. Press Okay to try again.')
    label.pack(side='top', fill='x', pady=10)
    ok_button = tk.Button(pop, text='Okay', command=pop.destroy)
    ok_button.pack()
    pop.mainloop()


# starts the touch screen component at the given location in the form of 'WIDTHxHEIGHT+PADX+PADY'
def start_touch_screen(position: str, menu_settings: {}, db_loc: str, db_name: str):
    controllers = {
        'create_beer_controller': CreateBeerController(db_loc=db_loc, db_name=db_name),
        'list_beer_controller': ListBeerController(db_loc=db_loc, db_name=db_name),
        'settings_controller': SettingsController(menu_settings)
    }
    app = MainView(controllers=controllers, menu_settings=menu_settings)
    app.geometry(position)
    app.mainloop()


# starts the peripheral display component at the given location in the form of 'WIDTHxHEIGHT+PADX+PADY'
def start_peripheral_display(position: str, display_settings: {}, db_loc: str, db_name: str):
    display = PeripheralDisplay(ctrl=PeripheralDisplayController(db_loc=db_loc, db_name=db_name), display_settings=display_settings)
    display.geometry(position)
    display.mainloop()


def main():
    print("Brewery Menu Application v1.0")
    operating_system = plat.system()
    config_file = os.path.relpath('config/config.ini', os.curdir)
    config = config_parser.ConfigParser(comment_prefixes=('#', ';'), delimiters=(':', '='))
    config.read(config_file)

    db_name = config['File Paths']['database_name']

    if operating_system == 'Windows':
        db_loc = config['File Paths']['database_windows_dir']
    elif operating_system == 'Linux':
        db_loc = config['File Paths']['database_pi_dir']  # used in pi environment
    else:
        print('Could not determine OS.')
        exit(-1)

    touch_screen_position = '1200x800+0+0'
    display_screen_position = '1200x800+0+0'
    # if operating_system == 'Windows':
    #     # get all monitor sizes attached to primary device
    #     monitors = get_monitors()
    #     while len(monitors) < 2:
    #         check_monitors_popup()
    #         monitors = get_monitors()
    #
    #     # setup each window to take the entire screen and position them accordingly
    #     # TODO: support more than 1 display monitor?? would be fairly easy to do
    #     touch_screen_position = str(monitors[0].width) + 'x' + str(monitors[0].height) + '+0+0'
    #     display_screen_position = str(monitors[1].width) + 'x' + str(monitors[1].height) + '+' + str(monitors[1].x) + '+0'
    # elif operating_system == 'Linux':
    #     # TODO: figure out how to determine attached displays via Linux kernel
    #     # TODO: figure out how to parse the device-tree on Rasbian
    #     # TODO: determine which nodes to search for in device-tree to find DSI and HDMI connections
    #     print('')
    #     touch_screen_position = ''
    #     display_screen_position = ''
    # else:
    #     print('Could not determine OS.')
    #     exit(-1)
    # start_touch_screen(touch_screen_position, config['Menu Settings'], db_loc, db_name)
    # create threads to handle touch_screen and peripheral_display
    touch_screen_thread = threading.Thread(target=start_touch_screen, args=([touch_screen_position], config['Menu Settings'], db_loc, db_name))
    # peripheral_display is a background thread now and will close if the application is exited regardless of state
    # peripheral_display_thread = threading.Thread(target=start_peripheral_display, args=([display_screen_position], config['Display Settings'], db_loc, db_name), daemon=True)

    # start threads
    touch_screen_thread.start()
    # peripheral_display_thread.start()

    # wait for each thread to finish
    # this shouldn't happen until the application is closing
    # TODO: Figure out exception by Sqlite objects based on closing application from "x-ing out" of BaseUI
    touch_screen_thread.join()


if __name__ == '__main__':
    main()
