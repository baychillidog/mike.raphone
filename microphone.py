#

#

class Microphone(object):
    
    def __init__(self,sound):
        self.sound =  sound
    
    
    def record(self):
        print "I Recorded %s"%(self.sound,)