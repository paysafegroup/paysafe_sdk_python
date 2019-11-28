from PythonPaysafeSDK.common.DomainObject import DomainObject
class BillingCycle(DomainObject):
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['endDate'] = self.endDate
        handler['frequency']=self.frequency

        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass

    '''
    Property endDate
    '''
    def endDate(self,endDate):
        self.__dict__['endDate'] = endDate

    '''
    Property frequency
    '''
    def frequency(self,frequency):
        self.__dict__['frequency'] = frequency

           

    