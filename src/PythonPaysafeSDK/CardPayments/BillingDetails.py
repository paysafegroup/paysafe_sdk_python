'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.common.DomainObject import DomainObject


class BillingDetails(DomainObject):
    '''
    classdocs
    '''

    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['street'] = self.street
        handler['street2'] = self.street2
        handler['city'] = self.city
        handler['state'] = self.state
        handler['country'] = self.country
        handler['zip'] = self.zip
        handler['phone'] = self.phone
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass

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
    Property State
    '''
    def state(self, state):
        self.__dict__['state'] = state
        
    '''
    Property Country
    '''
    def country(self, country):
        self.__dict__['country'] =  country
        
    '''
    Property Zip
    '''
    def zip(self, zip_):
        self.__dict__['zip'] = zip_
    
    '''
    Property Phone
    '''
    def phone(self, phone):
        self.__dict__['phone'] = phone
