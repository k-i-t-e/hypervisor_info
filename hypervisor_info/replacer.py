'''
Created on 31.05.2013

@author: Mike
'''
import threading

class Replacer(threading.Thread):
    def __init__(self, period):
        threading.Thread.__init__(self)
        self.period = period
        
    def run(self):
        while True:
            pass
        
def run_replacer(period):
    rep = Replacer(period)
    rep.daemon = True
    rep.start()
    