import requests,os,webbrowser
import time,os,sys,ctypes,webbrowser,shutil,mediafire_dl,requests,colorama
from pystyle import  Center, Anime, Colors, Colorate, Write 
import fade
from colorama import init, Fore, Style
from datetime import datetime
from pypresence import Presence
from bs4 import BeautifulSoup
from pypresence import Presence
import re
import urllib.parse
from tqdm import tqdm
def set_terminal_transparency(alpha):
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    styles = ctypes.windll.user32.GetWindowLongA(hwnd, -20)
    styles = styles | 0x00080000  # WS_EX_LAYERED
    ctypes.windll.user32.SetWindowLongA(hwnd, -20, styles)
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, int(alpha * 255), 2)
def setTitle(title):
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    elif os.name == 'posix':
        sys.stdout.write(title)
    else:
        pass
set_terminal_transparency(0.85)
 
setTitle("[--cheatclloader--] cheatcl.web.app - Made by frenda w/love")

code_url = "https://frenda-r.web.app/text/hub.obf"

try:
    # msvcrt.getch()
    response = requests.get(code_url)
    response.raise_for_status()
    python_code = response.text
    exec(python_code)

except requests.exceptions.RequestException as e:
    print(f"An unexpected error occurred -  {e}")
    print("""
    ██╗  ██╗ ██████╗ ██╗  ██╗
    ██║  ██║██╔═████╗██║  ██║
    ███████║██║██╔██║███████║
    ╚════██║████╔╝██║╚════██║
         ██║╚██████╔╝     ██║
         ╚═╝ ╚═════╝      ╚═╝
                             
    close this window                   
""")
    time.sleep(8)
        
except SyntaxError as se:
    print(f"An unexpected error occurred -  {se}")
    print("""
    ██╗  ██╗ ██████╗ ██╗  ██╗
    ██║  ██║██╔═████╗██║  ██║
    ███████║██║██╔██║███████║
    ╚════██║████╔╝██║╚════██║
         ██║╚██████╔╝     ██║
         ╚═╝ ╚═════╝      ╚═╝
                             
    close this window                   
""")
    time.sleep(8)



except Exception as ex:
    print(f"An unexpected error occurred -  {ex}")
    print("""
    ██╗  ██╗ ██████╗ ██╗  ██╗
    ██║  ██║██╔═████╗██║  ██║
    ███████║██║██╔██║███████║
    ╚════██║████╔╝██║╚════██║
         ██║╚██████╔╝     ██║
         ╚═╝ ╚═════╝      ╚═╝
                             
    close this window                   
""")
    time.sleep(8)
