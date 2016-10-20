'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.common.DomainObject import DomainObject


class MasterPass(DomainObject):
    '''
    classdocs
    '''

    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['payPassWalletIndicator'] = self.payPassWalletIndicator
        handler['authenticationMethod'] = self.authenticationMethod
        handler['cardEnrollmentMethod'] = self.cardEnrollmentMethod
        handler['masterCardAssignedId'] = self.masterCardAssignedId
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
        
    '''
    Property Pay Pass Wallet Indicator
    '''
    def payPassWalletIndicator(self, pay_pass_wallet_indicator):
        self.__dict__['payPassWalletIndicator'] = pay_pass_wallet_indicator

    '''
    Property Authentication Method
    '''
    def authenticationMethod(self, authentication_metohd):
        self.__dict__['authenticationMethod'] = authentication_metohd
        
    '''
    Property Card Enrollment Method
    '''
    def cardEnrollmentMethod(self, card_enrollment_method):
        self.__dict__['cardEnrollmentMethod'] = card_enrollment_method
        
    '''
    Property Master Card Assigned Id
    '''
    def masterCardAssignedId(self, master_card_assigned_id):
        self.__dict__['masterCardAssignedId'] = master_card_assigned_id
