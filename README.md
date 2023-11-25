<h1 align="center">Krypton Botnet</h1>

<p align="center">
    <img width="720" height=430" src="https://github.com/CirqueiraDev/KryptonC2/assets/118860604/7bab743a-1af4-4d48-9425-b2037808fc86">
</p>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br>
<br>
 **KryptonC2** is a basic open source [denial of service](https://en.wikipedia.org/wiki/Denial-of-service_attack) [botnet](https://en.wikipedia.org/wiki/Botnet) system written in Python 3, consists of a connect and control server and a bot malware script.

# Installation
1. Install Git and Python 3 on your server.
2. Clone the KryptonC2 Github repository to your server via Git: `$ git clone https://github.com/CirqueiraDev/KryptonC2`.
3. Change the host address and C&C port in the configuration section in [bot.py](src/Payload/bot.py) to your server address and C&C port.
4. Install the requirements.txt
5. Start the C2 server by executing the command: `$ python main.py`.
6. Add accounts in [logins.txt](/src/logins.txt) using the format: `username:password`.
7. Configure the port on the [config.json](/src/config.json) `{
"cnc_host": "0.0.0.0",
  "reg_host": "0.0.0.0",
  "cnc_port": 5511,
  "reg_port": 5512
}`.

8. Connect to the server through [PuTTY](https://www.putty.org/) on a raw socket connection.

*Compiling the malware and installing it on vulnerable devices won't be told as it's highly illegal to get remote access to devices without permission. Use of this project for illegal activities is at own risk! I'm not responsible for any of your taken actions!*

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br>

# News
1. New method  `(HTTP SPOOFER) L7 Method`. 11/11/2023
2. New method  `(NTP Reflection + Payload) L4 Method`. 11/13/2023
3. New method  `(Memcached + Custom Payload) L4 Method`. 11/13/2023
4. New method  `(POD) L3 Method`. 11/14/2023
5. New method  `(ICMP) L3 Method`. 11/14/2023
6. Updated Method  `(HTTP IO) L7 Method`. 11/14/2023

# Ideas
1. `Method:  OVH | Bypass OVH` *L7 method*
2. `Method:  POST | POST Flood` *L7 method*
3. `Method:  STRESS | Send HTTP Packet With High Byte` *L7 method*
4. `Method:  OSTRESS | STRESS Without Proxy` *L7 method*
5. `Method:  BYPASS | Bypass Normal AntiDDoS` *L7 method*
6. `Method:  DGB | DDoS Guard Bypass` *L7 method*
7. `Method:  AVB | Arvan Cloud Bypass` *L7 method*
8. `Method:  SYN | SYN Flood` *L4 method*
9. **Send attacks with API's**

<br>

---

**💰 Donation Links:**
#### Donate Links

<b>BTC</b>: <code>bc1qynerkzreqgeuhfywfelhz45df2a73f38cmctzu</code></br>
<b>ETH</b>: <code>0xb685A72EdA6a016A43d75D269FdFa6315C80F8c9</code></br>
<b>Paypal: Contact me *Discord:  cirquera*</b>

<h1>Author 👑</h1>

- **CirqueiraDev**
- ✉ My Email: **Soon**
<div>
    
  [![Youtube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@cirqueiradev)
  [![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/cirqueira.lol/)
  [![Tiktok](https://img.shields.io/badge/TikTok-000000?style=for-the-badge&logo=tiktok&logoColor=white)](https://tiktok.com/@cirqueiradev)
</div>
