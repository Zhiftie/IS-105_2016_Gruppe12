# -*- coding: utf-8 -*-
"""
Denne modulen holder dictionary med userinputs som key, f.eks. chdir, rmdir, mkdir osv. og knytte disse opp til metoder som value. 
"""
class Commands():
    def __init__(self):
        self.cmd = {} # er implementeres kommandoer brukeren kan utnytte, f.eks. chdir, rmdir osv. og knyttes opp til metoder som value. 
    
    
    #Remove rmdir
    def rmdir(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            print 'rmdir - remove directory'
            print 'usage: rmdir <dir_name>'
        else:
            name = cmd[1]
            if self.curr.is_dir(name):
                self.curr.remove(name)
                print 'Directory deleted.'
            else:
                print name, ' - invalid directory.' 
        
        
    #Sjekker om noden er en mappe (is_dir):
    #Return True if path is an existing directory
    
    def is_dir(self, name):
        if(self.is_file(name)) and self.get(name).type == 'dir':
            return True
        return False
    
        
    #Bytte til spesifisert mappe(chdir):
    def chdir(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            print 'chdir - change directory.'
            print 'usage: chdir <dir_name>'
        else:
            name = cmd[1]
            if name == '..':
                if self.curr.parent is not None:
                    self.curr = self.curr.parent
                elif self.curr.is_dir(name):
                    self.curr = self.curr.get(name)
                else:
                    print name, ' - invalid directory.'
