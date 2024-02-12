import nopecha, os, requests, time, json, zipfile, re, random, string
from nopecha import error
from os import path
from zenrows import ZenRowsClient
import undetected_chromedriver as webdriver
from os import system
from selenium.webdriver.common.by import By
from datetime import datetime
from pystyle import Center, Anime, Colors, Colorate, Write

current_time = datetime.now()


def alert2(type, text):
    if type == "error":
        Write.Print(f"   [e] NOT FOUND | {text} | wait 1s coninue \n", Colors.red_to_white, interval=0.000)
    elif type == "done":
        Write.Print(f"   [+] Successful | {text} | wait 1s coninue \n", Colors.green_to_white, interval=0.000)
    elif type == "info":
        Write.Print(f"   [i] ---------  | {text} | wait 1s coninue \n", Colors.blue_to_white, interval=0.000)


def cyan_gradient(text):
    system("")
    faded = ""

    start_color = (140, 255, 244)
    end_color = (165, 140, 255)

    r_step = (end_color[0] - start_color[0]) / len(text)
    g_step = (end_color[1] - start_color[1]) / len(text)
    b_step = (end_color[2] - start_color[2]) / len(text)

    current_color = start_color

    for line in text.splitlines():
        for character in line:
            faded += (
                f"\033[38;2;{int(current_color[0])};{int(current_color[1])};{int(current_color[2])}m{character}\033[0m"
            )
            current_color = (
                current_color[0] + r_step,
                current_color[1] + g_step,
                current_color[2] + b_step,
            )

        faded += "\n"
    faded = faded.rstrip("\n")
    return faded


clear = lambda: os.system("cls")


class Data():
    CONFIG_PATH = "conf.json"

    def __init__(self):
        if not path.exists(self.CONFIG_PATH):
            with open(self.CONFIG_PATH, "w") as f:
                json.dump({}, f)
        self.load_data()

    def load_data(self):
        with open(self.CONFIG_PATH, "r") as file:
            data = json.load(file)
            self.user = data.get("user", "")
            self.password = data.get("password", "")
            self.zenrowtoken = data.get("zenrowtoken")
            self.nopechatoken = data.get("nopechatoken")

        self.prompt_for_missing_values()

    def prompt_for_missing_values(self):
        for attribute in ("user", "password", "zenrowtoken", "nopechatoken"):
            value = getattr(self, attribute)
            if not value:
                self.prompt_and_save_value(attribute)

    def prompt_and_save_value(self, attribute):
        while True:

            prompt = f"Enter {attribute.replace('_', ' ')}:"
            prompt = cyan_gradient(
                f'''
    ╭─ ♥ {current_time.hour}:{current_time.minute} | {current_time.year}/{current_time.month}/{current_time.day} | # {attribute.replace('_', ' ')}
    ╰─ ~  '''
            )
            new_value = input(prompt)

            setattr(self, attribute, new_value)  # Sets the attribute value
            with open(self.CONFIG_PATH, "w") as f:
                json.dump(self.__dict__, f)  # Saves the configuration
            break


# Get reCaptcha token func
def getRecaptchaToken(driver, id):
    value = ""

    while value == "":
        try:
            value = driver.find_element(By.ID, id).get_attribute("value")
        except Exception:
            pass

        if value == "":
            continue
        else:
            break

    return value


# Get id func
def getId(driver, id):
    value = None

    while value == None:
        try:
            value = driver.find_element(By.NAME, id).get_attribute("value")
        except Exception:
            pass

        if value == None:
            pass
        else:
            return value


# Main func
def main():
    clear()
    print(cyan_gradient("     > Heromc alt gen"))
    Data()
    data = Data()
    user = data.user
    password = data.password
    zenrowstoken = data.zenrowtoken
    nopechatoken = data.nopechatoken
    alert2("done", "Loaded!")
    alert2("info", "[STAGE] 1/4: Checking token...")
    client = ZenRowsClient(zenrowstoken)
    response = client.get("https://httpbin.io/anything")
    if response.status_code == 200:
        alert2("done", "[TOKEN] Zenrows token check PASS.")
    elif response.status_code == 403 or response.status_code == 401:
        alert2("error", "Error: Invaild zenrows token. Please try again with vaild token.")
        os.remove("conf.json")
        time.sleep(3)
        return
    elif response.status_code == 402:
        alert2("error", "Error: Expired zenrows token. Please renew or try with vaild token.")
        os.remove("conf.json")
        time.sleep(3)
        return
    else:
        alert2("error", f"Error {response.status_code}. Please try again.")
        time.sleep(3)
        return

    nopecha.api_key = nopechatoken
    try:
        balance = nopecha.Balance().get()["credit"]
        plan = nopecha.Balance().get()["plan"]
    except nopecha.AuthenticationError:
        alert2("error", "Error: Invaild NopeCHA token. Please try again with vaild token.")
        os.remove("conf.json")
        time.sleep(3)
        return
    finally:
        if int(balance) <= 2:
            alert2("error", "Error: Running out of money in tokens. Please renew token.")
            os.remove("conf.json")
            time.sleep(3)
            return
        else:
            alert2("info", "[TOKEN] NopeCHA token check PASS.")
            time.sleep(3)
            clear()

            alert2("info", "[STAGE] 2/4: Setting NopeCHA token...")
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
    with open("chrome.zip", "wb") as f:
        f.write(requests.get("https://nopecha.com/f/chrome.zip").content)
    with zipfile.ZipFile("chrome.zip", "r") as zip_ref:
        zip_ref.extractall("nopecha")
    options.add_argument(f"--load-extension={os.getcwd()}/nopecha")
    driver = webdriver.Chrome(options=options)
    driver.get(f"https://nopecha.com/setup#{nopechatoken}")
    alert2("info", "Setted NopeCHA token.")
    time.sleep(3)
    clear()

    alert2("info", "[STAGE] 3/4: Getting reCaptcha token...")
    driver.get("https://heromc.net")
    driver.refresh()
    driver.get("https://id.heromc.net/member/dangky.php")
    while True:
        captchaToken = getRecaptchaToken(driver, "g-recaptcha-response")
        if captchaToken != "":
            break
        else:
            captchaToken = getRecaptchaToken(driver, "g-recaptcha-response")
            continue
    tokenValue = getId(driver, "token")
    phpSessionId = driver.execute_script(
        "return document.cookie.match(/PHPSESSID=([^;]+)/)[1]"
    )
    driver.quit()
    alert2("info", "Completed.")
    time.sleep(3)
    clear()

    alert2("info", "[STAGE] 4/4: Creating account...")

    characters = string.ascii_letters + string.digits
    user_num = len(user)
    user_num_left = 16 - user_num
    user_num_left_2 = user_num - 2
    if user_num_left_2 >= 1:
        user_num_left_2 = 1
    random_length = random.randint(user_num_left_2, user_num_left)
    randomuser = "".join(random.choice(characters) for i in range(random_length))
    user = user + "_" + randomuser
    url_reg = "https://id.heromc.net/member/xuly.php"
    header = {"Cookie": f"PHPSESSID={phpSessionId}"}
    postData = f"type=dangky&username={user}&password={password}&passc={password}&email=ryzltln@gmail.com&token={tokenValue}&captcha={captchaToken}"
    data = client.post(
        url_reg,
        params={
            "premium_proxy": "true",
            "proxy_country": "vn",
            "original_status": "true",
            "custom_headers": "true",
        },
        headers=header,
        data=postData,
    )
    if data.status_code == 200:
        data = json.loads(data.text)
        data_dict = data.get("status")
        if data_dict == "ok":
            alert2("done", f"Account created. {user}:{password}")
            # Save information to a text file
            with open("output.txt", "a") as file:
                file.write(f"{user}:{password}\n")
        else:
            alert2("info", "Error when creating account. Please try again.")
    else:
        alert2("info", f"HTTP request failed with status code {data.status_code}")



if __name__ == "__main__":
    main()
