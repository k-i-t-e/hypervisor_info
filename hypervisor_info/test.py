'''
Created on Mar 28, 2013

@author: kite
'''
import libvirt
import sys
import libvirtmod

conn = libvirt.openReadOnly("qemu:///system")
#conn = libvirt.openReadOnly("qemu://195.208.117.178/system")
if conn == None:
    print 'Failed to open connection to hypervisor'
    sys.exit(1)

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

print "Sys Info:"
print conn.getSysinfo(0)

#this gets list of domains IDs
print "Domain IDs"
domains = conn.listDomainsID()
print domains

print "Info for Domain number 0"
dom = conn.lookupByID(domains[0])
print dom.name()
print dom.info()
print dom.OSType()

print "Memory stats for Dom number 0"
print dom.memoryStats()

print "Max memory:"
print dom.maxMemory()

print "Max VCPUS"
print dom.maxVcpus()

print "Memory Parameters"
print dom.memoryParameters(0)

print "Scheduler parameters" 
print dom.schedulerParameters()

print "Scheduler type:"
print dom.schedulerType()

print "Job info"
print dom.jobInfo()

print "Domain state:"
print dom.state(0)

print "VCPUS information:"
print dom.vcpus()

#1 - secure or 4 - update CPU requirements
print "dom XML description"
print dom.XMLDesc(1)
#try:
#    dom0 = conn.lookupByName("Domain-0")
#except:
#    print 'Failed to find the main domain'
#    sys.exit(1)

#print "Domain 0: id %d running %s" % (dom0.ID(), dom0.OSType())
#print dom0.info()