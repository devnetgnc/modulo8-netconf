from ncclient import manager
import xml.dom.minidom



netconf_filter ="""
<filter>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""


with manager.connect(
    host="10.10.20.175",
    port=830,
    username="cisco",
    password="cisco",
    hostkey_verify=False

)as m:
    netconf_reply = m.get_config(source="running", filter=netconf_filter)
    #print(f'Recuperar configuracion: {netconf_reply}')   
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())  
'''
print("Capabilities (YANG MODELS")
for capability in m.server_capabilities:
    print(capability)
'''

