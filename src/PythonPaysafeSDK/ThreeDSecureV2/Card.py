from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK.common.CardExpiry import CardExpiry
class Card(DomainObject):
    def __init__(self, obj):
        '''
        Constructor
        '''
        #Handler dictionary
        handler = dict()
        handler['paymentToken'] = self.paymentToken
        handler['holderName']=self.holderName
        handler['cardNum']=self.cardNum
        handler['cardExpiry']=self.cardExpiry

        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
    '''
    Property paymentToken
    '''
    def paymentToken(self,paymentToken):
        self.__dict__['paymentToken'] = paymentToken

    '''
    Property holderName
    '''
    def holderName(self,holderName):
        self.__dict__['holderName'] = holderName

    '''
    Property cardNum
    '''
    def cardNum(self,cardNum):
        self.__dict__['cardNum'] = cardNum

    '''
    Property cardBin
    '''
    def cardBin(self,cardBin):
        self.__dict__['cardBin'] = cardBin

    '''
    Property cardExpiry
    '''
    def cardExpiry(self,cardExpiry):
        if isinstance(cardExpiry,CardExpiry):
            self.__dict__['cardExpiry'] = cardExpiry
        else:
            ce=CardExpiry(cardExpiry)
            self.__dict__['cardExpiry']=ce

    '''
    Property type
    '''
    def type(self,type):
        self.__dict__['type'] = type

    '''
    Property lastDigits
    '''
    def lastDigits(self,lastDigits):
        self.__dict__['lastDigits'] = lastDigits
