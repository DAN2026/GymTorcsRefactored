
class Utility:
    
    def __init__(self):
        pass

    @staticmethod
    def destringify(self, s):
        '''makes a string into a value or a list of strings into a list of
        values (if possible)'''
        if not s: return s
        if type(s) is str:
            try:
                return float(s)
            except ValueError:
                print("Could not find a value in %s" % s)
                return s
        elif type(s) is list:
            if len(s) < 2:
                return self.destringify(s[0])
            else:
                return [self.destringify(i) for i in s]
