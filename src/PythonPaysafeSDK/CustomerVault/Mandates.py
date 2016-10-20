'''
Created on 01-Apr-2016

@author: Murali.Mohan
'''
from PythonPaysafeSDK import CustomerVault
from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK.common.Error import Error


class Mandates(DomainObject):
    
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['bacs'] = self.bacs
        handler['sepa'] = self.sepa
        handler['profile'] = self.profile
        handler['error'] = self.error
        
        
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
    Property Reference
    '''
    def reference(self, reference):
        self.__dict__['reference'] = reference
        
    '''
    Property Bank Account Id
    '''
    def bankAccountId(self, bank_account_id):
        self.__dict__['bankAccountId'] = bank_account_id
        
    '''
    Property Status
    '''
    def status(self, status):
        self.__dict__['status'] = status
        
    '''
    Property Payment Token
    '''
    def paymentToken(self, payment_token):
        self.__dict__['paymentToken'] = payment_token
        
    '''
    Property Status Change Date
    '''
    def statusChangeDate(self, status_change_date):
        self.__dict__['statusChangeDate'] = status_change_date
        
    '''
    Propert Status Reason Code
    '''
    def statusReasonCode(self, status_reason_code):
        self.__dict__['statusReasonCode'] = status_reason_code
        
    '''
    Propert Status Reason
    '''
    def statusReason(self, status_reason):
        self.__dict__['statusReason'] = status_reason

    '''
    Property bacs
    @param: BACSBankAccount Object
    '''
    def bacs(self, bacs):
        if isinstance(bacs, CustomerVault.BACSBankAccount.BACSBankAccount):
            e = CustomerVault.BACSBankAccount.BACSBankAccount(bacs.__dict__)
            self.__dict__['bacs'] = e
        else:
            p = CustomerVault.BACSBankAccount.BACSBankAccount(bacs)
            self.__dict__['bacs'] = p

    '''
    Property sepa
    @param: SEPABankAccount Object
    '''
    def sepa(self, sepa):
        if isinstance(sepa, CustomerVault.SEPABankAccount.SEPABankAccount):
            e = CustomerVault.SEPABankAccount.SEPABankAccount(sepa.__dict__)
            self.__dict__['sepa'] = e
        else:
            p = CustomerVault.SEPABankAccount.SEPABankAccount(sepa)
            self.__dict__['sepa'] = p
        
    '''
    Property Error
    @param: Error Object
    '''        
    def error(self, error):
        e = Error(error)
        self.__dict__['error'] = e
        
    '''
    Property Profile
    @param: Profile Object
    '''        
    def profile(self, profile):
        p = CustomerVault.Profile.Profile(profile.__dict__)
        self.__dict__['profile'] = p