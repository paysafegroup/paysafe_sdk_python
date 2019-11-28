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
        handler['shipMethod'] = self.shipMethod
        handler['street'] = self.street
        handler['street2']=self.street2
        handler['city'] = self.city
        handler['state'] = self.state
        handler['country'] = self.country
        handler['zip'] = self.zip
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
    '''
    Property shipMethod
    '''
    def shipMethod(self,shipMethod):
        self.__dict__['shipMethod'] = shipMethod

    '''
    Property street
    '''
    def street(self,street):
        self.__dict__['street'] = street

    '''
    Property street2
    '''
    def street2(self,street2):
        self.__dict__['street2'] = street2

    '''
    Property city
    '''
    def city(self,city):
        self.__dict__['city'] = city

    '''
    Property state
    '''
    def state(self,state):
        self.__dict__['state'] = state

    '''
    Property country
    '''
    def country(self,country):
        self.__dict__['country'] = country

    '''
    Property zip
    '''
    def zip(self,zip):
        self.__dict__['zip'] = zip
        

    