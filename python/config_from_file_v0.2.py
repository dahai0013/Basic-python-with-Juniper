from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import *
from pprint import pprint
from jinja2 import Template
import yaml
import sys

host = 'vQFX1'
junos_hosts = [ '192.168.56.15' ]
yaml_file = '../yamlfiles/OSPF_iBGP_config.yaml'
jinja2_file = '../jinja2files/OSPF_iBGP_config.j2'
#jinja2_file = '../jinja2files/firewall_filter.j2'

for ip in junos_hosts:
    try:
        # Open and read the YAML file.
        with open( yaml_file , 'r') as fh:
            data = yaml.load(fh.read())

        # print the rended file
        #print ("\nResults for device " + host)
        #print ("------------------------" )
        #print (myConfig)

        #write to the Juniper Box
        dev = Device(host=ip, user='lab', password='lab123')
        dev.open()
        config = Config(dev)
        config.lock()
        config.load(template_path=jinja2_file, template_vars=data, merge=True, format="text")
        config.pdiff()
        config.commit()
        config.unlock()
        dev.close()
    except LockError as e:
        print ("The config database was locked!")
    except ConnectTimeoutError as e:
        print ("Connection timed out!")
