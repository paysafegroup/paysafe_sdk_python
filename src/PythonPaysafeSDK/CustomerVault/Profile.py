'''
Created on 04-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.CustomerVault.ACHBankAccount import ACHBankAccount
from PythonPaysafeSDK.CustomerVault.Addresses import Address
from PythonPaysafeSDK.CustomerVault.BACSBankAccount import BACSBankAccount
from PythonPaysafeSDK.CustomerVault.Card import Card
from PythonPaysafeSDK.CustomerVault.DateOfBirth import DateOfBirth
from PythonPaysafeSDK.CustomerVault.EFTBankAccount import EFTBankAccount
from PythonPaysafeSDK.CustomerVault.SEPABankAccount import SEPABankAccount
from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK.common.Error import Error
from PythonPaysafeSDK.common.Link import Link


class Profile(DomainObject):
    
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['dateOfBirth'] = self.dateOfBirth
        handler['addresses'] = self.addresses
        handler['cards'] = self.cards
        handler['card'] = self.card
        handler['error'] = self.error
        handler['links'] = self.links
        handler['achBankAccounts']= self.achBankAccounts
        handler['bacsBankAccounts'] = self.bacsBankAccounts
        handler['eftBankAccounts'] = self.eftBankAccounts
        handler['sepaBankAccounts'] = self.sepaBankAccounts
        
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
    Property Status
    '''        
    def status(self, status):
        self.__dict__['status'] = status
        
    '''
    Property Merchant Customer Id
    '''        
    def merchantCustomerId(self, merchant_customer_id):
        self.__dict__['merchantCustomerId'] = merchant_customer_id
    
    '''
    Property Locale
    '''        
    def locale(self, locale):
        self.__dict__['locale'] = locale
        
    '''
    Property First Name
    '''        
    def firstName(self, first_name):
        self.__dict__['firstName'] = first_name
        
    '''
    Property Middle Name
    '''        
    def middleName(self, middle_name):
        self.__dict__['middleName'] = middle_name
        
    '''
    Property Last Name
    '''        
    def lastName(self, last_name):
        self.__dict__['lastName'] = last_name
    
    '''
    Property Date  Of Birth
    @param: DateOfBirth Object, List of DateOfBirth Objects
    '''        
    def dateOfBirth(self, date_of_birth):
        if isinstance(date_of_birth, DateOfBirth):
            p = DateOfBirth(date_of_birth.__dict__)
            self.__dict__['dateOfBirth'] = p
        else:
            p = DateOfBirth(date_of_birth)
            self.__dict__['dateOfBirth'] = p
        
    '''
    Property Ip
    '''        
    def ip(self, ip):
        self.__dict__['ip'] = ip
        
    '''
    Property Gender
    '''        
    def gender(self, gender):
        self.__dict__['gender'] = gender
    
    '''
    Property Nationality
    '''        
    def nationality(self, nationality):
        self.__dict__['nationality'] = nationality
    
    '''
    Property Email
    '''        
    def email(self, email):
        self.__dict__['email'] = email
        
    '''
    Property Phone
    '''        
    def phone(self, phone):
        self.__dict__['phone'] = phone
        
    '''
    Property Cell Phone
    '''        
    def cellPhone(self, cell_phone):
        self.__dict__['cellPhone'] = cell_phone

    '''
    Property Payment Token
    '''        
    def paymentToken(self, payment_token):
        self.__dict__['paymentToken'] = payment_token
    
    '''
    Property Addresses
    @param: Addresses Object, List of Addresses Objects
    '''        
    def addresses(self, addresses):
        if isinstance(addresses, Address):
            addr = Address(addresses)
            self.__dict__['addresses'] = addr
        else:
            for count in range(0, addresses.__len__()):
                addr_obj = Address(addresses[count])
                self.__dict__.setdefault('addresses', []).append(addr_obj)    
    
    '''
    Property Card
    @param: Card Object
    '''        
    def card(self, card):
        p = Card(card.__dict__)
        self.__dict__['card'] = p
    
    '''
    Property Card
    @param: Card Object, List of Card Objects
    '''        
    def cards(self, cards):
        if isinstance(cards, Card):
            c = Card(cards)
            self.__dict__['cards'] = c
        else:
            for count in range(0, cards.__len__()):
                card_obj = Card(cards[count])
                self.__dict__.setdefault('cards', []).append(card_obj)

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
            l = Link(links)
            self.__dict__['links'] = l
        else:
            for count in range(0, links.__len__()):
                l = Link(links[count])
                self.__dict__.setdefault('links', []).append(l)
    
    '''
    Property achBankAccounts 
    @param: achBankAccounts  Object, List of achBankAccounts  Objects
    '''       
    def achBankAccounts(self, ach_bank_accounts ):
        if isinstance(ach_bank_accounts, ACHBankAccount):
            p = ACHBankAccount(ach_bank_accounts)
            self.__dict__['achBankAccounts'] = p
        else:
            for count in range(0, ach_bank_accounts.__len__()):
                p = ACHBankAccount(ach_bank_accounts[count])
                self.__dict__.setdefault('achBankAccounts', []).append(p)
                
    '''
    Property bacsBankAccounts
    @param: bacsbankaccount Object, List of bacsBankAccounts Objects
    '''        
    def bacsBankAccounts(self, bacs_bank_accounts):
        if isinstance(bacs_bank_accounts, BACSBankAccount):
            p = BACSBankAccount(bacs_bank_accounts)
            self.__dict__['bacsBankAccounts'] = p
        else:
            for count in range(0, bacs_bank_accounts.__len__()):
                p = BACSBankAccount(bacs_bank_accounts[count])
                self.__dict__.setdefault('bacsBankAccounts', []).append(p)
            
    '''
    Property eftBankAccounts 
    @param: eftbankaccount  Object, List of eftBankAccounts  Objects
    '''        
    def eftBankAccounts(self, eft_bank_accounts ):
        if isinstance(eft_bank_accounts, EFTBankAccount ):
            p = EFTBankAccount (eft_bank_accounts)
            self.__dict__['eftBankAccounts '] = p
        else:
            for count in range(0, eft_bank_accounts.__len__()):
                p = EFTBankAccount(eft_bank_accounts[count])
                self.__dict__.setdefault('eftBankAccounts ', []).append(p)
              
    '''
    Property sepaBankAccounts
    @param: sepabankaccount Object, List of sepaBankAccounts  Objects
    '''        
    def sepaBankAccounts(self, sepa_bank_accounts ):
        if isinstance(sepa_bank_accounts, SEPABankAccount ):
            p = SEPABankAccount (sepa_bank_accounts)
            self.__dict__['sepaBankAccounts '] = p
        else:
            for count in range(0, sepa_bank_accounts.__len__()):
                p = SEPABankAccount(sepa_bank_accounts[count])
                self.__dict__.setdefault('sepaBankAccounts ', []).append(p)