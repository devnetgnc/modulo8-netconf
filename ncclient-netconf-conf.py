from ncclient import manager
import xml.dom.minidom



netconf_filter ="""
<filter>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""

netconf_hostname= """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <hostname>NETCONF-HOSTNAME</hostname>
 </native>
</config>      
"""
netconf_loopback="""
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <interface>
 <Loopback>
 <name>1</name>
 <description>My first NETCONF loopback</description>
 <ip>
 <address>
 <primary>
 <address>10.1.1.1</address>
 <mask>255.255.255.0</mask>
 </primary>
 </address>
 </ip>
 </Loopback>
 </interface>
</native>
</config>

"""

netconf_newloop ="""
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <interface>
 <Loopback>
 <name>2</name>
 <description>My second NETCONF loopback</description>
 <ip>
 <address>
 <primary>
 <address>10.1.1.1</address>
 <mask>255.255.255.0</mask>
 </primary>
 </address>
 </ip>
 </Loopback>
 </interface>
</native>
</config>

"""

with manager.connect(
    host="10.10.20.175",
    port=830,
    username="cisco",
    password="cisco",
    hostkey_verify=False

)as m:
    #netconf_reply = m.get_config(source="running", filter=netconf_filter)
    #netconf_reply = m.edit_config(target="running", config =netconf_hostname)
    #netconf_reply = m.edit_config(target="running", config =netconf_loopback)
    netconf_reply = m.edit_config(target="running", config =netconf_newloop)
    #print(f'Recuperar configuracion: {netconf_reply}')   
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())  


