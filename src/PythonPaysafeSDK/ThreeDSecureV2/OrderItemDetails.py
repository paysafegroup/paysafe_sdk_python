from PythonPaysafeSDK.common.DomainObject import DomainObject
class OrderItemDetails(DomainObject):
    def __init__(self, obj):
        '''
        Constructor
        '''
        #Handler dictionary
        handler = dict()
        handler['preOrderItemAvailabilityDate'] = self.preOrderItemAvailabilityDate
        handler['preOrderPurchaseIndicator']=self.preOrderPurchaseIndicator
        handler['reorderItemsIndicator']=self.reorderItemsIndicator
        handler['shippingIndicator']=self.shippingIndicator

        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
    '''
    Property preOrderItemAvailabilityDate
    '''
    def preOrderItemAvailabilityDate(self,preOrderItemAvailabilityDate):
        self.__dict__['preOrderItemAvailabilityDate'] = preOrderItemAvailabilityDate

    '''
    Property preOrderPurchaseIndicator
    '''
    def preOrderPurchaseIndicator(self,preOrderPurchaseIndicator):
        self.__dict__['preOrderPurchaseIndicator'] = preOrderPurchaseIndicator

    '''
    Property reorderItemsIndicator
    '''
    def reorderItemsIndicator(self,reorderItemsIndicator):
        self.__dict__['reorderItemsIndicator'] = reorderItemsIndicator

    '''
    Property shippingIndicator
    '''
    def shippingIndicator(self,shippingIndicator):
        self.__dict__['shippingIndicator'] = shippingIndicator