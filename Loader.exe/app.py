import time,os,sys,ctypes,webbrowser,shutil
try:
    import requests,colorama
    from pystyle import  Center, Anime, Colors, Colorate, Write 
    import mediafire_dl
    from colorama import init, Fore, Back, Style
except:
    os.system("pip install requests && pip install pystyle && pip install colorama && pip install psutil && pip install git+https://github.com/nck404/pymediafire ")
import requests,colorama
import mediafire_dl
from pystyle import  Center, Anime, Colors, Colorate, Write 
from colorama import init, Fore, Back, Style

# import time,os,sys,ctypes,webbrowser,shutil
# import requests,colorama
# from pystyle import  Center, Anime, Colors, Colorate, Write 
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
def enenror():
    Write.Print("   [e] NOT FOUND | wait 4s coninue", Colors.blue_to_white, interval=0.000)
    time.sleep(1.5)
    chose() 

def fprint(text):
    for char in text:
        if char.isalpha():
            print( rgb(178, 186, 216) + char, end='')
        elif char.isdigit():
            print( rgb(169, 137, 209) + char, end='')
        elif (char == "[") or (char == "]"): 
            print( rgb(88, 176, 194) + char, end='')
        elif (char == "#") : 
            print( rgb(241, 144, 130) + char, end='')
        else:
            print(Fore.WHITE + char, end='')
def chose():
    setTitle(f"NCK Launcher")
    init(autoreset=True)
    clear = lambda: os.system('cls')
    clear()
    Write.Print(f"""

            ╔══════════════════════════════════════════════════════════╗
            ║    ___ _                                                 ║     
            ║   / __\ |__   ___  __ _| |_  / __\ / /                   ║ 
            ║  / /  | '_ \ / _ \/ _` | __|/ /   / /    yt/@necakco     ║ 
            ║ / /___| | | |  __/ (_| | |_/ /___/ /___  dsc.gg/cheatcl  ║
            ║ \____/|_| |_|\___|\__,_|\__\____/\____/  cheatcl.web.app ║
            ╚══════════════════════════════════════════════════════════╝
                
    """,Colors.blue_to_white, interval=0)
    try:
        response = requests.get(chosetext)
        if response.status_code == 200:
            fprint(response.text)
        else:
            print(f"    [e] falled: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"    [e] falled: {e}")
    print()
    choice = Write.Input(f'     ~/> ',Colors.blue_to_white ,interval=0.000)
    link, text_link = fs(chosejson, choice)

    if (choice == "0") :
         cls()
         chose()
    elif link and text_link:
        cls()
        print(f" {rgb(145, 192, 135)}Page {choice} - {rgb(178, 186, 216)} 0 to go back")
        text = requests.get(text_link).text
        fprint(text)
        choice = Write.Input(f' ~/> ',Colors.blue_to_white ,interval=0.000)
        if (choice == "0") :
         cls()
         chose()
        else:
            method()
            dmt = Write.Input(f'     ~/> ',Colors.blue_to_white ,interval=0.000)
            fetch_link_from_json(link,choice,dmt)
                                
    else:
        cls()
        enenror()



banner = r"""               
                                        ███╗   ██╗███████╗ █████╗ ██╗ ██████╗ 
                                        ████╗  ██║██╔════╝██╔══██╗██║██╔═══██╗
                                        ██╔██╗ ██║█████╗  ███████║██║██║   ██║
                                        ██║╚██╗██║██╔══╝  ██╔══██║██║██║   ██║
                                        ██║ ╚████║███████╗██║  ██║██║╚██████╔╝
                                        ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝         
                                                  Press ENTER to open.                                                                                      
"""[0:]
Anime.Fade(Center.Center(banner), Colors.black_to_white, Colorate.Vertical, enter=True)
chose()