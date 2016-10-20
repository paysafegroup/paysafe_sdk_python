'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK import CustomerVault
from PythonPaysafeSDK import common
from PythonPaysafeSDK.CardPayments.CardExpiry import CardExpiry
from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK.common.Link import Link


class Card(DomainObject):
    '''
    classdocs
    '''

    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['cardExpiry'] = self.cardExpiry
        handler['profile'] = self.profile
        handler['error'] = self.error
        handler['links'] = self.links        
        handler['brand'] = self.brand
        handler['country'] = self.country
        handler['expiry'] = self.expiry
        handler['threeDEnrolment'] = self.threeDEnrolment
        
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
    Property Nick Name
    '''
    def nickName(self, nick_name):
        self.__dict__['nickName'] = nick_name
        
    '''
    Property Merchant Reference Number
    '''
    def merchantRefNum(self, merchant_ref_num):
        self.__dict__['merchantRefNum'] = merchant_ref_num
        
    '''
    Property Holder Name
    '''
    def holderName(self, holder_name):
        self.__dict__['holderName'] = holder_name

    '''
    Property Card Number
    '''
    def cardNum(self, card_num):
        self.__dict__['cardNum'] = card_num
        
    '''
    Property Card Bin
    '''
    def cardBin(self, card_bin):
        self.__dict__['cardBin'] = card_bin
        
    '''
    Property Last Digits
    '''
    def lastDigits(self, last_digits):
        self.__dict__['lastDigits'] = last_digits
        
    '''
    Property Card Expiry
    @param: CardExpiry Object
    '''
    def cardExpiry(self, card_expiry):
        if isinstance(card_expiry, CardExpiry):
            self.__dict__['cardExpiry'] = card_expiry
        else:
            ce = CardExpiry(card_expiry)
            self.__dict__['cardExpiry'] = ce
            
    '''
    Property Card Type
    '''
    def cardType(self, card_type):
        self.__dict__['cardType'] = card_type
      
    '''
    Property Billing  Address Id
    '''
    def billingAddressId(self, billing_address_id):
        self.__dict__['billingAddressId'] = billing_address_id
        
    '''
    Property Default Card Indicator
    '''
    def defaultCardIndicator(self, default_card_indicator):
        self.__dict__['defaultCardIndicator'] = default_card_indicator
                            
    '''
    Property Payment Token
    '''
    def paymentToken(self, payment_token):
        self.__dict__['paymentToken'] = payment_token
               
    '''
    Property Type
    '''
    def type(self, type_):
        self.__dict__['type'] = type_
    
    '''
    Property Cvv
    '''
    def cvv(self, cvv):
        self.__dict__['cvv'] = cvv
        
    '''
    Property Track1
    '''
    def track1(self, track_1):
        self.__dict__['track1'] = track_1 
        
    '''
    Property Track2
    '''
    def track2(self, track_2):
        self.__dict__['track2'] = track_2   
        
    '''
    Property Profile
    @parma: Profile Object
    '''
    def profile(self, profile):
        if isinstance(profile, CustomerVault.Profile.Profile):
            self.__dict__['profile'] = profile
        else:
            p = CustomerVault.Profile.Profile(profile)
            self.__dict__['profile'] = p
    
    '''
    Property Error
    @param: Error Object
    '''
    def error(self, error):
        e = common.Error.Error(error)
        self.__dict__['error'] = e
    
    '''
    Property Status
    '''
    def status(self, status):
        self.__dict__['status'] = status
        
    '''
    Property Link
    @param: Link Object, List of Link Objects
    '''
    def links(self, links):
        if isinstance(links, Link):
            l = Link(links)
            self.__dict__['links'] = l
        else:
            for count in range(0, links.__len__()):
                l = Link(links[count])
                self.__dict__.setdefault('links', []).append(l)
   
    '''
    Property Brand
    '''
    def brand(self, brand_):
        self.__dict__['brand'] = brand_
        
    '''
    Property Country
    '''
    def country(self, country_):
        self.__dict__['country'] = country_
        
    '''
    Property Expiry
    '''
    def expiry(self, expiry_):
        self.__dict__['expiry'] = expiry_
        
    '''
    Property ThreeDEnrolment
    '''
    def threeDEnrolment(self, threeDEnrolment_):
        self.__dict__['threeDEnrolment'] = threeDEnrolment_
