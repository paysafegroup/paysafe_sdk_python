'''
Created on 15-Apr-2016

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.CardPayments.BillingDetails import BillingDetails
from PythonPaysafeSDK.CardPayments.ShippingDetails import ShippingDetails
from PythonPaysafeSDK.CustomerVault.ACHBankAccount import ACHBankAccount
from PythonPaysafeSDK.CustomerVault.BACSBankAccount import BACSBankAccount
from PythonPaysafeSDK.CustomerVault.EFTBankAccount import EFTBankAccount
from PythonPaysafeSDK.CustomerVault.Profile import Profile
from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK.common.Error import Error
from PythonPaysafeSDK.common.Link import Link


class StandaloneCredits(DomainObject):
    
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['profile'] = self.profile
        handler['ach'] = self.ach
        handler['eft'] = self.eft
        handler['bacs'] = self.bacs
        handler['billingDetails'] = self.billingDetails
        handler['shippingDetails'] = self.shippingDetails
        handler['links'] = self.links
        handler['standaloneCredits'] = self.standaloneCredits
        handler['error'] = self.error

        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
        
    '''
    Property Id
    '''
    def id(self,id_):
        self.__dict__['id'] = id_
    
    '''
    Property Merchant Reference Number
    '''
    def merchantRefNum(self,merchant_ref_num):
        self.__dict__['merchantRefNum']= merchant_ref_num
        
    '''
    Property Amount
    '''
    def amount(self,amount):
        self.__dict__['amount'] = amount

    '''
    Property Customer Ip
    '''    
    def customerIp(self,customer_ip):
        self.__dict__['customerIp'] = customer_ip
        
    '''
    Property Dup Check
    '''    
    def dupCheck(self,dup_check):
        self.__dict__['dupCheck'] = dup_check
    
    '''
    Property Txn Time
    '''
    def txnTime(self,txn_time):
        self.__dict__['txnTime'] = txn_time
        
    '''
    Property Currency Code
    '''
    def currencyCode(self,currency_code):
        self.__dict__['currencyCode'] = currency_code

    '''
    Property Status
    '''
    def status(self,status):
        self.__dict__['status'] = status
        
    '''
    Property ach
    @param: ach Object, List of ach Objects
    ''' 
    def ach(self, ach_bank_account):
        if isinstance(ach_bank_account, ACHBankAccount):
            p = ACHBankAccount(ach_bank_account.__dict__)
            self.__setattr__('ach', p)
        else:
            p = ACHBankAccount(ach_bank_account)
            self.__dict__['ach'] = p
            
    '''
    Property eft
    @param: eft Object, List of eft Objects
    '''        
    def eft(self, eft_bank_account):
        if isinstance(eft_bank_account, EFTBankAccount):
            p = EFTBankAccount(eft_bank_account.__dict__)
            self.__dict__['eft'] = p
        else:
            p = EFTBankAccount(eft_bank_account)
            self.__dict__['eft'] = p
            
    '''
    Property bacs
    @param: bacs Object, List of bacs Objects
    '''        
    def bacs(self, bacs_bank_account):
        if isinstance(bacs_bank_account, BACSBankAccount):
            p = BACSBankAccount(bacs_bank_account.__dict__)
            self.__dict__['bacs'] = p
        else:
            p = BACSBankAccount(bacs_bank_account)
            self.__dict__['bacs'] = p
               
    '''
    Property Profile
    @param: Profile Object
    '''        
    def profile(self, profile):
        if isinstance(profile, Profile):
            p = Profile(profile.__dict__)
            self.__dict__['profile'] = p
        else:
            p = Profile(profile)
            self.__dict__['profile'] = p
            
    '''
    Property billingDetails
    @param: BillingDetails Object
    '''        
    def billingDetails(self, billing_details):
        if isinstance(billing_details, BillingDetails):
            p = BillingDetails(billing_details.__dict__)
            self.__dict__['billingDetails'] = p
        else:
            p = BillingDetails(billing_details)
            self.__dict__['billingDetails'] = p
        
    '''
    Property shippingDetails
    @param: ShippingDetails Object
    '''        
    def shippingDetails(self, shipping_details):
        p = ShippingDetails(shipping_details.__dict__)
        self.__dict__['shippingDetails'] = p
                    
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
    Property standalonecredits
    '''
    def standaloneCredits(self, standalone_credits):
        if isinstance(standalone_credits, StandaloneCredits):
            p = StandaloneCredits(standalone_credits)
            self.__dict__['standaloneCredits'] = p
        else:
            for count in range(0, standalone_credits.__len__()):
                p = StandaloneCredits(standalone_credits[count])
                self.__dict__.setdefault('standaloneCredits', []).append(p)
    
    '''
    Property Error
    @param: Error Object
    '''        
    def error(self, error):
        e = Error(error)
        self.__dict__['error'] = e    