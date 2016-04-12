l1 = { "hello" : t1, "test2" : t2 } #dict with all the commands, needs to be extended to cover all the different commands in state.py

def t1():
    print "t1"
def t2():
    print "t2"

def connectS():
    """
    Connect through predefined socket. Socket modul, socket server.
    """

def listCmd():
    """
    print list of all the different commands the player can use
    List of all the commands kept in state modul?
    """
def cmd(cmdW):
    """
    Use cmdW to find the appropriate command in the state module
    """
def cmd(command): # Calls a cmd from dictionary with all the different commands based on the word entered as a parameter
    l1[str(command)]()
    
def quit():
    """
    ends the process
    """
