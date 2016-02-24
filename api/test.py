#!/usr/bin/python
from pyzabbix import ZabbixAPI
zapi = ZabbixAPI("http://192.168.22.14/zabbix")
zapi.login("Admin", "zabbix")
print "Connected to Zabbix API Version %s" % zapi.api_version()
for h in zapi.host.get(extendoutput=True):
    print h['host']
