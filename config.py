# Default configration for pyfm file manager
from colorama import init, Fore, Back, Style

init(convert=True)

# Title Bar
title_fg = Fore.CYAN
title_bg = Back.MAGENTA

# When user navigates through to the file manager
fg = Fore.WHITE
bg = Back.GREEN 

# Reset variables
reset_fg = Fore.RESET
reset_bg = Back.RESET

# key bindings
key_bindings = {
"j":"MOVE DOWN",
"k":"MOVE UP",
"q":"QUIT"
}


