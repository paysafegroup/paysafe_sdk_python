'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK import CardPayments
from PythonPaysafeSDK import common
from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK.common.Error import Error


class Refund(DomainObject):
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
        handler['settlements'] = self.settlements
        handler['links'] = self.links
        handler['refunds'] = self.refunds
        
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
    Property Account Number
    '''
    def accountNum(self, account_num):
        self.__dict__['accountNum'] = account_num

    '''
    Property Dup Check
    '''
    def dupCheck(self, dup_check):
        self.__dict__['dupCheck'] = dup_check

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
    Property Settlements
    @param: Settlement Object
    '''
    def settlements(self, settlements):
        if isinstance(settlements, CardPayments.Settlement.Settlement):
            self.__dict__['settlements'] = settlements
        else:
            a = CardPayments.Settlement.Settlement(settlements)
            self.__dict__['settlements'] = a
    
    '''
    Property Link
    @param: Link Object, List of Link Objects
    '''
    def links(self, links):
        if isinstance(links, common.Link.Link):
            self.__dict__['links'] = links
        else:
            for count in range(0, links.__len__()):
                l = common.Link.Link(links[count])
                self.__dict__.setdefault('links', []).append(l)

    '''
    Property Refunds
    '''
    def refunds(self, refunds):    
        if isinstance(refunds, Refund):
            self.__dict__['refunds'] = refunds
        else:
            for count in range(0, refunds.__len__()):
                ec = Refund(refunds[count])
                self.__dict__.setdefault('refunds', []).append(ec)