# -*- coding: utf-8 -*-
import shelve, time, sys
from File import *

class FileSystem(object):
    
    COMMANDS = ['ls', 'mkdir', 'chdir', 'cd', 'rmdir', 'create', 'read', 'rm', 'mv', 'cp', 'help', 'exit']
    
    def __init__(self):
        self.io = shelve.open('file.sys', writeback=True)
        if self.io.has_key('fs'):
            self.root = self.io['fs']
        else:
            self.root = File('/', 'dir')
        self.curr = self.root

    def mkdir(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            print 'mkdir - make directory'
            print 'usage: mkdir <dir_name>'
        else:
            name = cmd[1]
            if self.curr.is_file(name) == False:
                self.curr.add(name, 'dir')
            else:
                print name, ' - already exists.';

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
                
    
    def rm(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            print 'rm - remove file'
            print 'usage: rm <file_name>'
        else:
            name = cmd[1]
            if self.curr.is_file(name) and not self.curr.is_dir(name):
                self.curr.remove(name)
                print 'File deleted.'
            else:
                print name, ' - invalid file.'

    def ls(self, cmd):
        if(len(cmd) > 1):
            print 'ls - list stats'
            print 'usage: ls'
        self.curr.stat()

    def create(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            print 'create - create a file'
            print 'usage: create <file_name>'
        else:
            name = cmd[1]
            self.curr.add(name, 'file', raw_input('Enter file context: '))
            
    def read(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            print 'read - read a file'
            print 'usage: read <file_name>'
        else:
            name = cmd[1]
            if self.curr.is_file(name):
                self.curr.get(name).read()
            else:
                print name, 'invalid file'

    def mv(self, cmd):
        if len(cmd) < 3 or cmd[1] == '':
            print 'mv - rename a file'
            print 'usage: mv <old_name> <new_name>'
        else:
            old_name = cmd[1]
            new_name = cmd[2]
            if self.curr.is_file(old_name):
                self.curr.get(old_name).rename(new_name)
            else:
                print old_name, 'invalid file'

    def cp(self, cmd):
        if len(cmd) < 3 or cmd[1] == '':
            print 'cp - copy a file'
            print 'usage: cp <src> <dest>'
        else:
            src = cmd[1]
            dest = cmd[2]
            if self.curr.is_file(src):
                self.curr.copy(src, dest)
            else:
                print src, 'invalid file'
    
    def save(self):
        self.io['fs'] = self.root
        self.io.sync()
            
    def help(self, cmd):
        print 'COMMANDS: mkdir, ls, chdir, rmdir, create, read, mv, cp, rm, exit'

    def exit(self, cmd):
        sys.exit(0)
"""
Instanciate a FileSystem, that accepts commands. 
Catches invalid commands and prints instructions for user.
"""
def main():
    fs = FileSystem()
    while True:
        cmd = raw_input('> ').split(' ');
        method = None
        try:
            method = getattr(fs, cmd[0])
        except AttributeError:
            print 'Invalid command. Type "help".'
        if method is not None and cmd[0] in FileSystem.COMMANDS and callable(method):
            method(cmd)
            #fs.save()
        else:
            print 'Invalid command. Type "help".'
main()