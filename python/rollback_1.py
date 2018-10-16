from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from pprint import pprint

junos_hosts = [ '192.168.56.15' ]

for ip in junos_hosts:
    dev = Device(host=ip, user='lab', password='lab123')
    dev.open()
    config = Config(dev)
    config.lock()
    config.rollback(rb_id=1)
    config.pdiff()
    config.commit()
    config.unlock()
    dev.close()