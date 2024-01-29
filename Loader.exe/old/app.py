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
import fade
from colorama import init, Fore, Style
from datetime import datetime
from pypresence import Presence

# function
def webclonner():

    from bs4 import BeautifulSoup
  

    import os
    from pystyle import Write, Colors

    base_dir = os.getcwd()

    Write.Print(f"""

                ╔══════════════════════════════════════════════════════════╗
                ║    ___ _                                                 ║     
                ║   / __\ |__   ___  __ _| |_  / __\ / /                   ║ 
                ║  / /  | '_ \ / _ \/ _` | __|/ /   / /    yt/@necakco     ║ 
                ║ / /___| | | |  __/ (_| | |_/ /___/ /___  dsc.gg/cheatcl  ║
                ║ \____/|_| |_|\___|\__,_|\__\____/\____/  cheatcl.web.app ║
                ╚══════════════════════════════════════════════════════════╝
                    
        """, Colors.blue_to_white, interval=0)

    site_name = Write.Input(f'      Link website ~/>    ', Colors.blue_to_white, interval=0.000)
    project_name = ''
    if site_name == '0':

        chose()
    # Set project_path relative to the current working directory

    project_path = os.path.join(base_dir + '/cloned', project_name)
    os.makedirs(project_path, exist_ok=True)

    visited_links = []
    error_links = []


    def save(bs, element, check):
        links = bs.find_all(element)

        for l in links:
            href = l.get("href")
            if href is not None and href not in visited_links:
                if check in href:
                    href = l.get("href")
                    print("Working with : {}".format(href))
                    if "//" in href:
                        path_s = href.split("/")
                        file_name = ""
                        for i in range(3, len(path_s)):
                            file_name = file_name + "/" + path_s[i]
                    else:
                        file_name = href

                    l = site_name + file_name

                    try:
                        r = requests.get(l)
                    except requests.exceptions.ConnectionError:
                        error_links.append(l)
                        continue

                    if r.status_code != 200:
                        error_links.append(l)
                        continue

                    os.makedirs(os.path.dirname(project_path + file_name.split("?")[0]), exist_ok=True)
                    with open(project_path + file_name.split("?")[0], "wb") as f:
                        f.write(r.text.encode('utf-8'))
                        f.close()

                    visited_links.append(l)


    def save_assets(html_text):
        bs = BeautifulSoup(html_text, "html.parser")
        save(bs=bs, element="link", check=".css")
        save(bs=bs, element="script", check=".js")

        links = bs.find_all("img")
        for l in links:
            href = l.get("src")
            if href is not None and href not in visited_links:
                print("Working with : {}".format(href))
                if "//" in href:
                    path_s = href.split("/")
                    file_name = ""
                    for i in range(3, len(path_s)):
                        file_name = file_name + "/" + path_s[i]
                else:
                    file_name = href

                l = site_name + file_name

                try:
                    r = requests.get(l, stream=True)
                except requests.exceptions.ConnectionError:
                    error_links.append(l)
                    continue

                if r.status_code != 200:
                    error_links.append(l)
                    continue

                os.makedirs(os.path.dirname(project_path + file_name.split("?")[0]), exist_ok=True)
                with open(project_path + file_name.split("?")[0], "wb") as f:
                    shutil.copyfileobj(r.raw, f)

                visited_links.append(l)

        # Check and save files with ".jar", ".exe", and ".zip" extensions
        specific_file_extensions = [".jar", ".exe", ".zip"]
        specific_file_links = bs.find_all("a", href=lambda x: (x and x.endswith(tuple(specific_file_extensions))))
        
        for specific_file_link in specific_file_links:
            href = specific_file_link.get("href")
            if href is not None and href not in visited_links:
                print("Working with : {}".format(href))
                if "//" in href:
                    path_s = href.split("/")
                    file_name = ""
                    for i in range(3, len(path_s)):
                        file_name = file_name + "/" + path_s[i]
                else:
                    file_name = href

                l = site_name + file_name

                try:
                    r = requests.get(l, stream=True)
                except requests.exceptions.ConnectionError:
                    error_links.append(l)
                    continue

                if r.status_code != 200:
                    error_links.append(l)
                    continue

                os.makedirs(os.path.dirname(project_path + file_name.split("?")[0]), exist_ok=True)
                with open(project_path + file_name.split("?")[0], "wb") as f:
                    shutil.copyfileobj(r.raw, f)

                visited_links.append(l)


    def crawl(link):
        if "http://" not in link and "https://" not in link:
            link = site_name + link

        if site_name in link and link not in visited_links:
            fprint(f"              [i] - Working with : {link}",selected_theme)

            path_s = link.split("/")
            file_name = ""
            for i in range(3, len(path_s)):
                file_name = file_name + "/" + path_s[i]

            if file_name[len(file_name) - 1] != "/":
                file_name = file_name + "/"

            try:
                r = requests.get(link)
            except requests.exceptions.ConnectionError:
                fprint("              [e] - Connection Error",selected_theme)
                sys.exit(1)

            if r.status_code != 200:
                fprint("              [e] - Invalid Response",selected_theme)
                sys.exit(1)
            print(project_path + file_name + "index.html")
            os.makedirs(os.path.dirname(project_path + file_name.split("?")[0]), exist_ok=True)
            with open(project_path + file_name.split("?")[0] + "index.html", "wb") as f:
                text = r.text.replace(site_name, project_name)
                f.write(text.encode('utf-8'))
                f.close()

            visited_links.append(link)

            save_assets(r.text)

            soup = BeautifulSoup(r.text, "html.parser")

            for link in soup.find_all('a'):
                try:
                    crawl(link.get("href"))
                except:
                    error_links.append(link.get("href"))


    crawl(site_name + "/")
    fprint("              [i] - Link crawled log\n",selected_theme)
    for link in visited_links:
        print("              [>] - ---- {}\n".format(link))

    fprint("              [a] - Link error log\n",selected_theme)
    for link in error_links:
        print("              [>] - ---- {}\n".format(link))

def setTitle(title):
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    elif os.name == 'posix':
        sys.stdout.write(title)
    else:
        pass
def titlea():
    setTitle(f"[--cheatclloader--] cheatcl.web.app - Made by frenda w/love")
    time.sleep(1.2)
    setTitle(f"[--cheatclloader--] - nck on top - cheatcl.web.app")
global cls
def alert(type):
    pass
def set_terminal_transparency(alpha):
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    styles = ctypes.windll.user32.GetWindowLongA(hwnd, -20)
    styles = styles | 0x00080000  # WS_EX_LAYERED
    ctypes.windll.user32.SetWindowLongA(hwnd, -20, styles)
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, int(alpha * 255), 2)

set_terminal_transparency(0.85)
def cls():
 os.system('cls' if os.name=='nt' else 'clear')
def tool():
  os.system('cls' if os.name=='nt' else 'clear')
def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')
def method():
     print(f'''
        {rgb(214, 166, 201)} {Colorate.Horizontal(Colors.blue_to_cyan, "[1]")}{Fore.RESET} - {Colorate.Horizontal(Colors.white_to_blue, "Mediafire")}            {rgb(214, 166, 201)}   *    {rgb(178, 186, 216)}If there is any error or issue    {rgb(214, 166, 201)}    
        {rgb(214, 166, 201)} {Colorate.Horizontal(Colors.blue_to_cyan, "[2]")}{Fore.RESET} - {Colorate.Horizontal(Colors.white_to_blue, "get")}                  {rgb(214, 166, 201)}   *    {rgb(178, 186, 216)}please contact us through Discord {rgb(214, 166, 201)}
        {rgb(214, 166, 201)} {Colorate.Horizontal(Colors.blue_to_cyan, "[3]")}{Fore.RESET} - {Colorate.Horizontal(Colors.white_to_blue, "website")}              {rgb(214, 166, 201)}   *    {rgb(178, 186, 216)}dsc.gg/cheatcl                    {rgb(214, 166, 201)}   
        ''')
def rgb(r, g, b):
    return f"\x1b[38;2;{r};{g};{b}m"
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
def chosetod():
    choice = Write.Input(f'''
    ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | # 
    ╰─ ~  ''',Colors.blue_to_white ,interval=0.000)
    return choice
def dtool(entry):
    method()
    dmt = chosetod()
    if dmt == "3":
        if entry["website"] == "none":
            print(f"  {rgb(175, 143, 217)} [i] the link is not available to you")
            time.sleep(2.5)
        else:
            webbrowser.open(entry["website"])
            time.sleep(2.5)
    elif dmt == "2":
        if entry["wget"] == "none":
            print(f"  {rgb(175, 143, 217)} [i] the link is not available to you")
            time.sleep(2.5)
        else:
            download(entry["wget"])
            print(f"  {rgb(175, 143, 217)} [i] ok")
            time.sleep(2.5)            
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
def fetch_link_from_json(json_url, choice):
    try:
        response = requests.get(json_url)
        if response.status_code == 200:
            data = response.json()
            print(f"  {rgb(175, 143, 217)} [i] requests : 200")
            for entry in data["data"]:
                if (entry["choice"] == choice):
                    if entry["page"] == "true":
                        loadingpage(choice)
                        page(entry["ptext"])
                        choice = chosetod()
                        if choice == "0":
                            cls()
                            chose()
                        else:
                            fetch_link_from_json(entry["plink"],choice)
                    else:     
                        print(f"  {rgb(175, 143, 217)} [i] single : true")
                        if choice == "0":
                            cls()
                            chose()
                        else:
                            dtool(entry)
                            break
                    loadingpage(page)
                else:
                    enenror()
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

    titlea()
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

        {rgb(207,131,153)} # - function""")
    fprint(f"""        [f1] - web clonner
        [f2] - mediafire downloader
        [f3] - workupload downloader  
        [f4] - auto clicker  
    """,selected_theme)
    print(f"    {rgb(207,131,153)} # - link")
    fprint(f"""        [l1] - nck's media
        [l2] - discord 
        [l3] - website 
    """,selected_theme)
    current_time = datetime.now()
    choice = chosetod()
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
    elif choice =="f1":
        cls()
        fprint("              [0] - exit ",selected_theme)
        webclonner()
        time.sleep(1.6)
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
    

    global link,text_link
    link, text_link = fs(chosejson, choice)
    if link and text_link:
        global text
        cls()
        print(f" {rgb(145, 192, 135)}Page {choice} - {rgb(178, 186, 216)} 0 to go back")
        text = requests.get(text_link).text
        fprint(text, selected_theme)
        choice = Write.Input(f'''
    ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | # {choice}
    ╰─ ~  ''',Colors.blue_to_white ,interval=0.000)
        
        if choice == "0":
            cls()
            chose()
        else:
            fetch_link_from_json(link, choice)
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
    text = """
         ██████╗██╗  ██╗███████╗ █████╗ ████████╗ ██████╗██╗     
        ██╔════╝██║  ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██║     
        ██║     ███████║█████╗  ███████║   ██║   ██║     ██║     
        ██║     ██╔══██║██╔══╝  ██╔══██║   ██║   ██║     ██║     
        ╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╗███████╗
         ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝╚══════╝                                                     
"""
    faded_text = fade.water(text)
    print(faded_text)
    sel = Write.Input(f'''
        ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | # Enable Discord RPC ?
        ╰─ ~ (yes/no) ?   ''',Colors.white_to_blue ,interval=0.000)
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
    print(f" {rgb(169, 137, 209)}      Invalid theme selected.")
    time.sleep(1.7)



