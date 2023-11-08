<h1 align="center">Krypton Botnet</h1>

<p align="center">
    <img width="719" height="460" src="https://github.com/CirqueiraDev/KryptonC2/assets/118860604/5ceb037c-3c21-498c-9587-0cd376cd180b">
</p>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br>

 **KryptonC2** is a basic open source [denial of service](https://en.wikipedia.org/wiki/Denial-of-service_attack) [botnet](https://en.wikipedia.org/wiki/Botnet) system written in Python 3, consists of a connect and control server and a bot malware script.

# Installation
1. Install Git and Python 3 on your server.
2. Clone the PYbot Github repository to your server via Git: `$ git clone https://github.com/CirqueiraDev/KryptonC2`.
3. Change the host address and C&C port in the configuration section in [bot.py](src/Payload/bot.py) to your server address and C&C port.
4. Start the CnC server by executing the command: `$ python cnc.py <cnc port>`.
5. Add accounts in [logins.txt](/src/logins.txt) using the format: `username:password`.
6. Connect to the server through [PuTTY](https://www.putty.org/) on a raw socket connection.

*Compiling the malware and installing it on vulnerable devices won't be told as it's highly illegal to get remote access to devices without permission. Use of this project for illegal activities is at own risk! I'm not responsible for any of your taken actions!*
