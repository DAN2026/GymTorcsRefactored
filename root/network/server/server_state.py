from network.utils import Utility

class ServerState():
    
    '''What the server is reporting right now.'''
    
    def __init__(self):
        self.servstr= str()
        self.d= dict()
        self.data_size = 2**17

    def parse_server_str(self, server_string):
        
        '''Parse the server string.'''
        
        self.servstr= server_string.strip()[:-1]
        
        sslisted= self.servstr.strip().lstrip('(').rstrip(')').split(')(')
        
        for i in sslisted:
            w= i.split(' ')
            self.d[w[0]]= Utility.destringify(w[1:])

    def __repr__(self):
        
        # Comment the next line for raw output:
        
        return self.fancyout()
    
        # -------------------------------------
        
        out= str()
        for k in sorted(self.d):
            strout= str(self.d[k])
            if type(self.d[k]) is list:
                strlist= [str(i) for i in self.d[k]]
                strout= ', '.join(strlist)
            out+= "%s: %s\n" % (k,strout)
        return out