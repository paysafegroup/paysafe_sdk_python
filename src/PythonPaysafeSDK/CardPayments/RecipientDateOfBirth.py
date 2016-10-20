'''
Created on 17-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.common.DomainObject import DomainObject


class RecipientDateOfBirth(DomainObject):
    '''
    classdocs
    '''

    def __init__(self,obj):
        '''
        Constructor
        '''        
        if obj is not None:
            self.setProperties(obj)
        else:
            pass
               
    '''
    Property Day
    '''
    def day(self, day):
        self.__dict__['day'] = day
    
    '''
    Property Month
    '''
    def month(self, month):
        self.__dict__['month'] = month
    
    '''
    Property Year
    '''
    def year(self, year):
        self.__dict__['year'] = year
        