'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.common.DomainObject import DomainObject


class VisaAdditionalAuthData(DomainObject):
    '''
    classdocs
    '''
    
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['dateOfBirth'] = self.dateOfBirth
        handler['recipientZip'] = self.recipientZip
        handler['recipientLastName'] = self.recipientLastName
        handler['recipientAccountNumber'] = self.recipientAccountNumber
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass        
            
    '''
    Property Date Of Birth
    '''
    def dateOfBirth(self, date_of_birth):
        self.__dict__['dateOfBirth'] = date_of_birth

    '''
    Property Recipient Zip
    '''
    def recipientZip(self, recipient_zip):
        self.__dict__['recipientZip'] = recipient_zip

    '''
    Property Recipient Last Name
    '''
    def recipientLastName(self, recipient_last_name):
        self.__dict__['recipientLastName'] = recipient_last_name

    '''
    Property Recipient Account Number
    '''
    def recipientAccountNumber(self, recipient_account_no):
        self.__dict__['recipientAccountNumber'] = recipient_account_no
