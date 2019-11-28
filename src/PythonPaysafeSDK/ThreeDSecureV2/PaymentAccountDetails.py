from PythonPaysafeSDK.common.DomainObject import DomainObject
class PaymentAccountDetails(DomainObject):
    def __init__(self, obj):
        '''
        Constructor
        '''
        #Handler dictionary
        handler = dict()
        handler['createdDate'] = self.createdDate
        handler['createdRange']=self.createdRange
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
    '''
    Property createdDate
    '''
    def createdDate(self,createdDate):
        self.__dict__['createdDate'] = createdDate

    '''
    Property createdRange
    '''
    def createdRange(self,createdRange):
        self.__dict__['createdRange'] = createdRange

    