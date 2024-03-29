import os,sys
import requests
import shutil
from bs4 import BeautifulSoup
from pystyle import Write, Colors

base_dir = os.getcwd()

Write.Print("""
   ╔══════════════════════════════════════════════════════════╗
   ║  ___ _                                                   ║     
   ║ / __\ |__   ___  __ _| |_  / __\ / /                     ║ 
   ║/ /  | '_ \ / _ \/ _` | __|/ /   / /    yt/@necakco       ║ 
   ║\ \___| | | |  __/ (_| | |_/ /___/ /___  dsc.gg/cheatcl   ║
   ║ \____|_| |_|\___|\__,_|\__\____/\____/  cheatcl.web.app  ║
   ╚══════════════════════════════════════════════════════════╝
""", Colors.blue_to_white, interval=0)

site_name = Write.Input(f'      Link website ~/>    ', Colors.blue_to_white, interval=0.000)
site_folder = Write.Input(f'      Fodler Name ~/>    ', Colors.blue_to_white, interval=0.000)
# Set the specific folder where you want to save the files
project_path = os.path.join(base_dir, site_folder)
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

                # Remove project name from the file path
                file_name = file_name.replace(site_name, "")

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

            # Remove project name from the file path
            file_name = file_name.replace(site_name, "")

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

            # Remove project name from the file path
            file_name = file_name.replace(site_name, "")

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
        print("Working with : {}".format(link))

        path_s = link.split("/")
        file_name = ""
        for i in range(3, len(path_s)):
            file_name = file_name + "/" + path_s[i]

        if file_name[len(file_name) - 1] != "/":
            file_name = file_name + "/"

        try:
            r = requests.get(link)
        except requests.exceptions.ConnectionError:
            print("Connection Error")
            sys.exit(1)

        if r.status_code != 200:
            print("Invalid Response")
            sys.exit(1)

        os.makedirs(os.path.dirname(project_path + file_name.split("?")[0]), exist_ok=True)
        with open(project_path + file_name.split("?")[0] + "index.html", "wb") as f:
            text = r.text.replace(site_name, "")
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
print("Link crawled\n")
for link in visited_links:
    print("---- {}\n".format(link))

print("\n\n\nLink error\n")
for link in error_links:
    print("---- {}\n".format(link))
