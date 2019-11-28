from PythonPaysafeSDK.common.DomainObject import DomainObject
class ElectronicDelivery(DomainObject):
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['email'] = self.email
        handler['isElectronicDelivery']=self.isElectronicDelivery

        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
    '''
    Property email
    '''
    def email(self,email):
        self.__dict__['email'] = email

    '''
    Property isElectronicDelivery
    '''
    def isElectronicDelivery(self,isElectronicDelivery):
        self.__dict__['isElectronicDelivery'] = isElectronicDelivery