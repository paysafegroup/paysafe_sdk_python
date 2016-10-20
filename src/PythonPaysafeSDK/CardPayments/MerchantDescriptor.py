'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.common.DomainObject import DomainObject


class MerchantDescriptor(DomainObject):
    '''
    classdocs
    '''

    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['dynamicDescriptor'] = self.dynamicDescriptor
        handler['phone'] = self.phone

        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
        
    '''
    Property Dynamic Descriptor
    '''
    def dynamicDescriptor(self, dynamic_descriptor):
        self.__dict__['dynamicDescriptor'] = dynamic_descriptor

    '''
    Property Phone
    '''
    def phone(self, phone):
        self.__dict__['phone'] = phone
