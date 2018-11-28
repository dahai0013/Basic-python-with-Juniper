import napalm
from pprint import pprint as pp

driver = napalm.get_network_driver('junos')
device = driver(hostname='172.30.92.193', username='root', password='eyeno1t2!', optional_args={'port': 830})
device.open()

pp(device.username)
pp(device.device)
#pp(device.get_facts())
pp("The S/N is: "+device.get_facts()['serial_number'])

device.close()