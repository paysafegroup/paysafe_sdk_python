from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK import ThreeDSecureV2
from PythonPaysafeSDK.common.Error import Error
from PythonPaysafeSDK.ThreeDSecureV2.ElectronicDelivery import ElectronicDelivery
from PythonPaysafeSDK.ThreeDSecureV2.Card import Card
from PythonPaysafeSDK.ThreeDSecureV2.OrderItemDetails import OrderItemDetails
from PythonPaysafeSDK.ThreeDSecureV2.BillingCycle import BillingCycle
from PythonPaysafeSDK.ThreeDSecureV2.PurchasedGiftCardDetails import PurchasedGiftCardDetails
from PythonPaysafeSDK.ThreeDSecureV2.BrowserDetails import BrowserDetails
from PythonPaysafeSDK.ThreeDSecureV2.BillingDetails import BillingDetails
from PythonPaysafeSDK.ThreeDSecureV2.ShippingDetails import ShippingDetails
from PythonPaysafeSDK.ThreeDSecureV2.UserAccountDetails import UserAccountDetails
from PythonPaysafeSDK.ThreeDSecureV2.Profile import Profile

class Authentications(DomainObject):
    def __init__(self,obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['merchantRefNum'] = self.merchantRefNum
        handler['amount'] = self.amount
        handler['deviceFingerprintingId'] = self.deviceFingerprintingId
        handler['currency']=self.currency
        handler['card']=self.card
        handler['merchantUrl']=self.merchantUrl
        handler['transactionIntent']=self.transactionIntent
        handler['maxAuthorizationsForInstalmentPayment']=self.maxAuthorizationsForInstalmentPayment
        handler['authenticationPurpose']=self.authenticationPurpose
        handler['deviceChannel']=self.deviceChannel
        handler['messageCategory']=self.messageCategory
        handler['initialPurchaseTime']=self.initialPurchaseTime
        handler['requestorChallengePreference']=self.requestorChallengePreference
        handler['electronicDelivery']=self.electronicDelivery
        handler['orderItemDetails']=self.orderItemDetails
        handler['purchasedGiftCardDetails']=self.purchasedGiftCardDetails
        handler['billingCycle']=self.billingCycle
        handler['browserDetails']=self.browserDetails
        handler['userAccountDetails']=self.userAccountDetails
        handler['billingDetails']=self.billingDetails
        handler['shippingDetails']=self.shippingDetails
        handler['profile']=self.profile
        handler['mcc']=self.mcc
        handler['merchantName']=self.merchantName


        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
    '''
    Property Id
    '''
    def id(self,id):
        self.__dict__['id'] = id

    '''
    Property deviceFingerprintingId
    '''
    def deviceFingerprintingId(self,device_Fingerprinting_Id):
        self.__dict__['deviceFingerprintingId'] = device_Fingerprinting_Id

    '''
    Property merchantRefNum
    '''
    def merchantRefNum(self,merchant_Ref_Num):
        self.__dict__['merchantRefNum']=merchant_Ref_Num

    
    '''
    Property amount
    '''
    def amount(self,amount):
        self.__dict__['amount'] = amount

    '''
    Property currency
    '''
    def currency(self,currency):
        self.__dict__['currency'] = currency

    '''
    Property Card
    @param:  Card Object
    '''
    def card(self, card):
        if isinstance(card, Card):
            self.__dict__['card'] = card
        else:
            c = Card(card)
            self.__dict__['card'] = c
    '''
    Property merchantUrl
    '''
    def merchantUrl(self,merchantUrl):
        self.__dict__['merchantUrl'] = merchantUrl

    '''
    Property txnTime
    '''
    def txnTime(self,txnTime):
        self.__dict__['txnTime'] = txnTime

    '''
    Property error
    '''
    def error(self, error):
        e = Error(error)
        self.__dict__['error'] = e

    '''
    Property status
    '''
    def status(self,status):
        self.__dict__['status'] = status
  
 
    '''
    Property acsUrl
    '''
    def acsUrl(self,acsUrl):
        self.__dict__['acsUrl'] = acsUrl

    
    '''
    Property payload
    '''
    def payload(self,payload):
        self.__dict__['payload'] = payload

    '''
    Property threeDEnrollment
    '''
    def threeDEnrollment(self,threeDEnrollment):
        self.__dict__['threeDEnrollment'] = threeDEnrollment

    '''
    Property threeDResult
    '''
    def threeDResult(self,threeDResult):
        self.__dict__['threeDResult'] = threeDResult

    '''
    Property threeDSecureVersion
    '''
    def threeDSecureVersion(self,threeDSecureVersion):
        self.__dict__['threeDSecureVersion'] = threeDSecureVersion

    '''
    Property directoryServerTransactionId
    '''
    def directoryServerTransactionId(self,directoryServerTransactionId):
        self.__dict__['directoryServerTransactionId'] = directoryServerTransactionId
    
    '''
    Property eci
    '''
    def eci(self,eci):
        self.__dict__['eci'] = eci

    '''
    Property cavv
    '''
    def cavv(self,cavv):
        self.__dict__['cavv'] = cavv

    '''
    Property xid
    '''
    def xid(self,xid):
        self.__dict__['xid'] = xid

    '''
    Property sdkChallengePayload
    '''
    def sdkChallengePayload(self,sdkChallengePayload):
        self.__dict__['sdkChallengePayload'] = sdkChallengePayload

    '''
    Property transactionIntent

    '''
    def transactionIntent(self,transactionIntent):
        self.__dict__['transactionIntent'] = transactionIntent
    '''
    Property maxAuthorizationsForInstalmentPayment
    '''
    def maxAuthorizationsForInstalmentPayment(self,maxAuthorizationsForInstalmentPayment):
        self.__dict__['maxAuthorizationsForInstalmentPayment'] = maxAuthorizationsForInstalmentPayment

    '''
    Property authenticationPurpose
    '''
    def authenticationPurpose(self,authenticationPurpose):
        self.__dict__['authenticationPurpose'] = authenticationPurpose

    '''
    Property deviceChannel
    '''
    def deviceChannel(self,deviceChannel):
        self.__dict__['deviceChannel'] = deviceChannel

    '''
    Property messageCategory
    '''
    def messageCategory(self,messageCategory):
        self.__dict__['messageCategory'] = messageCategory


    '''
    Property initialPurchaseTime
    '''
    def initialPurchaseTime(self,initialPurchaseTime):
        self.__dict__['initialPurchaseTime'] = initialPurchaseTime

    '''
    Property requestorChallengePreference
    '''
    def requestorChallengePreference(self,requestorChallengePreference):
        self.__dict__['requestorChallengePreference'] = requestorChallengePreference

    '''
    Property electronicDelivery
    '''
    def electronicDelivery(self,electronicDelivery):
        if isinstance(electronicDelivery, ElectronicDelivery):
            self.__dict__['electronicDelivery'] = electronicDelivery
        else:
            ed = ElectronicDelivery(electronicDelivery)
            self.__dict__['electronicDelivery'] = ed
    '''
    Property orderItemDetails
    '''
    def orderItemDetails(self,orderItemDetails):
        if isinstance(orderItemDetails,OrderItemDetails):
            self.__dict__['orderItemDetails'] = orderItemDetails
        else:
            od=OrderItemDetails(orderItemDetails)
            self.__dict__['orderItemDetails']=od
    '''
    Property purchasedGiftCardDetails
    '''
    def purchasedGiftCardDetails(self,purchasedGiftCardDetails):
        if isinstance(purchasedGiftCardDetails,PurchasedGiftCardDetails):
            self.__dict__['purchasedGiftCardDetails']=purchasedGiftCardDetails
        else:
            pd=PurchasedGiftCardDetails(purchasedGiftCardDetails)
            self.__dict__['purchasedGiftCardDetails'] = pd

    '''
    Property billingCycle
    '''
    def billingCycle(self,billingCycle):
        if isinstance(billingCycle,BillingCycle):
            self.__dict__['billingCycle'] =billingCycle
        else:
            bc=BillingCycle(billingCycle)
            self.__dict__['billingCycle']=bc
    '''
    Property browserDetails
    '''
    def browserDetails(self,browserDetails):
        if isinstance(browserDetails,BrowserDetails):
            self.__dict__['browserDetails'] = browserDetails
        else:
            bd=BrowserDetails(browserDetails)
            self.__dict__['browserDetails']=bd


    '''
    Property userAccountDetails
    '''
    def userAccountDetails(self,userAccountDetails):
        if isinstance(userAccountDetails,UserAccountDetails):
            self.__dict__['userAccountDetails'] = userAccountDetails
        else:
            ud=UserAccountDetails(userAccountDetails)
            self.__dict__['userAccountDetails']=ud

    '''
    Property billingDetails
    '''
    def billingDetails(self,billingDetails):
        if isinstance(billingDetails,BillingDetails):
            self.__dict__['billingDetails'] = billingDetails
        else:
            bd=BillingDetails(billingDetails)
            self.__dict__['billingDetails']=bd


    '''
    Property shippingDetails
    '''
    def shippingDetails(self,shippingDetails):
        if isinstance(shippingDetails,ShippingDetails):
            self.__dict__['shippingDetails'] = shippingDetails
        else:
            sd=ShippingDetails(shippingDetails)
            self.__dict__['shippingDetails']=sd

    '''
    Property profile
    '''
    def profile(self,profile):
        if isinstance(profile,Profile):
            self.__dict__['profile']=profile
        else:
            p=Profile(profile)
            self.__dict__['profile']=p


    '''
    Property signatureStatus
    '''
    def signatureStatus(self,signatureStatus):
        self.__dict__['signatureStatus'] = signatureStatus

    '''
    Property threeDSecureServerTransactionId
    '''
    def threeDSecureServerTransactionId(self,threeDSecureServerTransactionId):
        self.__dict__['threeDSecureServerTransactionId'] = threeDSecureServerTransactionId

    '''
    Property mcc
    '''
    def mcc(self,mcc):
        self.__dict__['mcc'] = mcc

    '''
    Property merchantName
    '''
    def merchantName(self,merchantName):
        self.__dict__['merchantName'] = merchantName
