from urllib.request import urlopen
from sys import argv, exit
from colorama import Fore

def check(url):
    ''' check given URL is vulnerable or not '''

    try:
        if "http" not in url: url = "http://" + url

        data = urlopen(url)
        headers = data.info()

        if not "X-Frame-Options" in headers: return True
        if not "Content-Security-Policy" in headers: return True

    except: return False


def listVulnerableSite(url):
    f=open("Vulnerable.txt", "a+")
    f.write(url)
    f.close()


def main():

    try: sites = open(argv[1], 'r').readlines()
    except: print("[*] Usage: python(3) clickjacking_tester.py <file_name>"); exit(0)

    for site in sites[0:]:
        status = check(site)

        if status:
            print("[+] "+Fore.GREEN+site.split('\n')[0] +Fore.WHITE+ " is "+Fore.RED+"vulnerable"+Fore.WHITE+" to ClickJacking")
            listVulnerableSite(site.split('\n')[0])
        
        elif not status: print("[+] "+Fore.GREEN+site.split('\n')[0] +Fore.WHITE+ " is "+Fore.CYAN+" not vulnerable"+Fore.WHITE+" to ClickJacking")
        else: print('Every single thing is crashed, Python got mad, dude wtf you just did?')

if __name__ == '__main__': main()
