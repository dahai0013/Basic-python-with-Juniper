import napalm
from jinja2 import Template

#from pprint import pprint as pp

#driver = napalm.get_network_driver('junos')
#device = driver(hostname='172.30.92.193', username='root', password='eyeno1t2!', optional_args={'port': 830})

def get_credential():
   import yaml
   credentialfilename = r'credential_napalm.yaml'
   diccredential = yaml.load(open(credentialfilename))
   hostname = diccredential['hostname']
   username = diccredential['username']
   password = diccredential['password']
   port = diccredential['optional_args']['port']
   # how to close the file ?
   return (hostname,username,password,port)


def render_jinja2(template_name,list_variables):
    #print(list_variables)
    #with open(r"C:\Users\jkriker\Documents\GitHub\JAUT_Training\Basic-python-with-Juniper\Napalm\config_unit.j2") as file_:
    with open(template_name) as file_:
        template = Template(file_.read())
    #print(template.render(unit_id='5', vlan_id=5, subnet="0.5"))
    #print(template.render(list_variables))
    return (template.render(list_variables))


def calcul_scvlanid_ipoct2_ipoct3(unit_id):
    # (vlan_id//4095)
    # Floor division - division that results into whole number adjusted to the left in the number line
    #unit_id = 40004
    s_vlan_id = (unit_id // 4096)
    c_vlan_id = unit_id - ((unit_id//4096)*4096)
    #print (s_vlan_id,c_vlan_id)
    ip_oct2 = (unit_id//256)
    ip_oct3 = unit_id - ((unit_id//256)*256)
    #print (str(oct2)+"."+str(oct3))
    dict_value = {"unit_id":unit_id , "s_vlan_id":s_vlan_id, "c_vlan_id": c_vlan_id,"ip_oct2":ip_oct2, "ip_oct3":ip_oct3 }
    #print(dict_value)
    return(dict_value)


def change_configuration(returntuple, configuration):
    # get configuration file
    #my_filename = r"C:\Users\jkriker\Documents\GitHub\JAUT_Training\Basic-python-with-Juniper\Napalm"
    #my_filename = my_filename + "\\"+str(config_file)
    #print((my_filename))
    # not working !!!!!!
    #configuration = open(my_filename,'r')
    #print ( json.dumps(configuration.read()).rstrip('\n'))
    # get credential
    my_hostname = returntuple[0]
    my_username = returntuple[1]
    my_password = returntuple[2]
    my_port = returntuple[3]
    #print(my_hostname,my_username,my_password,my_port)
    driver = napalm.get_network_driver('junos')
    device = driver(hostname=my_hostname, username=my_username, password=my_password, optional_args={'port': my_port})
    # open session
    device.open()
    # not working with configuration string!!!!!!
    device.load_merge_candidate(config=configuration)
    #device.load_merge_candidate(filename = my_filename)
    device.compare_config()
    print(device.compare_config())
    device.commit_config()
    #device.rollback()
    # close session
    device.close()


def main():
    template_name = r"C:\Users\jkriker\Documents\GitHub\JAUT_Training\Basic-python-with-Juniper\Napalm\config_unit.j2"
    full_config = ""

    print ("start")
    # get credential
    returntuple = get_credential()

    # get the unit_id converted to vlan_id and subnet
    print("get unit_id converted")
    unit_id = 9
    for unit_id in range(1,2200):
        dict_value = calcul_scvlanid_ipoct2_ipoct3(unit_id)
        subnet = str(dict_value['ip_oct2'])+"."+str(dict_value['ip_oct3'])
        #list_dict_value.append = dict_value
        #list_subnet.append = subnet

        # render the jinja2 tamplate
        #print ("render jinja2 template")
        list_variables = {"unit_id" : dict_value['unit_id'] , "vlan_id" : dict_value['c_vlan_id'], "subnet" :subnet}
        #print(type(list_variables))
        configuration = render_jinja2(template_name,list_variables)
        #print("configuration type is: ",type(configuration))
        full_config = full_config + configuration
    #print ("the full config is:\n",full_config)

    # call the change config
    print('-' * 60)
    print("does the config")
    change_configuration(returntuple, full_config)
    print('-' * 60)


if __name__ == "__main__":
    # 1: will strip the first argument, the script.py itself
    main()