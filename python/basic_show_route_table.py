import sys
from jnpr.junos import Device
from jnpr.junos.exception import *
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.phyport import PhyPortTable
from pprint import pprint

junos_hosts = [ '172.30.92.193' ]

for ip in junos_hosts:
    try:
        dev = Device(host=ip, user='root', password='eyeno1t2!')
        dev.open()
        routes = RouteTable(dev)
        interfaces = PhyPortTable(dev)
        routes.get()
        #print(type(routes))
        # print(routes.get())
        # print(routes.keys())
        #
        # print the interface list
        # print(interfaces.get())
        # print(type(interfaces.keys()))
        # print(interfaces.keys()[0])
        #
        for route in routes.keys():
            if routes[route]['protocol'] == 'local':
                print (route)
            else:
                #print(route)
                pass
        dev.close()
    except LockError as e:
        print ("The config database was locked!")
    except ConnectTimeoutError as e:
        print ("Connection timed out!")
