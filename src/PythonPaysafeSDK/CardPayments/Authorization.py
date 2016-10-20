'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.CardPayments.AccordD import AccordD
from PythonPaysafeSDK.CardPayments.AcquirerResponse import AcquirerResponse
from PythonPaysafeSDK.CardPayments.Authentication import Authentication
from PythonPaysafeSDK.CardPayments.BillingDetails import BillingDetails
from PythonPaysafeSDK.CardPayments.Card import Card
from PythonPaysafeSDK.CardPayments.MasterPass import MasterPass
from PythonPaysafeSDK.CardPayments.MerchantDescriptor import MerchantDescriptor
from PythonPaysafeSDK.CardPayments.Settlement import Settlement
from PythonPaysafeSDK.CardPayments.ShippingDetails import ShippingDetails
from PythonPaysafeSDK.CardPayments.VisaAdditionalAuthData import \
                            VisaAdditionalAuthData
from PythonPaysafeSDK.CustomerVault.Profile import Profile
from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK.common.Error import Error
from PythonPaysafeSDK.common.Link import Link


class Authorization(DomainObject):
    '''
    classdocs
    '''

    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['card'] = self.card
        handler['authentication'] = self.authentication
        handler['profile'] = self.profile
        handler['billingDetails'] = self.billingDetails
        handler['shippingDetails'] = self.shippingDetails
        handler['merchantDescriptor'] = self.merchantDescriptor
        handler['accordD'] = self.accordD
        handler['masterPass'] = self.masterPass
        handler['error'] = self.error
        handler['acquirerResponse'] = self.acquirerResponse
        handler['visaAdditionalAuthData'] = self.visaAdditionalAuthData
        handler['links'] = self.links
        handler['settlements'] = self.settlements
        handler['riskReasonCode'] = self.riskReasonCode
        handler['auths'] = self.auths
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass

    '''
    Property Id
    '''
    def id(self, id_):
        self.__dict__['id'] = id_
        
    '''
    Property Merchant Reference Number
    '''
    def merchantRefNum(self, merchant_ref_num):
        self.__dict__['merchantRefNum'] = merchant_ref_num
        
    '''
    Property Amount
    '''
    def amount(self, amount):
        self.__dict__['amount'] = amount
        
    '''
    Property Settle With Auth
    '''
    def settleWithAuth(self, settle_with_auth):
        self.__dict__['settleWithAuth'] = settle_with_auth
            
    '''
    Property Available To Settle
    '''
    def availableToSettle(self, available_to_settle):
        self.__dict__['availableToSettle'] = available_to_settle
        
    '''
    Property Child Account Number
    '''
    def childAccountNum(self, child_account_num):
        self.__dict__['childAccountNum'] = child_account_num
        
    '''
    Property Card
    @param:  Card Object
    '''
    def card(self, card):
        if isinstance(card, Card):
            self.__dict__['card'] = card
        else:
            p = Card(card)
            self.__dict__['card'] = p
    
    '''
    Property Authentication
    @param: Authentication Object
    '''
    def authentication(self, authentication):
        if isinstance(authentication, Authentication):
            self.__dict__['authentication'] = authentication
        else:
            a = Authentication(authentication)
            self.__dict__['authentication'] = a
        
    '''
    Property Auth Code
    '''
    def authCode(self, auth_code):
        self.__dict__['authCode'] =auth_code
        
    '''
    Property Profile
    @param: Profile Object
    '''
    def profile(self, profile):
        if isinstance(profile, Profile):
            self.__dict__['profile'] = profile
        else:
            p = Profile(profile)
            self.__dict__['profile'] = p
    
    '''
    Property Billing Details
    @param: BillingDetails Object
    '''
    def billingDetails(self, billing_details):
        if isinstance(billing_details, BillingDetails):
            self.__dict__['billingDetails'] = billing_details
        else:
            bd = BillingDetails(billing_details)
            self.__dict__['billingDetails'] = bd
    
    '''
    Property Shipping Details
    @param: ShippingDetails Object
    '''
    def shippingDetails(self, shipping_details):
        if isinstance(shipping_details, ShippingDetails):
            self.__dict__['shippingDetails'] = shipping_details
        else:
            sd =  ShippingDetails(shipping_details)
            self.__dict__['shippingDetails'] = sd
        
    '''
    Property Recurring
    '''
    def recurring(self, recurring):
        self.__dict__['recurring'] = recurring
            
    '''
    Property Customer Ip
    '''
    def customerIp(self, customer_ip):
        self.__dict__['customerIp'] = customer_ip
    
    '''
    Property Dup Check
    '''
    def dupCheck(self, dup_check):
        self.__dict__['dupCheck'] = dup_check
    
    '''
    Property Keywords
    '''
    def keywords(self, keywords):
        self.__dict__['keywords'] = keywords
        
    '''
    Property Merchant Descriptor
    @param: MerchantDescriptor Object
    '''
    def merchantDescriptor(self, merchant_descriptor):
        if isinstance(merchant_descriptor, MerchantDescriptor):
            self.__dict__['merchantDescriptor'] = merchant_descriptor
        else:
            md = MerchantDescriptor(merchant_descriptor)
            self.__dict__['merchantDescriptor'] = md
    
    '''
    Property AccordD
    @param: AccordD Object
    '''
    def accordD(self, accord_d):
        if isinstance(accord_d, AccordD):
            self.__dict__['accordD'] = accord_d
        else:
            a = AccordD(accord_d)
            self.__dict__['accordD'] = a
        
    '''
    Property Description
    '''
    def description(self, description):
        self.__dict__['description'] = description
        
    '''
    Property Master Pass
    @param: MasterPass Object
    '''
    def masterPass(self, master_pass):
        if isinstance(master_pass, MasterPass):
            self.__dict__['masterPass'] = master_pass
        else:
            mp = MasterPass(master_pass)
            self.__dict__['masterPass'] = mp
        
    '''
    Property Txn Time
    '''
    def txnTime(self, txn_time):
        self.__dict__['txnTime'] = txn_time
        
    '''
    Property Currency Code
    '''
    def currencyCode(self, currency_code):
        self.__dict__['currencyCode'] = currency_code
        
    '''
    Property Avs Response
    '''
    def avsResponse(self, avs_response):
        self.__dict__['avsResponse'] = avs_response
        
    '''
    Property Cvv verification
    '''
    def cvvVerification(self, cvv_verification):
        self.__dict__['cvvVerification'] = cvv_verification
        
    '''
    Property Error
    @param: Error Object
    '''
    def error(self, error):
        e = Error(error)
        self.__dict__['error'] = e
        
    '''
    Property Status
    '''
    def status(self, status):
        self.__dict__['status'] = status
        
    '''
    Property Risk Reason Code
    '''
    def riskReasonCode(self, risk_reason_code):
        self.__dict__['riskReasonCode'] = risk_reason_code
    
    '''
    Property Acquirer Response
    @param: AcquirerResponse Object
    '''
    def acquirerResponse(self, acquirer_response):
        if isinstance(acquirer_response, AcquirerResponse):
            self.__dict__['acquirerResponse'] = acquirer_response
        else:
            ar = AcquirerResponse(acquirer_response)
            self.__dict__['acquirerResponse'] = ar
        
    '''
    Property Visa Additional Auth Data
    @param: VisaAdditionalAuthData Object
    '''
    def visaAdditionalAuthData(self, visa_additional_auth_data):
        if isinstance(visa_additional_auth_data, VisaAdditionalAuthData):
            self.__dict__['visaAdditionalAuthData'] = visa_additional_auth_data
        else:
            visa = VisaAdditionalAuthData(visa_additional_auth_data)
            self.__dict__['visaAdditionalAuthData'] = visa
            
    '''
    Property Link
    @param: Link Object, List of Link Objects
    '''
    def links(self, links):
        if isinstance(links, Link):
            self.__dict__['links'] = links
        else:
            for count in range(0, links.__len__()):
                l = Link(links[count])
                self.__dict__.setdefault('links', []).append(l)
                
    '''
    Property Settlement
    @param: Settlement Object
    '''
    def settlements(self, settlements):
        if isinstance(settlements, Settlement):
            self.__dict__['settlements'] = settlements
        else:
            for count in range(0, settlements.__len__()):
                st = Settlement(settlements[count])
                self.__dict__.setdefault('settlements', []).append(st)
                
    '''
    Property auths
    '''
    def auths(self, auths):    
        if isinstance(auths, Authorization):
            self.__dict__['auths'] = auths
        else:
            for count in range(0, auths.__len__()):
                ec = Authorization(auths[count])
                self.__dict__.setdefault('auths', []).append(ec)
