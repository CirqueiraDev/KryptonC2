from colorama import Fore
import requests

def get_location(ip_addr):
    ip_address = ip_addr
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    version = response['version']
    city = response['city']
    region_city = response['region']
    country_name = response['country_name']
    latitude = response['latitude']
    longitude = response['longitude']
    timezone = response['timezone']
    network = response['network']

    location_data = f'''
IPv4          : {ip_address}
NETWORK       : {network}
VERSION       : {version}

# LOCATION
CITY          : {city}
REGION        : {region_city}
COUNTRY       : {country_name}
LATITUDE      : {latitude}
LONGITUDE     : {longitude}

# TIME
TIMEZONE      : {timezone}
'''

    return location_data

def ip_to_loc(args, send, client, gray):
    try:
        ip = ''
        if len(args) == 2:
            ip = str(args[1])
            ip_location = get_location(ip)
            for x in ip_location.split('\n'):
                send(client, f'{gray}' + x)
        else:
            send(client, Fore.LIGHTWHITE_EX + '\n!GEOIP [IP]\n')
    except:
        send(client, Fore.RED + '\nInvalid data\n')