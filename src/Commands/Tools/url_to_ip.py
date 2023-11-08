from colorama import Fore
import socket, time

def url_to_ip(args, send, client, gray):
    try:
        url = ""
        if len(args) == 2:
            url = args[1]
            host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
            ip = socket.gethostbyname(host)
            time.sleep(0.2)
            DATA_TEXT = f'\nURL {url} | IP {ip}\n'
            send(client, f'{gray} {DATA_TEXT}')
        else:
            send(client, Fore.LIGHTWHITE_EX + '\n!GETIP [URL]\n')
    except socket.gaierror:
        send(client, Fore.RED + '\nInvalid website\n')