from jnpr.junos import Device
from pprint import pprint

junos_hosts = [ '172.30.92.193' ]

for ip in junos_hosts:
    dev = Device(host=ip, user='root', password='eyeno1t2!')
    dev.open()
    pprint(dev.facts)
    print("\nJLK: version :",dev.facts['version'])
    dev.close()