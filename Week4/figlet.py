# 先安装pyfiglet模块 -> pip install pyfiglet

from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
has_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    the_font = random.choice(has_fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in has_fonts:
        the_font = sys.argv[2]
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

s = input("Input: ")
figlet.setFont(font = the_font)
print("Output:\n", figlet.renderText(s))