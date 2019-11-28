from PythonPaysafeSDK.common.DomainObject import DomainObject
class ShippingDetailsUsage(DomainObject):
    '''
    classdocs
    '''
    def __init__(self, obj):
        '''
        Constructor
        '''
        #Handler dictionary
        handler = dict()
        handler['initialUsageDate'] = self.initialUsageDate
        handler['initialUsageRange'] = self.initialUsageRange
        handler['cardHolderNameMatch']=self.cardHolderNameMatch
        
        if obj is not None:
            self.setProperties(obj,handler=handler)
        else:
            pass
    '''
    Property initialUsageDate
    '''
    def initialUsageDate(self,initialUsageDate):
        self.__dict__['initialUsageDate'] = initialUsageDate

    '''
    Property initialUsageRange
    '''
    def initialUsageRange(self,initialUsageRange):
        self.__dict__['initialUsageRange'] = initialUsageRange

    '''
    Property cardHolderNameMatch
    '''
    def cardHolderNameMatch(self,cardHolderNameMatch):
        self.__dict__['cardHolderNameMatch'] = cardHolderNameMatch