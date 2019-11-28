from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK.ThreeDSecureV2.PaymentAccountDetails import PaymentAccountDetails
from PythonPaysafeSDK.ThreeDSecureV2.ShippingDetailsUsage import ShippingDetailsUsage
from PythonPaysafeSDK.ThreeDSecureV2.UserLogin import UserLogin
from PythonPaysafeSDK.ThreeDSecureV2.PriorThreeDSAuthentication import PriorThreeDSAuthentication
from PythonPaysafeSDK.ThreeDSecureV2.TravelDetails import TravelDetails
class UserAccountDetails(DomainObject):
    '''
    classdocs
    '''
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['createdDate'] = self.createdDate
        handler['createdRange'] = self.createdRange
        handler['changedDate']=self.changedDate
        handler['changedRange']=self.changedRange
        handler['passwordChangedDate']=self.passwordChangedDate
        handler['passwordChangedRange']=self.passwordChangedRange
        handler['totalPurchasesSixMonthCount']=self.totalPurchasesSixMonthCount
        handler['addCardAttemptsForLastDay']=self.addCardAttemptsForLastDay
        handler['transactionCountForPreviousDay']=self.transactionCountForPreviousDay
        handler['transactionCountForPreviousYear']=self.transactionCountForPreviousYear
        handler['suspiciousAccountActivity']=self.suspiciousAccountActivity
        handler['shippingDetailsUsage']=self.shippingDetailsUsage
        handler['paymentAccountDetails']=self.paymentAccountDetails
        handler['userLogin']=self.userLogin
        handler['priorThreeDSAuthentication']=self.priorThreeDSAuthentication
        handler['travelDetails']=self.travelDetails
        
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

    '''
    Property changedRange
    '''
    def changedRange(self,changedRange):
        self.__dict__['changedRange'] = changedRange

    '''
    Property changedDate
    '''
    def changedDate(self,changedDate):
        self.__dict__['changedDate'] = changedDate

    '''
    Property passwordChangedDate
    '''
    def passwordChangedDate(self,passwordChangedDate):
        self.__dict__['passwordChangedDate'] = passwordChangedDate

    '''
    Property passwordChangedRange
    '''
    def passwordChangedRange(self,passwordChangedRange):
        self.__dict__['passwordChangedRange'] = passwordChangedRange

    '''
    Property totalPurchasesSixMonthCount
    '''
    def totalPurchasesSixMonthCount(self,totalPurchasesSixMonthCount):
        self.__dict__['totalPurchasesSixMonthCount'] = totalPurchasesSixMonthCount

    '''
    Property addCardAttemptsForLastDay
    '''
    def addCardAttemptsForLastDay(self,addCardAttemptsForLastDay):
        self.__dict__['addCardAttemptsForLastDay'] = addCardAttemptsForLastDay

    '''
    Property transactionCountForPreviousDay
    '''
    def transactionCountForPreviousDay(self,transactionCountForPreviousDay):
        self.__dict__['transactionCountForPreviousDay'] = transactionCountForPreviousDay

    '''
    Property transactionCountForPreviousYear
    '''
    def transactionCountForPreviousYear(self,transactionCountForPreviousYear):
        self.__dict__['transactionCountForPreviousYear'] = transactionCountForPreviousYear

    '''
    Property suspiciousAccountActivity
    '''
    def suspiciousAccountActivity(self,suspiciousAccountActivity):
        self.__dict__['suspiciousAccountActivity'] = suspiciousAccountActivity

    '''
    Property shippingDetailsUsage
    '''
    def shippingDetailsUsage(self,shippingDetailsUsage):
        if isinstance(shippingDetailsUsage,ShippingDetailsUsage):
            self.__dict__['shippingDetailsUsage'] = shippingDetailsUsage
        else:
            sd=ShippingDetailsUsage(shippingDetailsUsage)
            self.__dict__['shippingDetailsUsage']=sd


    '''
    Property paymentAccountDetails
    '''
    def paymentAccountDetails(self,paymentAccountDetails):
        if isinstance(paymentAccountDetails,PaymentAccountDetails):
            self.__dict__['paymentAccountDetails'] = paymentAccountDetails
        else:
            pd=PaymentAccountDetails(paymentAccountDetails)
            self.__dict__['paymentAccountDetails']=pd
    '''
    Property userLogin
    '''
    def userLogin(self,userLogin):
        if isinstance(userLogin,UserLogin):
            self.__dict__['userLogin'] = userLogin
        else:
            ul=UserLogin(userLogin)
            self.__dict__['userLogin']=ul
    '''
    Property priorThreeDSAuthentication
    '''
    def priorThreeDSAuthentication(self,priorThreeDSAuthentication):
        if isinstance(priorThreeDSAuthentication,PriorThreeDSAuthentication):
            self.__dict__['priorThreeDSAuthentication'] = priorThreeDSAuthentication
        else:
            pa=PriorThreeDSAuthentication(priorThreeDSAuthentication)
            self.__dict__['priorThreeDSAuthentication']=pa

    '''
    Property travelDetails
    '''
    def travelDetails(self,travelDetails):
        if isinstance(travelDetails,TravelDetails):
            self.__dict__['travelDetails'] = travelDetails
        else:
            td=TravelDetails(travelDetails)
            self.__dict__['travelDetails']=td
