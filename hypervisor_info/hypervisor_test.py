'''
Created on Apr 12, 2013

@author: kite
'''

import hypervisor_info
from algorithm import ScheduldingAlgorithm

npc11 = hypervisor_info.HypervisorInfo("qemu:///system", 'npc11')
npc10 = hypervisor_info.HypervisorInfo("qemu+ssh://root@195.208.117.184/system", 'npc10')

print npc11.getDomainStats(10)
npc11.showVMs()

print npc10.getDomainStats(10)
npc10.showVMs()

test = ScheduldingAlgorithm()

test.VMs = []
test.VMs.extend(npc10.host.assigned_vms)
test.VMs.extend(npc11.host.assigned_vms)
test.hosts = [npc10.host, npc11.host]

test.show()

i = test.simulated_annealing_abstract(test.root_mean_sqr)

test.show_hosts()
print 'made '+str(i)+' iterations'