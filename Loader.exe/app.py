import requests,time,os,colorama,sys,ctypes,webbrowser,shutil
from pystyle import  Center, Anime, Colors, Colorate, Write
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
def info():
        Write.Print(f"""
    > Discord: dsc.gg/cheatcl   
    > Youtbe: yt/@necakco       
    > Website: cheatcl.web.app                                                                                     
    """,Colors.white, interval=0.000)
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
def fetch_link_from_json(json_url, choice):
    try:
        response = requests.get(json_url)
        if response.status_code == 200:
            data = response.json()
            for entry in data["data"]:
                if (entry["choice"] == choice)and(entry["type"] == "download"):
                    return entry["link"]
                elif (entry["choice"] == choice)and(entry["type"] == "link"):
                    open_link(entry["link"])
                    cls()
                    chose()
            return enenror()
        else:
            return "Failed to fetch JSON from URL"
    except requests.exceptions.RequestException:
        return enenror()
def fs(json_url, choice):
    try:
        response = requests.get(json_url)
        if response.status_code == 200:
            data = response.json()
            for entry in data["data"]:
                if entry["choice"] == choice:
                    return entry["link"], entry["text"]
            return "Choice not found in JSON", ""
        else:
            return "Failed to fetch JSON from URL", ""
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
                Write.Print(f"     ~/> Downloaded {data_downloaded:.2f} KB / {total_size:.2f} KB",  Colors.blue_to_white , interval=0.000 ,end='\r')
        Write.Print(f"     ~/> Downloaded the file to {save_path} \n",Colors.blue_to_white , interval=0.000)
        download_folder = os.path.expanduser("~" + os.sep + "Downloads")
        downloaded_file_path = os.path.join(download_folder, save_path)
        shutil.move(save_path, downloaded_file_path)
        Write.Print(f"     ~/> Moved the file to Downloads folder: {downloaded_file_path}",Colors.blue_to_white, interval=0.000)
        webbrowser.open("file://" + download_folder)
        cls()
        chose()
    except Exception as e:
        Write.Print(f"     ~/> An error occurred: {str(e)}",Colors.blue_to_white, interval=0.000)
# chose
chosetext = "https://cheatcl-file.web.app/fetch/chose/chose.txt"
chosejson = "https://cheatcl-file.web.app/fetch/chose/chose.json"
def enenror():
    Write.Print("       > NOT FOUND | wait 4s coninue", Colors.blue_to_white, interval=0.000)
    time.sleep(1.5)
    chose() 
def chose():
    setTitle(f"NCK Launcher")
    clear = lambda: os.system('cls')
    clear()
    colorama.init()
    info()
    print('\n \n')
    Write.Print(f"""
                      ___ _                _     ___   __  
                     / __\ |__   ___  __ _| |_  / __\ / /  
                    / /  | '_ \ / _ \/ _` | __|/ /   / /   
                   / /___| | | |  __/ (_| | |_/ /___/ /___ 
                   \____/|_| |_|\___|\__,_|\__\____/\____/ 
    """,Colors.red_to_white, interval=0)
    print('\n')
    try:
        response = requests.get(chosetext)
        if response.status_code == 200:
            Write.Print(response.text,Colors.red_to_white, interval=0.000)
        else:
            print(f"falled: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"falled: {e}")
    print()
    choice = Write.Input(f'     ~/> ',Colors.blue_to_white ,interval=0.000)
    link, text_link = fs(chosejson, choice)

    if link and text_link:
        cls()
        print(f" Page {choice} - 0 to go back")
        text = requests.get(text_link).text
        Write.Print(text,Colors.red_to_white, interval=0.000)
        choice = Write.Input(f'     ~/> ',Colors.blue_to_white ,interval=0.000)
        if (choice == "0") :
            chose()
        link = fetch_link_from_json(link, choice)
        download(link)
    else:
        cls()
        input("Error fetching data . Press ENTER to close. ")
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