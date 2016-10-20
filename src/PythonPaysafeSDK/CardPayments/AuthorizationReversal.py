'''
Created on 17-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK import CardPayments
from PythonPaysafeSDK import common
from PythonPaysafeSDK.common.DomainObject import DomainObject


class AuthorizationReversal(DomainObject):
    '''
    classdocs
    '''

    def __init__(self,obj):
        '''
        Constructor
        '''
        handler = dict()
        handler['error'] = self.error
        handler['acquirerResponse'] = self.acquirerResponse
        handler['links'] = self.links
        handler['authorization'] = self.authorization
        handler['voidAuths'] = self.voidAuths
        
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
    def merchantRefNum(self , merchantRefNum):
        self.__dict__['merchantRefNum'] = merchantRefNum
        
    '''
    Property Amount
    '''
    def amount(self, amount):
        self.__dict__['amount'] = amount
        
    '''
    Property Child Account Number
    '''
    def childAccountNum(self, childAccountNum):
        self.__dict__['childAccountNum'] = childAccountNum
        
    '''
    Property Dup Check
    '''
    def dupCheck(self, dup_check):
        self.__dict__['dupCheck'] = dup_check
    
    '''
    Property Txn Time
    '''
    def txnTime(self, txnTime):
        self.__dict__['txnTime'] = txnTime
    
    '''
    Property Error
    @parma: Error Object
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
    Property Risk Reason Code
    '''
    def riskReasonCode(self, riskReasonCode):
        self.__dict__['riskReasonCode'] = riskReasonCode
        
    '''
    Property Acqurier Response
    @param: AcqurierResponse Object
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
        if isinstance(links, common.Link.Link):
            self.__dict__['links'] = links
        else:
            for count in range(0, links.__len__()):
                l = common.Link.Link(links[count])
                self.__dict__.setdefault('links', []).append(l)
    
    '''
    Property Void Auth
    '''
    def voidAuths(self, void_auths):    
        if isinstance(void_auths, AuthorizationReversal):
            self.__dict__['voidAuths'] = void_auths
        else:
            for count in range(0, void_auths.__len__()):
                ec = AuthorizationReversal(void_auths[count])
                self.__dict__.setdefault('voidAuths', []).append(ec)
    
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
