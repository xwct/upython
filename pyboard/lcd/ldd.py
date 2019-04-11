# ldd.py Demo/test program for dropdown list and listbox controls for Pyboard LCD160CR GUI

# The MIT License (MIT)
#
# Copyright (c) 2017 Peter Hinch
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from constants import *
from lcd160_gui import Button, Label, Screen, Dropdown, Listbox, ButtonList
import font10
from lcd_local import setup

# STANDARD BUTTONS

def quitbutton():
    def quit(button):
        Screen.shutdown()
    Button((109, 107), font = font10, callback = quit, fgcolor = RED, text = 'Quit',)

# **** BASE SCREEN ****

class BaseScreen(Screen):
    def __init__(self):
        super().__init__()
        quitbutton()
# Dropdown
        self.lbl_dd = Label((0, 80), font = font10, width = 60, border = 2, bgcolor = DARKGREEN, fgcolor = RED)
        self.dropdown = Dropdown((0, 0), font = font10, width = 65, callback = self.cbdb,
                                 elements = ('Dog', 'Cat', 'Rat', 'Goat', 'Pig'))
# Listbox
        self.listbox = Listbox((80, 0), font = font10, width = 79,
                               bgcolor = GREY, fgcolor = YELLOW, select_color = BLUE,
                               elements = ('aardvark', 'zebra', 'armadillo', 'warthog'),
                               callback = self.cblb)

        self.btnrep = Button((0, 40), height = 20, font = font10, callback = self.cbrep, fgcolor = RED,
           text = 'Report', shape = RECTANGLE, width = 60)

# Enable/Disable toggle 
        self.bs_en = ButtonList(self.cb_en_dis)
        self.bs_en.add_button((0, 107), font = font10, fontcolor = BLACK, height = 20, width = 60,
                              fgcolor = GREEN, shape = RECTANGLE, text = 'Disable', args = (True,))
        self.bs_en.add_button((0, 107), font = font10, fontcolor = BLACK, height = 20, width = 60,
                              fgcolor = RED, shape = RECTANGLE, text = 'Enable', args = (False,))

    def cb_en_dis(self, button, disable):
        self.listbox.greyed_out(disable)
        self.dropdown.greyed_out(disable)
        self.btnrep.greyed_out(disable)

    def cbdb(self, dropdown):
        self.lbl_dd.value(dropdown.textvalue())
        print('dropdown callback:', dropdown.textvalue(), dropdown.value())

    def cblb(self, listbox):
        print('listbox callback:', listbox.textvalue(), listbox.value())

    def cbrep(self, _):
        print('Report:')
        print('listbox', self.listbox.textvalue(), self.listbox.value())
        print('dropdown', self.dropdown.textvalue(), self.dropdown.value())

def test():
    print('Testing TFT...')
    setup()
    Screen.change(BaseScreen)

test()
