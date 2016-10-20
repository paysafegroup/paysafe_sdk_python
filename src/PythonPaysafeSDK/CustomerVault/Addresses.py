'''
Created on 04-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK import CustomerVault
from PythonPaysafeSDK import common
from PythonPaysafeSDK.common.DomainObject import DomainObject


class Address(DomainObject):
    '''
    classdocs
    '''
    
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['profile'] = self.profile
        handler['error'] = self.error
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass

    '''
    Property Id
    '''        
    def id(self, id_):
        self.__dict__['id'] = id_

    '''
    Property Status
    '''                
    def status(self, status):
        self.__dict__['status'] = status   

    '''
    Property Default Shipping Address Indicator
    '''                
    def defaultShippingAddressIndicator(self, 
                                        default_shipping_address_indicator):
        self.__dict__['defaultShippingAddressIndicator'] = \
                    default_shipping_address_indicator
    
    '''
    Property Nick Name
    '''        
    def nickName(self, nick_name):
        self.__dict__['nickName'] = nick_name

    '''
    Property Street
    '''                
    def street(self, street):
        self.__dict__['street'] = street
    
    '''
    Property Street2
    '''        
    def street2(self, street2):
        self.__dict__['street2'] = street2

    '''
    Property City
    '''        
    def city(self, city):
        self.__dict__['city'] = city

    '''
    Property Country
    '''        
    def country(self, country):
        self.__dict__['country'] = country
        
    '''
    Property State
    '''        
    def state(self, state):
        self.__dict__['state'] = state

    '''
    Property Zip
    '''        
    def zip(self, zip_):
        self.__dict__['zip'] = zip_

    '''
    Property Recipient Name
    '''        
    def recipientName(self, recipient_name):
        self.__dict__['recipientName'] = recipient_name
    
    '''
    Property Phone
    '''        
    def phone(self, phone):
        self.__dict__['phone'] = phone
        
    '''
    Property Profile
    @param: Profile Object
    '''        
    def profile(self, profile):
        p = CustomerVault.Profile.Profile(profile.__dict__)
        self.__dict__['profile'] = p

    '''
    Property Error
    @param: Error Object
    '''        
    def error(self, error):
        e = common.Error.Error(error)
        self.__dict__['error'] = e
