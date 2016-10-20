'''
Created on 17-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK.common.FieldErrors import FieldErrors
from PythonPaysafeSDK.common.Link import Link


class Error(DomainObject):
    '''
    classdocs
    '''

    def __init__(self, obj):
        '''
        Constructor
        '''       
        # Handler dictionary
        handler = dict()
        handler['links'] = self.links
        handler['code'] = self.code
        handler['message'] = self.message
        handler['fieldErrors'] = self.fieldErrors
        handler['details'] = self.details

        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
        
    '''
    Property Links
    @param: Link Object, List of Link Objects
    '''   
    def links(self, links):
        if isinstance(links, Link):
            addr = Link(links.__dict__)
            self.__dict__['links'] = addr.__dict__
        else:
            for count in range(0, links.__len__()):
                addr_obj = Link(links[count])
                self.__dict__.setdefault('links', []).append(addr_obj) 
        
    '''
    Property Code
    '''   
    def code(self, code):
        self.__dict__['code'] = code
        
    '''
    Property Message
    '''   
    def message(self, message):
        self.__dict__['message'] = message
        
    '''
    Property Field Errors
    '''   
    def fieldErrors(self, field_errors):
        if isinstance(field_errors, FieldErrors):
            addr = FieldErrors(field_errors.__dict__)
            self.__dict__['fieldErrors'] = addr.__dict__
        else:
            for count in range(0, field_errors.__len__()):
                addr_obj = FieldErrors(field_errors[count])
                self.__dict__.setdefault('fieldErrors', []).append(addr_obj) 

        #fe = FieldErrors(field_errors)
        #self.__dict__['fieldErrors'] = fe
        
    '''
    Property Details
    '''   
    def details(self, details):
        self.__dict__['details'] = details
