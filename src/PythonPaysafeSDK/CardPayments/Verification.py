'''
Created on 10-Jun-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.CardPayments.AccordD import AccordD
from PythonPaysafeSDK.CardPayments.AcquirerResponse import AcquirerResponse
from PythonPaysafeSDK.CardPayments.Authentication import Authentication
from PythonPaysafeSDK.CardPayments.BillingDetails import BillingDetails
from PythonPaysafeSDK.CardPayments.Card import Card
from PythonPaysafeSDK.CardPayments.MasterPass import MasterPass
from PythonPaysafeSDK.CardPayments.MerchantDescriptor import MerchantDescriptor
from PythonPaysafeSDK.CardPayments.ShippingDetails import ShippingDetails
from PythonPaysafeSDK.CustomerVault.Profile import Profile
from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK.common.Error import Error
from PythonPaysafeSDK.common.Link import Link


class Verification(DomainObject):
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
        handler['profile'] = self.profile
        handler['authentication'] = self.authentication
        handler['accordD'] = self.accordD
        handler['billingDetails'] = self.billingDetails
        handler['shippingDetails'] = self.shippingDetails
        handler['merchantDescriptor'] = self.merchantDescriptor
        handler['masterPass'] = self.masterPass
        handler['error'] = self.error
        handler['acquirerResponse'] = self.acquirerResponse
        handler['links'] = self.links
        handler['riskReasonCode'] = self.riskReasonCode
        handler['verifications'] = self.verifications
        
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
    Property Child Account Number
    '''
    def childAccountNum(self, child_account_num):
        self.__dict__['childAccountNum'] = child_account_num

    '''
    Propert Card
    @param: Card Object
    '''
    def card(self, card):
        if isinstance(card, Card):
            self.__dict__['card'] = card
        else:
            p = Card(card)
            self.__dict__['card'] = p

    '''
    Property Auth Code
    '''
    def authCode(self, auth_code):
        self.__dict__['authCode'] = auth_code

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
            sd = ShippingDetails(shipping_details)
            self.__dict__['shippingDetails'] = sd

    '''
    Property Authentication Details
    @param: Authentication Object
    '''
    def authentication(self, authentication):
        if isinstance(authentication, Authentication):
            self.__dict__['authentication'] = authentication
        else:
            aa = Authentication(authentication)
            self.__dict__['authentication'] = aa

    '''
    Property AccordD Details
    @param: AccordD Object
    '''
    def accordD(self, accordD):
        if isinstance(accordD, AccordD):
            self.__dict__['accordD'] = accordD
        else:
            aa = AccordD(accordD)
            self.__dict__['accordD'] = aa

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
    Property Merchant Descriptor
    @param: MerchantDescriptor
    '''
    def merchantDescriptor(self, merchant_descriptor):
        if isinstance(merchant_descriptor, MerchantDescriptor):
            self.__dict__['merchantDescriptor'] = merchant_descriptor
        else:
            md = MerchantDescriptor(merchant_descriptor)
            self.__dict__['merchantDescriptor'] = md

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
    Property Transaction Time
    '''
    def txnTime(self, txn_time):
        self.__dict__['txnTime'] = txn_time

    '''
    Property Currency Code
    '''
    def currencyCode(self, currency_code):
        self.__dict__['currencyCode'] = currency_code

    '''
    Property AVS Response
    '''
    def avsResponse(self, avs_response):
        self.__dict__['avsResponse'] = avs_response

    '''
    Property Cvv Verification
    '''
    def cvvVerification(self, cvv_verification):
        self.__dict__['cvvVerification'] = cvv_verification

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
    Property Error
    @param: Error Object
    '''
    def error(self, error):
        e = Error(error)
        self.__dict__['error'] = e

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
    Property Verifications
    '''
    def verifications(self, verifications):    
        if isinstance(verifications, Verification):
            self.__dict__['verifications'] = verifications
        else:
            for count in range(0, verifications.__len__()):
                ec = Verification(verifications[count])
                self.__dict__.setdefault('verifications', []).append(ec)
                
