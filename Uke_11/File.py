# -*- coding: utf-8 -*-
import time

class File(object):

    """
    Creates an empty list
    @param name of file
    @param type of file
    @param parent(diretory) of file.
    @param text to add to this file object. 
    """
    def __init__(self, name, type, parent=None, text=''):
        self.list = []
        self.name = name
        self.type = type
        self.time = int(time.time())
        self.parent = parent
        self.text = text
    
    def is_file(self, name):
        for node in self.list:
            if node.name == name:
                return True
        return False
    
    def is_dir(self, name):
        if(self.is_file(name)) and self.get(name).type == 'dir':
            return True
        return False

    def get(self, name):
        for node in self.list:
            if node.name == name:
                return node
        
    def add(self, name, type, text=''):
        self.list.append(File(name, type, self, text))
             
    def remove(self, name):
        self.list.remove(self.get(name))
            
    def rename(self, name):
        self.name = name

    def copy(self, src, dest):
        src = self.get(src)
        self.add(dest, src.type, src.text)

    def stat(self):
        print 'Listing', self.name
        for node in self.list:
            print 'Name:', node.name, '; Created:', node.time, '; Type:', node.type
            
    def read(self):
        print 'Reading file:', self.name
        print self.text