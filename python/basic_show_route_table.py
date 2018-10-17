import sys
from jnpr.junos import Device
from jnpr.junos.exception import *
from jnpr.junos.op.routes import RouteTable
from pprint import pprint

junos_hosts = [ '192.168.56.15' ]

for ip in junos_hosts:
    try:
        dev = Device(host=ip, user='lab', password='lab123')
        dev.open()
        routes = RouteTable(dev)
        routes.get()
        for route in routes.keys():
            if routes[route]['protocol'] == 'local':
                print (routes)
            else:
                print(routes)
                pass
        dev.close()
    except LockError as e:
        print ("The config database was locked!")
    except ConnectTimeoutError as e:
        print ("Connection timed out!")
