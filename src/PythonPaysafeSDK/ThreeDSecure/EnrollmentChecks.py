'''
Created on 18-Apr-2016

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.CardPayments.Card import Card
from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK.common.Error import Error
from PythonPaysafeSDK.common.Link import Link


class EnrollmentChecks(DomainObject):
    
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['card'] = self.card
        handler['links'] = self.links
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
    Property Currency
    '''
    def currency(self, currency):
        self.__dict__['currency'] = currency
        
    '''
    Property Card
    @param:  Card Object
    '''
    def card(self, card):
        if isinstance(card, Card):
            self.__dict__['card'] = card
        else:
            p = Card(card)
            self.__dict__['card'] = p
    
    '''
    Property Customer Ip
    '''    
    def customerIp(self,customer_ip):
        self.__dict__['customerIp'] = customer_ip
        
    '''
    Property User Agent
    '''
    def userAgent(self, user_agent):
        self.__dict__['userAgent'] = user_agent
        
    '''
    Property Accept Header
    '''
    def acceptHeader(self, accept_header):
        self.__dict__['acceptHeader'] = accept_header
        
    '''
    Property Merchant Uri
    '''
    def merchantUrl(self, merchant_uri):
        self.__dict__['merchantUrl'] = merchant_uri
        
    '''
    Property Txn Time
    '''
    def txnTime(self, txn_time):
        self.__dict__['txnTime'] = txn_time
    
    '''
    Property status
    '''
    def status(self, status):
        self.__dict__['status'] = status
    
    '''
    Property ACS URL
    '''
    def acsURL(self, acs_url):
        self.__dict__['acsURL'] = acs_url
    
    '''
    Property paReq
    '''
    def paReq(self, paReq):
        self.__dict__['paReq'] = paReq
        
    '''
    Property eci
    '''
    def eci(self, eci):
        self.__dict__['eci'] = eci
        
    '''
    Property threeDEnrollment
    '''
    def threeDEnrollment(self, three_d_enrollment):
        self.__dict__['threeDEnrollment'] = three_d_enrollment

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
    Property Error
    @param: Error Object
    '''        
    def error(self, error):
        e = Error(error)
        self.__dict__['error'] = e    