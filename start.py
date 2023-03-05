#!/bin/python3

import dns.resolver
import whois

domain_list = ["yandex", "google", "fgfjghjfgdfsf"]

# for domain in domain_list:
#     try:
#         result = dns.resolver.resolve(domain + ".ru", 'A')
#     except:
#         print("Домен возможно свободен " + domain + ".ru")

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
                print("Домен возможно свободен " + domain)