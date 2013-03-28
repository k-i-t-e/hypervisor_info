'''
Created on Mar 28, 2013

@author: kite
'''
import libvirt
import sys

conn = libvirt.openReadOnly("qemu:///system")
if conn == None:
    print 'Failed to open connection to hypervisor'
    sys.exit(1)

domains = conn.listDomainsID()

print domains
dom = conn.lookupByID(domains[0])
dom0_info =  dom.info()
print dom0_info

#try:
#    dom0 = conn.lookupByName("Domain-0")
#except:
#    print 'Failed to find the main domain'
#    sys.exit(1)

#print "Domain 0: id %d running %s" % (dom0.ID(), dom0.OSType())
#print dom0.info()