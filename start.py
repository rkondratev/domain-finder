#!/bin/python3

import dns.resolver
import whois

with open('sgb-words.txt') as domains:
    for domain in domains:
        domain = domain.strip() + ".ru"
        try:
            result = dns.resolver.resolve(domain, 'A')
        except KeyboardInterrupt:
            break
        except:
            try:
                result = whois.whois(domain)
            except:
                print("Domain found " + domain)