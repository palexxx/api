from pyzabbix import ZabbixAPI, ZabbixAPIException
import sys

# The hostname at which the Zabbix web interface is available
ZABBIX_SERVER = 'http://192.168.22.14/zabbix'

zapi = ZabbixAPI(ZABBIX_SERVER)

# Login to the Zabbix API
zapi.login('Admin', 'zabbix')

host_name = '192.168.22.13'
#add group APP   
group=zapi.hostgroup.create(name="APP")
print("Added hostgroup with groupid {0} to host: {1}".format(group["groupids"][0],host_name))

#fgroup=zapi.hostgroup.get(output="extend",filter={"name":"APP"})
#print ("fgr_id= ".format(fgroup["groupids"][0]))

#group=zapi.hostgroup.create(name="DB")
#print("Added hostgroup with groupid {0} to host: {1}".format(group["groupids"][0],host_name))

gr_id=group["groupids"][0]
print("gr= " + gr_id)
#gr_id=40
host=zapi.host.create(
    host="APP1",
    interfaces=[{"type":1,"main":1,"useip":1,"ip":"192.168.22.22","dns":"APP1","port":"10050"}],
    groups=[{"groupid":gr_id}]
    )
    
host=zapi.host.create(
    host="APP2",
    interfaces=[{"type":1,"main":1,"useip":1,"ip":"192.168.22.23","dns":"","port":"10050"}],
    groups=[{"groupid":gr_id}]
    )

