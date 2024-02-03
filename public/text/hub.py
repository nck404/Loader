import requests,os,webbrowser
import time,os,sys,ctypes,webbrowser,shutil,mediafire_dl,requests,colorama
from pystyle import  Center, Anime, Colors, Colorate, Write 
import fade
from colorama import init, Fore, Style
from datetime import datetime
from pypresence import Presence
from bs4 import BeautifulSoup
global fprint,selected_theme,tool,colorspack,chosetext,clearConsole,chosetext,chosejson,choice,current_time,fs,fetch_link_from_json,chose
global blink
from os import system
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
   
# --------------------------------------------------------
#   _   _                         
#  | | | |                        
#  | |_| |__   ___ _ __ ___   ___ 
#  | __| '_ \ / _ \ '_ ` _ \ / _ \
#  | |_| | | |  __/ | | | | |  __/
#   \__|_| |_|\___|_| |_| |_|\___|
#                                 
#      print(f"{hex('#6F7CBE')} abc")               
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
# --------------------------------------------------------
def method():
     print(f'''
        {rgb(214, 166, 201)} {Colorate.Horizontal(Colors.blue_to_cyan, "[1]")}{Fore.RESET} - {Colorate.Horizontal(Colors.white_to_blue, "Mediafire")}            {rgb(214, 166, 201)}   *    {rgb(178, 186, 216)}If there is any error or issue    {rgb(214, 166, 201)}    
        {rgb(214, 166, 201)} {Colorate.Horizontal(Colors.blue_to_cyan, "[2]")}{Fore.RESET} - {Colorate.Horizontal(Colors.white_to_blue, "get")}                  {rgb(214, 166, 201)}   *    {rgb(178, 186, 216)}please contact us through Discord {rgb(214, 166, 201)}
        {rgb(214, 166, 201)} {Colorate.Horizontal(Colors.blue_to_cyan, "[3]")}{Fore.RESET} - {Colorate.Horizontal(Colors.white_to_blue, "website")}              {rgb(214, 166, 201)}   *    {rgb(178, 186, 216)}dsc.gg/cheatcl                    {rgb(214, 166, 201)}   
        ''')


def backchose(textlink):
    cls()
    text = requests.get(textlink).text
    fprint(text,selected_theme)
def download(link): 
    Write.Print(f'     ~/> Download ~ {link} \n',Colors.blue_to_white ,interval=0.002)
    url = link
    save_path = url.split("/")[-1]
    download_file(url, save_path, show_progress=True)
    time.sleep(1.5)
def open_link(link):
    try:
        webbrowser.open(link)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
def loadingpage(choice):
    print(f"  {rgb(175, 143, 217)} [i] loading page")
    time.sleep(0.5)
    cls()
    print(f" {rgb(145, 192, 135)}Page {choice} - {rgb(178, 186, 216)} 0 to go back")
def page(plink):
    text = requests.get(plink).text
    fprint(text,selected_theme)

def dtool(entry):
    method()
    dmt = finput()
    if dmt == "3":
        if entry["website"] == "none":
            alert2("error","the link is not available to you")
            time.sleep(2.5)
        else:
            webbrowser.open(entry["website"])
            time.sleep(2.5)
    elif dmt == "2":
        if entry["wget"] == "none":
            alert2("error","the link is not available to you")
            time.sleep(2.5)
        else:
            download(entry["wget"])
            print(f"  {rgb(175, 143, 217)} [i] ok")
            time.sleep(2.5)            
    elif dmt == "1":
        if entry["mediafire"] == "none":
            alert2("error","the link is not available to you")
        else:
            mediafire_dl.download(entry["mediafire"], entry["name"], quiet=False)
            download_folder = os.path.expanduser("~" + os.sep + "Downloads")

            downloaded_files = [f for f in os.listdir('.') if os.path.isfile(f)]
        
            newest_file = max(downloaded_files, key=os.path.getctime)            
            downloaded_file_path = os.path.join(download_folder, newest_file)
            shutil.move(newest_file, downloaded_file_path)

            alert2("done","Moved the file to Downloads folder")
            webbrowser.open("file://" + download_folder)
    time.sleep(2.5)
def fetch_link_from_json(json_url, choice,blink):
    try:
        response = requests.get(json_url)
        if response.status_code == 200:
            data = response.json()
            print(f"  {rgb(175, 143, 217)} [i] requests : 200")
            for entry in data["data"]:
                if (entry["choice"] == choice):
                    if entry["page"] == "true":
                        cls()
                        print(f"  {rgb(175, 143, 217)} [i] multi : true")
                        print(cyan_gradient('  < cheatcl > You should download by using mediafire'))
                        print(f"   {rgb(145, 192, 135)}Page {choice} - {rgb(178, 186, 216)} 0 to go back")
                        page(entry["ptext"])
                        choice = finput()
                        if choice == "0":
                            cls()
                            chose()
                        else:
                            fetch_link_from_json(entry["plink"],choice,blink)
                    else:     
                        print(f"  {rgb(175, 143, 217)} [i] single : true")
                        if choice == "0":
                            cls()
                            chose()
                        else:
                            dtool(entry)
                            break
            cls()     
            print(f" {rgb(145, 192, 135)}Page {choice} - {rgb(178, 186, 216)} 0 to go back")            
            fprint(text, selected_theme)
            choice = Write.Input(f'''
    ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | # {choice}
    ╰─ ~  ''',Colors.blue_to_white ,interval=0.000)
        
            if choice == "0":
                cls()
                chose()
            else:
                fetch_link_from_json(blink, choice,blink)
        else:
            return f"    [e] Failed to fetch JSON from URL, Status Code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error during request: {e}"


    
def fs(json_url, choice):
    try:
        response = requests.get(json_url)
        if response.status_code == 200:
            data = response.json()
            for entry in data["data"]:
                if entry["choice"] == choice:
                    return entry["link"], entry["text"]
            return "    [e] Choice not found in JSON", ""
        else:
            return "    [e] Failed to fetch JSON from URL", ""
    except requests.exceptions.RequestException as e:
        return f"Failed to fetch JSON from URL, Error: {e}", ""
def download_file(url, save_path, show_progress=True):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0)) / 1024  
        block_size = 1024
        data_downloaded = 0  
        with open(save_path, 'wb') as file:
            for data in response.iter_content(block_size):
                data_downloaded += len(data) / 1024  
                file.write(data)
                Write.Print(f"  [i] Downloaded {data_downloaded:.2f} KB / {total_size:.2f} KB",  Colors.blue_to_white , interval=0.000 ,end='\r')
        Write.Print(f"  [i] Downloaded the file to {save_path} \n",Colors.blue_to_white , interval=0.000)
        download_folder = os.path.expanduser("~" + os.sep + "Downloads")
        downloaded_file_path = os.path.join(download_folder, save_path)
        shutil.move(save_path, downloaded_file_path)
        Write.Print(f"  [i] Moved the file to Downloads folder: {downloaded_file_path}",Colors.blue_to_white, interval=0.000)
        webbrowser.open("file://" + download_folder)
        time.sleep(2.5)
        cls()
        chose()
    except Exception as e:
        Write.Print(f"  [e] An error occurred: {str(e)}",Colors.blue_to_white, interval=0.000)
        alert("error")
# chose
chosetext = "https://frenda-r.web.app/fetch/chose/chose.txt"
chosejson = "https://frenda-r.web.app/fetch/chose/chose.json"
clf = "https://frenda-r.web.app/fetch/cheatcl/changlog.txt"
newsf = "https://frenda-r.web.app/fetch/cheatcl/news.txt"







def chose():
    init(autoreset=True)
    clear = lambda: os.system('cls')
    user = "nck" 
    oss = "win10"
    clear()
    fprint(f"""

            ╔══════════════════════════════════════════════════════════╗
            ║    ___ _                                                 ║     
            ║   / __\ |__   ___  __ _| |_  / __\ / /                   ║ 
            ║  / /  | '_ \ / _ \/ _` | __|/ /   / /    yt/@necakco     ║ 
            ║ / /___| | | |  __/ (_| | |_/ /___/ /___  dsc.gg/cheatcl  ║
            ║ \____/|_| |_|\___|\__,_|\__\____/\____/  cheatcl.web.app ║
            ╚══════════════════════════════════════════════════════════╝
                
    """,selected_theme)

    print(cyan_gradient('       Enter the number that matches the one you want to enter.'))
    try:
        response = requests.get(chosetext)
        if response.status_code == 200:
            fprint(response.text,selected_theme)
        else:
            print(f"    [e] falled: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"    [e] falled: {e}")
    print(f"""      
        {rgb(145, 192, 135)}[cl] {rgb(178, 186, 216)}- changelog
        {rgb(145, 192, 135)}[nw] {rgb(178, 186, 216)}- news
        {rgb(145, 192, 135)}[info] {rgb(178, 186, 216)}- info

        {rgb(207,131,153)} # [fu] tool""")
    print(f"        {rgb(207,131,153)} # [li] link")

    current_time = datetime.now()
    choice = finput()
    if choice == "cl":
        cls()
        try:
            response = requests.get(clf)
            if response.status_code == 200:
                fprint(response.text,selected_theme)
            else:
                print(f"    [e] falled: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"    [e] falled: {e}")
        while choice != "0" :
            choice = finput()
        chose()
    if choice == "nw":
        cls()
        try:
            response = requests.get(newsf)
            if response.status_code == 200:
                fprint(response.text,selected_theme)
            else:
                print(f"    [e] falled: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"    [e] falled: {e}")
        while choice != "0" :
            choice = Write.Input(f'''
        ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | #
        ╰─ ~  ''',Colors.blue_to_white ,interval=0.000)
        chose()
    elif choice =="0":
        chose()
    elif choice == "info":
        cls()
        fprint("""
            ╔══════════════════════════════════════════════════════════╗
            ║    ___ _                                                 ║     
            ║   / __\ |__   ___  __ _| |_  / __\ / /                   ║ 
            ║  / /  | '_ \ / _ \/ _` | __|/ /   / /    yt/@necakco     ║ 
            ║ / /___| | | |  __/ (_| | |_/ /___/ /___  dsc.gg/cheatcl  ║
            ║ \____/|_| |_|\___|\__,_|\__\____/\____/  cheatcl.web.app ║
            ╚══════════════════════════════════════════════════════════╝

        [+] website : chaetcl.web.app
        [+] youtube : necakco
        [+] discord : dsc.gg/cheatcl
        [+] dev : necakco (website + loader)
        [+] visual : frd,necakco
            
        Providing cheats,service, etc since May 1st, 2019.
        Back in service since June 1st, 2023!
                ---------------------------------------------------
        CheatCL will not be responsible for any risks in your device 
        if you use the things we found.
               
        0 - to go back

           """,selected_theme)
        while choice != "0" :
            choice = Write.Input(f' ~/> ',Colors.blue_to_white ,interval=0.000)
        chose()
    elif choice == "fu":
        cls()
        fprint("""
            ╔══════════════════════════════════════════════════════════╗
            ║    ___ _                                                 ║     
            ║   / __\ |__   ___  __ _| |_  / __\ / /                   ║ 
            ║  / /  | '_ \ / _ \/ _` | __|/ /   / /    yt/@necakco     ║ 
            ║ / /___| | | |  __/ (_| | |_/ /___/ /___  dsc.gg/cheatcl  ║
            ║ \____/|_| |_|\___|\__,_|\__\____/\____/  cheatcl.web.app ║
            ╚══════════════════════════════════════════════════════════╝

        [1] web clonner
        [2] auto clicker
            
                ---------------------------------------------------
        CheatCL will not be responsible for any risks in your device 
        if you use the things we found.
               
        0 - to go back

           """,selected_theme)
    
        choice = Write.Input(f'        ~/> ',Colors.blue_to_white ,interval=0.000)
        if choice == "0":
            alert2("done","go back")
        elif choice == "1":
            code_url = "https://frenda-r.web.app/tool/webcl.py"
            try:
                # msvcrt.getch()
                response = requests.get(code_url)
                response.raise_for_status()
                python_code = response.text
                cls()
                exec(python_code)

            except requests.exceptions.RequestException as e:
                alert2("error",e)
            except SyntaxError as se:
                alert2("error",se)
            except Exception as ex:
                alert2("error",ex)
        elif choice == "2":
            code_url = "https://frenda-r.web.app/tool/auto.py"
            try:
                # msvcrt.getch()
                response = requests.get(code_url)
                response.raise_for_status()
                python_code = response.text
                cls()
                exec(python_code)

            except requests.exceptions.RequestException as e:
                alert2("error",e)
            except SyntaxError as se:
                alert2("error",se)
            except Exception as ex:
                alert2("error",ex)
            print(cyan_gradient("     done \n"))
            time.sleep(1)

    global link,text_link
    link, text_link = fs(chosejson, choice)
    if link and text_link:
        global text
        cls()
        print(cyan_gradient('< cheatcl > You should download by using mediafire'))
        print(f" {rgb(145, 192, 135)}Page {choice} - {rgb(178, 186, 216)} 0 to go back")
        text = requests.get(text_link).text
        fprint(text, selected_theme)
        choice = finput2(choice)
        blink = link
        if choice == "0":
            cls()
            chose()
        else:
            fetch_link_from_json(link, choice,blink)
    else:
        alert("error")
        cls()
        chose()
    

            



banner = r"""               
                                        ███╗   ██╗███████╗ █████╗ ██╗ ██████╗ 
                                        ████╗  ██║██╔════╝██╔══██╗██║██╔═══██╗
                                        ██╔██╗ ██║█████╗  ███████║██║██║   ██║
                                        ██║╚██╗██║██╔══╝  ██╔══██║██║██║   ██║
                                        ██║ ╚████║███████╗██║  ██║██║╚██████╔╝
                                        ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝         
                                                  Press ENTER to open.                                                                                      
"""[0:]
Write.Print(f"""

            ╔══════════════════════════════════════════════════════════╗
            ║    ___ _                                                 ║     
            ║   / __\ |__   ___  __ _| |_  / __\ / /                   ║ 
            ║  / /  | '_ \ / _ \/ _` | __|/ /   / /    yt/@necakco     ║ 
            ║ / /___| | | |  __/ (_| | |_/ /___/ /___  dsc.gg/cheatcl  ║
            ║ \____/|_| |_|\___|\__,_|\__\____/\____/  cheatcl.web.app ║
            ╚══════════════════════════════════════════════════════════╝

    """,Colors.blue_to_white, interval=0)
print(f"""
        {rgb(178, 186, 216)} chose your theme
        
        {rgb(145, 192, 135)}[1] {rgb(178, 186, 216)}- catpuccin (default)          
        {rgb(145, 192, 135)}[2] {rgb(178, 186, 216)}- rose pine (gold)
        {rgb(145, 192, 135)}[3] {rgb(178, 186, 216)}- rose pine (iris)
    """)
current_time = datetime.now()
selected_theme = Write.Input(f'''
        ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | #
        ╰─ ~  ''',Colors.blue_to_white ,interval=0.000)
if selected_theme in colorspack:
    Anime.Fade(Center.Center(banner), Colors.black_to_white, Colorate.Vertical, enter=True)
    text = """
         ██████╗██╗  ██╗███████╗ █████╗ ████████╗ ██████╗██╗     
        ██╔════╝██║  ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██║     
        ██║     ███████║█████╗  ███████║   ██║   ██║     ██║     
        ██║     ██╔══██║██╔══╝  ██╔══██║   ██║   ██║     ██║     
        ╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╗███████╗
         ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝╚══════╝                                                     
"""
    print(cyan_gradient(text))

    sel = Write.Input(f'''
        ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | # Enable Discord RPC ?
        ╰─ ~ (yes/no) ?   ''',Colors.white_to_blue ,interval=0.000)
    print('\n')
    print(cyan_gradient("     If you like CheatCL, don't forget to subscribe Necakco on youtube ♥ ♥  \n"))
    sm = Write.Input(f'''
        ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | # sub2nck or die?
        ╰─ ~ (yes/no) ?   ''',Colors.white_to_blue ,interval=0.000)
    if sm == 'yes':
        webbrowser.open("https://www.youtube.com/channel/UC51P2yIrqRGdun9MtvXNXaA")
    print(cyan_gradient("     follow necakco on facbook  \n"))
    sm2 = Write.Input(f'''
        ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | # follow necakco on facbook
        ╰─ ~ (yes/no) ?   ''',Colors.white_to_blue ,interval=0.000)
    if sm2 == 'yes':
        webbrowser.open("https://www.facebook.com/profile.php?id=100088572223464")
    if (sel == 'yes'):
        def connect_with_retry():
            cls()
            max_retries = 2
            retry_count = 0
            start_time = time.time()
            print('''
            [+] Discord RPC setup   
            ''')
            time.sleep(0.1)
            while retry_count < max_retries:
                try:
                    RPC = Presence("1193756572791361608")
                    RPC.connect()
                    return RPC
                except Exception as e:
                    print(f"    [-] Error: {e}")
                    print("    [e] Retrying in 2 seconds...")
                    time.sleep(2)
                    retry_count += 1

                    # Kiểm tra thời gian đã trôi qua từ lúc bắt đầu kết nối
                    elapsed_time = time.time() - start_time
                    if elapsed_time > 2:  # Đặt giới hạn thời gian là 10 giây
                        print("    [!] Connection timeout. Skipping connection.")
                        return None

            print("Could not connect to Discord even after retries.")
            cls()
            return None

        RPC = connect_with_retry()

        if RPC:
            RPC.update(
                state="Playing CheatCL Loader",
                details="The best Archive for software, cheat,.. | CheatCl",
                start=int(time.time()),
                buttons=[
                    {"label": "Visit website", "url": "https://cheatcl.web.app"},
                ]
            )
        else:
            print("Cannot proceed without connecting to Discord.")
        chose()
    else:
        chose()
 
else:
    alert2("error","Invalid theme selected.")
    time.sleep(1.7)



