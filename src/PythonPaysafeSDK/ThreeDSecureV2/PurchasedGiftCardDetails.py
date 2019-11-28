from PythonPaysafeSDK.common.DomainObject import DomainObject
class PurchasedGiftCardDetails(DomainObject):
    def __init__(self,obj):
        '''
        Constructor
        '''
        #Handler dictionary
        handler = dict()
        handler['amount'] = self.amount
        handler['count']=self.count
        handler['currency']=self.currency
      
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
    '''
    Property amount
    '''
    def amount(self,amount):
        self.__dict__['amount'] = amount

    '''
    Property count
    '''
    def count(self,count):
        self.__dict__['count'] = count

    '''
    Property currency
    '''
    def currency(self,currency):
        self.__dict__['currency'] = currency