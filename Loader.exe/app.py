import time,os,sys,ctypes,webbrowser,shutil
try:
    import time,os,sys,ctypes,webbrowser,shutil,mediafire_dl,requests,colorama
    from pystyle import  Center, Anime, Colors, Colorate, Write 
    from colorama import init, Fore, Back, Style
    from datetime import datetime
except:
    os.system("pip install requests && pip install pystyle && pip install colorama && pip install psutil && pip install git+https://github.com/nck404/pymediafire ")
import time,os,sys,ctypes,webbrowser,shutil,mediafire_dl,requests,colorama
from pystyle import  Center, Anime, Colors, Colorate, Write 
from colorama import init, Fore, Back, Style
from datetime import datetime
from pypresence import Presence
def setTitle(title):
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    elif os.name == 'posix':
        sys.stdout.write(title)
    else:
        pass
global cls
def cls():
 os.system('cls' if os.name=='nt' else 'clear')
def tool():
  os.system('cls' if os.name=='nt' else 'clear')
def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')
def method():
     print(f'''
        {rgb(214, 166, 201)}╔════════════════════════════╗       ╔═══════════════════════════════════╗
        {rgb(214, 166, 201)}║ {Colorate.Horizontal(Colors.blue_to_cyan, "[1]")}{Fore.RESET} - {Colorate.Horizontal(Colors.white_to_blue, "Mediafire")}            {rgb(214, 166, 201)}║   *   ║ {rgb(178, 186, 216)}If there is any error or issue    {rgb(214, 166, 201)}║     
        {rgb(214, 166, 201)}║ {Colorate.Horizontal(Colors.blue_to_cyan, "[2]")}{Fore.RESET} - {Colorate.Horizontal(Colors.white_to_blue, "get")}                  {rgb(214, 166, 201)}║   *   ║ {rgb(178, 186, 216)}please contact us through Discord {rgb(214, 166, 201)}║
        {rgb(214, 166, 201)}║ {Colorate.Horizontal(Colors.blue_to_cyan, "[3]")}{Fore.RESET} - {Colorate.Horizontal(Colors.white_to_blue, "website")}              {rgb(214, 166, 201)}║   *   ║ {rgb(178, 186, 216)}dsc.gg/cheatcl                    {rgb(214, 166, 201)}║   
        {rgb(214, 166, 201)}╚════════════════════════════╝       ╚═══════════════════════════════════╝
        ''')
def rgb(r, g, b):
    return f"\x1b[38;2;{r};{g};{b}m"



# Thực hiện một số thay đổi trong thời gian chạy

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


def fetch_link_from_json(json_url, choice, dmt):
    try:
        response = requests.get(json_url)
        if response.status_code == 200:
            data = response.json()
            print(f"  {rgb(175, 143, 217)} [i] requests : 200")
            for entry in data["data"]:
                # print(f"Processing entry: {entry}")
                if (entry["choice"] == choice):
                    if dmt == "3":
                        if entry["website"] == "none":
                            print(f"  {rgb(175, 143, 217)} [i] the link is not available to you")
                        else:
                            webbrowser.open(entry["website"])
                        time.sleep(2.5)
                        cls()
                        chose()
                    elif dmt == "2":
                        if entry["wget"] == "none":
                            print(f"  {rgb(175, 143, 217)} [i] the link is not available to you")
                        else:
                            download(entry["wget"])
                            print(f"  {rgb(175, 143, 217)} [i] ok")
                            time.sleep(2.5)

                        time.sleep(2.5)
                        cls()
                        chose()
                    elif dmt == "1":
                        if entry["mediafire"] == "none":
                            print(f"  {rgb(175, 143, 217)} [i] the link is not available to you")
                        else:
                            mediafire_dl.download(entry["mediafire"], entry["name"], quiet=False)
                            download_folder = os.path.expanduser("~" + os.sep + "Downloads")
                            downloaded_file_path = os.path.join(download_folder, entry["name"])
                            shutil.move(entry["name"], downloaded_file_path)
                            Write.Print(f"  [i] Moved the file to Downloads folder: {downloaded_file_path}", Colors.blue_to_white, interval=0.000)
                            webbrowser.open("file://" + download_folder)
                    time.sleep(2.5)
                    cls()
                    chose()
            return enenror()

        else:
            return f"    [e] Failed to fetch JSON from URL, Status Code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error during request: {e}"

# ... (other code)

    
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
        enenror()
# chose
chosetext = "https://cheatcl-file.web.app/fetch/chose/chose.txt"
chosejson = "https://cheatcl-file.web.app/fetch/chose/chose.json"
clf = "https://cheatcl-file.web.app/fetch/cheatcl/changlog.txt"
newsf = "https://cheatcl-file.web.app/fetch/cheatcl/news.txt"
def enenror():
    Write.Print("   [e] NOT FOUND | wait 4s coninue", Colors.blue_to_white, interval=0.000)
    time.sleep(1.5)
    chose() 

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




def chose():

    setTitle(f"NCK Launcher")
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
    """)
    current_time = datetime.now()
    choice = Write.Input(f'''
        ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | #
        ╰─ ~  ''',Colors.blue_to_white ,interval=0.000)
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
            choice = Write.Input(f'''
        ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | #
        ╰─ ~  ''',Colors.blue_to_white ,interval=0.000)
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
    
    link, text_link = fs(chosejson, choice)
    if link and text_link:
        cls()
        print(f" {rgb(145, 192, 135)}Page {choice} - {rgb(178, 186, 216)} 0 to go back")
        text = requests.get(text_link).text
        fprint(text, selected_theme)
        
        choice = Write.Input(f'''
    ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | #
    ╰─ ~  ''',Colors.blue_to_white ,interval=0.000)
        
        if choice == "0":
            cls()
            chose()
        else:
            method()
            dmt = Write.Input(f'''
    ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | #
    ╰─ ~  ''',Colors.blue_to_white ,interval=0.000)
            fetch_link_from_json(link, choice, dmt)
    else:
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
    print(f" {rgb(169, 137, 209)}      Invalid theme selected.")
    time.sleep(1.7)