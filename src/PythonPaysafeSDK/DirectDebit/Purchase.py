'''
Created on 11-Apr-2016

@author: Murali.Mohan
'''
from PythonPaysafeSDK.CardPayments.BillingDetails import BillingDetails
from PythonPaysafeSDK.CustomerVault.ACHBankAccount import ACHBankAccount
from PythonPaysafeSDK.CustomerVault.BACSBankAccount import BACSBankAccount
from PythonPaysafeSDK.CustomerVault.EFTBankAccount import EFTBankAccount
from PythonPaysafeSDK.CustomerVault.Profile import Profile
from PythonPaysafeSDK.CustomerVault.SEPABankAccount import SEPABankAccount
from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK.common.Error import Error
from PythonPaysafeSDK.common.Link import Link


class Purchase(DomainObject):

    def __init__(self,obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['profile'] = self.profile
        handler['ach'] = self.ach
        handler['eft'] = self.eft
        handler['bacs'] = self.bacs
        handler['sepa'] = self.sepa
        handler['links'] = self.links
        handler['purchases'] = self.purchases
        handler['billingDetails'] = self.billingDetails
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
    def customerIp(self,customer_Ip):
        self.__dict__['customerIp'] = customer_Ip
        
    '''
    Property Dup Check
    '''    
    def dupCheck(self,dup_Check):
        self.__dict__['dupCheck'] = dup_Check
    
    '''
    Property Txn Time
    '''
    def txnTime(self,txn_Time):
        self.__dict__['txnTime'] = txn_Time
        
    '''
    Property Currency Code
    '''
    def currencyCode(self,currency_Code):
        self.__dict__['currencyCode'] = currency_Code

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
            self.__dict__['ach'] = p
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
    Property sepa
    @param: sepa Object, List of sepa Objects
    '''        
    def sepa(self, sepa_bank_account):
        if isinstance(sepa_bank_account, SEPABankAccount):
            p = SEPABankAccount(sepa_bank_account.__dict__)
            self.__dict__['sepa'] = p
        else:
            p = SEPABankAccount(sepa_bank_account)
            self.__dict__['sepa'] = p        
       
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
    Property Purchases
    '''
    def purchases(self, purchases):
        if isinstance(purchases, Purchase):
            p = Purchase(purchases)
            self.__dict__['purchases'] = p
        else:
            for count in range(0, purchases.__len__()):
                p = Purchase(purchases[count])
                self.__dict__.setdefault('purchases', []).append(p)
    
    '''
    Property Error
    @param: Error Object
    '''        
    def error(self, error):
        e = Error(error)
        self.__dict__['error'] = e
    
