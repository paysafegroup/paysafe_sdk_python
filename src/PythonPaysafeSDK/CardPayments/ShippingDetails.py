'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.common.DomainObject import DomainObject


class ShippingDetails(DomainObject):
    '''
    classdocs
    '''
    def __init__(self, obj):
        '''
        Constructor
        '''
        
        # Handler dictionary
        handler = dict()        
        handler['carrier'] = self.carrier
        handler['shipMethod'] = self.shipMethod        
        handler['recipientName'] = self.recipientName
        handler['street'] = self.street
        handler['city'] = self.city
        handler['state'] = self.state
        handler['country'] = self.country
        handler['zip'] = self.zip
                       
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
        
    '''
    Property Carrier
    '''
    def carrier(self, carrier):
        self.__dict__['carrier'] = carrier        

    '''
    Property Ship Method
    '''
    def shipMethod(self, ship_method):
        self.__dict__['shipMethod'] = ship_method
            
    '''
    Property Recipient Name
    '''
    def recipientName(self, recipient_name):
        self.__dict__['recipientName'] = recipient_name
        
    '''
    Property Street
    '''
    def street(self, street):
        self.__dict__['street'] = street
                
    '''
    Property City
    '''
    def city(self, city):
        self.__dict__['city'] = city
        
    '''
    Property State
    '''
    def state(self, state):
        self.__dict__['state'] = state
                
    '''
    Property Country
    '''
    def country(self, country):
        self.__dict__['country'] = country
        
    '''
    Property Zip
    '''
    def zip(self, zip_):
        self.__dict__['zip'] = zip_
