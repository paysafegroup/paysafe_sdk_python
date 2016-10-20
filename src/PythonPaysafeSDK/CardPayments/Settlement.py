'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK import CardPayments
from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK.common.Error import Error
from PythonPaysafeSDK.common.Link import Link


class Settlement(DomainObject):
    '''
    classdocs
    '''

    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['error'] = self.error
        handler['acquirerResponse'] = self.acquirerResponse
        handler['links'] = self.links
        handler['authorization'] = self.authorization
        handler['settlements'] = self.settlements
        
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
    Property Available To Refund
    '''
    def availableToRefund(self, available_to_refund):
        self.__dict__['availableToRefund'] = available_to_refund
        
    '''
    Property Child Account Number
    '''
    def childAccountNum(self, child_account_no):
        self.__dict__['childAccountNum'] = child_account_no

    '''
    Property Txn Time
    '''
    def txnTime(self, txn_time):
        self.__dict__['txnTime'] = txn_time

    '''
    Property Error
    @param: Error Object
    '''
    def error(self, error):
        e = Error(error)
        self.__dict__['error'] = e

    '''
    Property Dup Check
    '''
    def dupCheck(self, dup_check):
        self.__dict__['dupCheck'] = dup_check

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
        if isinstance(acquirer_response, 
                      CardPayments.AcquirerResponse.AcquirerResponse):
            self.__dict__['acquirerResponse'] = acquirer_response
        else:
            ar = CardPayments.AcquirerResponse.AcquirerResponse(
                                                acquirer_response)
            self.__dict__['acquirerResponse'] = ar
    
    '''
    Property Link
    @parma: Link Object, List of Link Objects
    '''
    def links(self, links):
        if isinstance(links, Link):
            self.__dict__['links'] = links
        else:
            for count in range(0, links.__len__()):
                l = Link(links[count])
                self.__dict__.setdefault('links', []).append(l)
    
    '''
    Property Authorization
    @param: Authorization Object
    '''
    def authorization(self, authorization):
        if isinstance(authorization, CardPayments.Authorization.Authorization):
            self.__dict__['authorization'] = authorization
        else:
            a = CardPayments.Authorization.Authorization(authorization)
            self.__dict__['authorization'] = a
            
    '''
    Property Settlements
    '''
    def settlements(self, settlements):    
        if isinstance(settlements, Settlement):
            self.__dict__['settlements'] = settlements
        else:
            for count in range(0, settlements.__len__()):
                ec = Settlement(settlements[count])
                self.__dict__.setdefault('settlements', []).append(ec)
