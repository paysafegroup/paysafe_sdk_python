'''
Created on 18-Apr-2016

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.ThreeDSecure.EnrollmentChecks import EnrollmentChecks
from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK.common.Error import Error
from PythonPaysafeSDK.common.Link import Link


class Authentications(DomainObject):
    
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['error'] = self.error
        handler['links'] = self.links
        handler['enrollmentchecks'] = self.enrollmentchecks
        
        
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
    Property enrollmentchecks
    '''
    def enrollmentchecks(self, enrollment_checks):    
        if isinstance(enrollment_checks, EnrollmentChecks):
            self.__dict__['enrollmentchecks'] = enrollment_checks
        else:
            for count in range(0, enrollment_checks.__len__()):
                ec = EnrollmentChecks(enrollment_checks[count])
                self.__dict__.setdefault('enrollmentchecks', []).append(ec)
    
    '''
    Property Merchant Reference Number
    '''
    def merchantRefNum(self,merchant_ref_num):
        self.__dict__['merchantRefNum']= merchant_ref_num
        
    '''
    Property paRes
    '''
    def paRes(self, paRes):
        self.__dict__['paRes'] = paRes

    '''
    Property Customer Ip
    '''    
    def customerIp(self,customer_ip):
        self.__dict__['customerIp'] = customer_ip
        
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
    Property threeDResult
    '''
    def threeDResult(self, three_d_result):
        self.__dict__['threeDResult'] = three_d_result
        
    '''
    Property Signature Status
    '''
    def signatureStatus(self, signature_status):
        self.__dict__['signatureStatus'] = signature_status
        
    '''
    Property eci
    '''
    def eci(self, eci):
        self.__dict__['eci'] = eci
        
    '''
    Property cavv
    '''
    def cavv(self, cavv):
        self.__dict__['cavv'] = cavv
        
    '''
    Property xid
    '''
    def xid(self, xid):
        self.__dict__['xid'] = xid

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