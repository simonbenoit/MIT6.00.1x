# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    if newFrob.myName() > atMe.myName():
        previous = atMe
        while previous.getAfter() != None and newFrob.myName() > previous.getAfter().myName():
            previous = previous.getAfter()
        newFrob.setAfter(previous.getAfter())
        newFrob.setBefore(previous)
        if previous.getAfter() != None:
            previous.getAfter().setBefore(newFrob)
        previous.setAfter(newFrob)
    else:
        after = atMe
        while after.getBefore() != None and newFrob.myName() < after.getBefore().myName():
            after = after.getBefore()
        newFrob.setAfter(after)
        newFrob.setBefore(after.getBefore())
        if after.getBefore() != None:
            after.getBefore().setAfter(newFrob)
        after.setBefore(newFrob)
        