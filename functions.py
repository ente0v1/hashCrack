import os
import time
import random
import subprocess
from datetime import datetime
from termcolor import colored

default_scripts = os.path.expanduser("~/hashCrack")
default_windows_scripts = f"/c/Users/{os.getenv('USER')}/source/repos/ente0v1/hashCrack/scripts/windows"

def define_default_parameters():
    return {
        "default_hashcat": ".",
        "default_status_timer": "y",
        "default_workload": "4",
        "default_os": "Linux",
        "default_restorepath": os.path.expanduser("~/.local/share/hashcat/sessions"),
        "default_session": datetime.now().strftime("%Y-%m-%d"),
        "default_wordlists": "wordlists",
        "default_masks": "masks",
        "default_rules": "rules",
        "default_wordlist": "dnsmap.txt",
        "default_mask": "?d?d?d?d",
        "default_rule": "T0XlCv2.rule",
        "default_min_length": "4",
        "default_max_length": "16",
        "default_hashmode": "22000"
    }

def define_windows_parameters():
    return {
        "default_hashcat": ".",
        "default_status_timer": "y",
        "default_workload": "4",
        "default_os": "Windows",
        "default_restorepath": os.path.expanduser("~/hashcat/sessions"),
        "default_session": datetime.now().strftime("%Y-%m-%d"),
        "default_wordlists": f"/c/Users/{os.getenv('USER')}/wordlists",
        "default_masks": "masks",
        "default_rules": "rules",
        "default_wordlist": "rockyou.txt",
        "default_mask": "?d?d?d?d",
        "default_rule": "T0XlCv2.rule",
        "default_min_length": "4",
        "default_max_length": "16",
        "default_hashmode": "22000"
    }

def define_my_parameters():
    return {
        "default_hashcat": ".",
        "default_status_timer": "y",
        "default_workload": "2",
        "default_os": "Linux",
        "default_restorepath": os.path.expanduser("~/.local/share/hashcat/sessions"),
        "default_session": datetime.now().strftime("%Y-%m-%d"),
        "default_wordlists": os.path.expanduser("~/cracking/wordlists"),
        "default_masks": os.path.expanduser("~/cracking/masks"),
        "default_rules": os.path.expanduser("~/cracking/rules"),
        "default_wordlist": "paroleitaliane/bruteforce.txt",
        "default_mask": "?d?d?d?d",
        "default_rule": "T0XlCv2.rule",
        "default_min_length": "4",
        "default_max_length": "16",
        "default_hashmode": "22000"
    }

def list_sessions(default_restorepath):
    print(colored("Available sessions:", 'green'))
    restore_files = [
        f.replace(".restore", "")
        for f in os.listdir(default_restorepath)
        if f.endswith(".restore")
    ]
    if not restore_files:
        print("No restore files found...")
    else:
        print("\n".join(restore_files))

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_menu(default_os):
    ascii_art = """
    
                                        .s5SSSs.                                         
.s    s.  .s5SSSs.  .s5SSSs.  .s    s.        SS. .s5SSSs.  .s5SSSs.  .s5SSSs.  .s    s. 
      SS.       SS.       SS.       SS. sS    `:;       SS.       SS.       SS.       SS.
sS    S%S sS    S%S sS    `:; sS    S%S SS        sS    S%S sS    S%S sS    `:; sS    S%S
SSSs. S%S SSSs. S%S `:;;;;.   SSSs. S%S SS        SS .sS;:' SSSs. S%S SS        SSSSs.S:'
SS    S%S SS    S%S       ;;. SS    S%S SS        SS    ;,  SS    S%S SS        SS  "SS. 
SS    `:; SS    `:;       `:; SS    `:; SS        SS    `:; SS    `:; SS        SS    `:;
SS    ;,. SS    ;,. .,;   ;,. SS    ;,. SS    ;,. SS    ;,. SS    ;,. SS    ;,. SS    ;,.
:;    ;:' :;    ;:' `:;;;;;:' :;    ;:' `:;;;;;:' `:    ;:' :;    ;:' `:;;;;;:' :;    ;:'

    """
    print(colored(ascii_art, 'cyan'))
    print(colored("="*50, 'cyan'))
    print(colored(f"   Welcome to hashCrack! - Menu Options for {default_os}", 'cyan', attrs=['bold']))
    print(colored("="*50, 'cyan'))
    options = [
        f"{colored('[1]', 'blue', attrs=['bold'])} Crack with Wordlist          {colored('[EASY]', 'blue', attrs=['bold'])}",
        f"{colored('[2]', 'green', attrs=['bold'])} Crack with Association       {colored('[MEDIUM]', 'green', attrs=['bold'])}",
        f"{colored('[3]', 'yellow', attrs=['bold'])} Crack with Brute-Force       {colored('[HARD]', 'yellow', attrs=['bold'])}",
        f"{colored('[4]', 'red', attrs=['bold'])} Crack with Combinator        {colored('[ADVANCED]', 'red', attrs=['bold'])}",
    ]
    print("\n   " + "\n   ".join(options))
    print(colored("\n" + "="*50, 'magenta'))
    print(f"   {colored('Press X to switch to Windows' if default_os == 'Linux' else 'Press X to switch to Linux', 'magenta', attrs=['bold'])}.")
    print(colored("="*50, 'magenta'))


def animate_text(text, delay):
    for i in range(len(text) + 1):
        clear_screen()
        print(text[:i], end="", flush=True)
        time.sleep(delay)

def handle_option(option, default_os):
    animate_text("...", 0.1)
    
    script_map = {
        "1": "crack_wordlist.py",
        "2": "crack_rule.py",
        "3": "crack_bruteforce.py",
        "4": "crack_combo.py"
    }
    
    script_type = "windows" if default_os == "Windows" else "linux"
    script_name = script_map.get(option, None)

    if script_name:
        script_path = f"scripts/{script_type}/{script_name}"
        print(f"{colored(f'{script_path} is Executing', 'green')}")
        
        if default_os == "Linux":
            os.system(f"python3 {script_path}")
        else:
            os.system(f"python {script_path}")

        input("Press Enter to return to the menu...")

    elif option.lower() == "q":
        animate_text("Exiting...", 0.1)
        print(colored("Done! Exiting...", 'yellow'))
        exit(0)
    else:
        print(colored("Invalid option. Please try again.", 'red'))


def execute_windows_scripts():
    windows_scripts_dir = "scripts/windows"
    if os.path.isdir(windows_scripts_dir):
        for script in os.listdir(windows_scripts_dir):
            script_path = os.path.join(windows_scripts_dir, script)
            if os.path.isfile(script_path):
                print(f"Executing Windows script: {script}")
                os.system(f"python {script_path}")
    else:
        print(colored(f"Windows scripts directory not found: '{windows_scripts_dir}'", 'red'))

def save_settings(session, path_wordlists, default_wordlist, mask, rule):
    with open("status.txt", "w") as f:
        f.write(f"\nSession: {session}")
        f.write(f"\nWordlist: {path_wordlists}/{default_wordlist}")
        f.write(f"\nMask: {mask}")
        f.write(f"\nRule: {rule}")
        f.write(f"\nHash: {open('hash.txt').read()}")
        f.write(f"\nPlaintext: {open('plaintext.txt').read()}")

def restore_session(restore_file_input, default_restorepath):
    if restore_file_input:
        restore_file = os.path.join(default_restorepath, f"{restore_file_input}.restore")
        if not os.path.isfile(restore_file):
            print(colored(f"Error: Restore file '{restore_file}' not found.", 'red'))
            exit(1)
        session = os.path.basename(restore_file).replace(".restore", "")
        print(colored(f"Restore >> {restore_file}", 'green'))
        cmd = f"hashcat --session={session} --restore"
        os.system(cmd)

def save_logs(session):
    os.makedirs(f"logs/{session}", exist_ok=True)
    os.rename(session, f"logs/{session}")
    os.rename("status.txt", f"logs/{session}/status.txt")
    os.rename("plaintext.txt", f"logs/{session}/plaintext.txt")
