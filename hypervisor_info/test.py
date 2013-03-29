'''
Created on Mar 28, 2013

@author: kite
'''
import libvirt
import sys

conn = libvirt.openReadOnly("qemu:///system")
#conn = libvirt.openReadOnly("qemu://195.208.117.178/system")
if conn == None:
    print 'Failed to open connection to hypervisor'
    sys.exit(1)

#this gets list of domains IDs
domains = conn.listDomainsID()
print domains

dom = conn.lookupByID(domains[0])
print dom.info()

# This gets a lot of xml
cap = conn.getCapabilities()
print "Host capabilities:\n"+cap

hypervisor_type = conn.getType()
print "hypervisor type = "+hypervisor_type


info = conn.getInfo()
print "Info:"
print info

print "cell free memory = "
print conn.getCellsFreeMemory(0, 1)

print "CPU Stats:"
print conn.getCPUStats(1, 0)

# -1 for all cells statistic
mem_stat = conn.getMemoryStats(-1, 0)
print "Memory stats:"
print mem_stat
#try:
#    dom0 = conn.lookupByName("Domain-0")
#except:
#    print 'Failed to find the main domain'
#    sys.exit(1)

#print "Domain 0: id %d running %s" % (dom0.ID(), dom0.OSType())
#print dom0.info()