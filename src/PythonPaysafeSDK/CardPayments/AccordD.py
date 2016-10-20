'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.common.DomainObject import DomainObject


class AccordD(DomainObject):
    '''
    classdocs
    '''

    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['financingType'] = self.financingType
        handler['plan'] = self.plan
        handler['gracePeriod'] = self.gracePeriod
        handler['term'] = self.term
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass

    '''
    Property Financing Type
    '''
    def financingType(self, financing_type):
        self.__dict__['financingType'] = financing_type
        
    '''
    Property Plan
    '''
    def plan(self, plan):
        self.__dict__['plan'] = plan
        
    '''
    Property Grace Period
    '''
    def gracePeriod(self, grace_period):
        self.__dict__['gracePeriod'] = grace_period
        
    '''
    Property Term
    '''
    def term(self, term):
        self.__dict__['term'] = term
