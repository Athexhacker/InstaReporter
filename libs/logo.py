# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = """
╭━━╮╱╱╱╱╱╭╮╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
╰┫┣╯╱╱╱╱╭╯╰╮╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╭╯╰╮
╱┃┃╭━╮╭━┻╮╭╋━━┫╰━╯┣━━┳━━┳━━┳┻╮╭╋━━┳━╮
╱┃┃┃╭╮┫━━┫┃┃╭╮┃╭╮╭┫┃━┫╭╮┃╭╮┃╭┫┃┃┃━┫╭╯
╭┫┣┫┃┃┣━━┃╰┫╭╮┃┃┃╰┫┃━┫╰╯┃╰╯┃┃┃╰┫┃━┫┃
╰━━┻╯╰┻━━┻━┻╯╰┻╯╰━┻━━┫╭━┻━━┻╯╰━┻━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯"""

urls = [
    "YouTube - https://youtube.com/@inziXploit444",
    "Instagram - https://instagram.com/itx_athex86",
    "InstaReporter Tool - Created By ATHEX H4CK3R"
    ]

def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.MAGENTA + "      Developer: ATHEX"+ Style.RESET_ALL + Style.BRIGHT)
    print(Fore.CYAN + "\n", "-> Follow me On Instagram @itx_athex86.")
    print ("\n", "-> Special For Hackers:\n    " + choice(urls))
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)
