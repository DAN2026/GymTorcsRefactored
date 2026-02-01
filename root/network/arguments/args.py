import sys

class Arguments:
    
    #region Class description
    '''
    This class handles arguments the user may use.
    '''
    #endregion
    
    TORCS_VERSION = "20130505-2"
    
    def __init__(self):
        # Build the help message
        self.ophelp = 'Options:\n'
        self.ophelp += ' --host, -H <host>    TORCS server host. [localhost]\n'
        self.ophelp += ' --port, -p <port>    TORCS port. [3001]\n'
        self.ophelp += ' --id, -i <id>        ID for server. [SCR]\n'
        self.ophelp += ' --steps, -m <#>      Maximum simulation steps. 1 sec ~ 50 steps. [100000]\n'
        self.ophelp += ' --episodes, -e <#>   Maximum learning episodes. [1]\n'
        self.ophelp += ' --track, -t <track>  Your name for this track. Used for learning. [unknown]\n'
        self.ophelp += ' --stage, -s <#>      0=warm up, 1=qualifying, 2=race, 3=unknown. [3]\n'
        self.ophelp += ' --debug, -d          Output full telemetry.\n'
        self.ophelp += ' --help, -h           Show this help.\n'
        self.ophelp += ' --version, -v        Show current version.'
        
        self.usage = 'Usage: %s [ophelp [optargs]] \n' % sys.argv[0]
        self.usage += self.ophelp

    def get_usage(self):
        return self.usage

    def get_version(self):
        return self.TORCS_VERSION