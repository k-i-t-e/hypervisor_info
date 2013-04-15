'''
Created on Apr 12, 2013

@author: kite
'''
import libvirt
import time
import vm_instance
from physical_host import PhysicalHost

# Got to do for all hypervisors simultaneously

class HypervisorInfo:
    def __init__(self, URI, hostname):
        self.conn = libvirt.open(URI)
        self.host = PhysicalHost(hostname)
        
    def getDomainStats(self, period):
        cpuTimeStart = []
        cpuTimeEnd = []
        stats = []
        memory = []
        domains = []
        
        
        domainsIDs_ = self.conn.listDomainsID()
        
        for domID in domainsIDs_:
            domains.append(self.conn.lookupByID(domID))
        
        totalMemory = self.conn.getMemoryStats(-1, 0)['total'] - self.conn.getMemoryStats(-1, 0)['buffers']\
            - self.conn.getMemoryStats(-1, 0)['cached']
        
        for dom_ in domains:
            stat = dom_.getCPUStats(1,0)[0]
            cpuTimeStart.append(stat['cpu_time'])
        
        time.sleep(period)
        
        for dom_ in domains:
            stat = dom_.getCPUStats(1,0)[0]
            cpuTimeEnd.append(stat['cpu_time'])
            memory.append(dom_.memoryStats()['rss'])
    
        for i in xrange(len(cpuTimeStart)):
            time_ = (cpuTimeEnd[i] - cpuTimeStart[i])*(10**(-9))
            memory_ = float(memory[i])/totalMemory
            stats.append( dict(id=domains[i].ID(), time=time_,
                             load_cpu = (time_/period)*100, memory = float(memory[i])/1024, 
                             load_mem = memory_*100) )
        for stat in stats:
            vm = vm_instance.VMInstance('custom', 'vm'+str(stat['id']))
            vm.cpu_usage = stat['load_cpu']
            vm.mem_usage = stat['load_mem']
            self.host.run_vm(vm)
            
        return stats
    
    def showVMs(self):
        self.host.show_host_props()