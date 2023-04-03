#!/bin/python3

import dns.resolver
import whois
import threading
import random
import string

zone = '.ru'
def domain1(fzone):
    domen = ''
    for i in range(3):
        domen += random.choice(string.ascii_lowercase + string.digits)
    domen += fzone
    return domen

def domain_founder():
    domain_name = domain1(zone)
    print(domain_name)
    try:
        result = dns.resolver.resolve(domain_name)
    except KeyboardInterrupt:
        quit()
    except:
        try:
            result = whois.whois(domain_name)
        except:
            print("Domain found " + domain_name)
while True:
    for i in range(5):
        my_thread = threading.Thread(
            target=domain_founder)
        my_thread.start()
    for i in range(5):
        my_thread.join()