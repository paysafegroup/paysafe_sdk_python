'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.common.DomainObject import DomainObject


class Link(DomainObject):
    '''
    classdocs
    '''
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['rel'] = self.rel
        handler['returnKeys'] = self.returnKeys
        handler['uri'] = self.uri
        handler['keys'] = self.keys
        handler['href'] = self.href
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
        
    '''
    Property Rel
    '''   
    def rel(self, rel):
        self.__dict__['rel'] = rel
        
    '''
    Property Return Keys
    '''   
    def returnKeys(self, return_keys):
        self.__dict__['returnKeys'] = return_keys
        
    '''
    Property Uri
    '''   
    def uri(self, uri):
        self.__dict__['uri'] = uri

    '''
    Property Key
    '''   
    def keys(self, keys):
        self.__dict__['keys'] = keys

    '''
    Property Href
    '''   
    def href(self, href):
        self.__dict__['href'] = href
