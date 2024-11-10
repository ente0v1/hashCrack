import os
import time
import sys
from functions import (
    define_default_parameters, define_windows_parameters, clear_screen, show_title, show_menu, handle_option
)

define_windows_parameters()
define_default_parameters()

default_os = "Linux"
counter = 1

while True:
    clear_screen()
    show_title()
    show_menu(default_os)
    
    user_option = input("Select an option: ").strip()
    counter += 1

    if user_option.lower() != 'x':
        default_os = "Windows" if counter % 2 == 0 else "Linux"
    else:
        counter -= 1

    if user_option.lower() == 'q':
        print("Exiting program...")
        break

    handle_option(user_option)

    if user_option == "hashcat_option_identifier":
        input("Hashcat has finished. Press any key to continue...")

    print(f"User option: {user_option}")
