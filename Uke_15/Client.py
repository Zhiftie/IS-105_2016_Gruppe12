from test import test1 as t

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
    for k in l1:
        print k + " : Desc of key"
def cmd(cmdW):
    """
    Use cmdW to find the appropriate command in the state module
    """
def cmd(): # Calls a cmd from dictionary with all the different commands based on the word entered as a parameter
    #l1[raw_input("Insert Command >>> ")]()
    inp = raw_input(">>> ")
    if inp in l1:
        l1[inp]()
        return inp
    else:
        print "Command not found"
    
def quit():
    """
    ends the process
    """
    print "quit"

l1 = { "hello" : t1, "test2" : t2, "quit" : quit, "ls" : listCmd  } #dict with all the commands, needs to be extended to cover all the different commands in state.py


while True:
    command = cmd()
    if command is "quit":
        break
    
    
        