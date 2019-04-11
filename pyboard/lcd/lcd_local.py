# lcd_local.py Configuration for Pybboard LCD160CR GUI

# This file is intended for definition of the local hardware. It's also a
# convenient place to store constants used on a project such as colors.

# The MIT License (MIT)
#
# Copyright (c) 2016 Peter Hinch
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

# Arguments for LCD160CR_G are as per official LCD160CR driver with the
# addition of a 'bufsize' kwarg. If provided it should be equal to
# height * max_width * 2 for the largest font in use.
# Default 1058 bytes, allowing fonts upto 23*23 pixels (font14.py)

import lcd160cr
from lcd160_gui import Screen, LCD160CR_G

def setup():
    lcd = LCD160CR_G("Y")  # Set connection
    lcd.set_orient(lcd160cr.LANDSCAPE)  # and orientation
    Screen.setup(lcd)
