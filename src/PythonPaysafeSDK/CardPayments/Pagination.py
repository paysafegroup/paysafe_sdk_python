'''
Created on 17-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.common.DomainObject import DomainObject


class Pagination(DomainObject):
    '''
    classdocs
    '''

    def __init__(self,obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['limit'] = self.limit
        handler['offset'] = self.offset
        handler['startDate'] = self.startDate
        handler['endDate'] = self.endDate
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
        
    '''
    Property Limit
    '''
    def limit(self, limit):
        self.__dict__['limit'] = limit
        
    '''
    Property Offset
    '''
    def offset(self, offset):
        self.__dict__['offset'] = offset
        
    '''
    Property Start Date
    '''
    def startDate(self, startDate):
        self.__dict__['startDate'] = startDate
    
    '''
    Property End Date
    '''
    def endDate(self, endDate):
        self.__dict__['endDate'] = endDate
        