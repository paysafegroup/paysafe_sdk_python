'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.common.DomainObject import DomainObject


class Authentication(DomainObject):
    '''
    classdocs
    '''

    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['eci'] = self.eci
        handler['cavv'] = self.cavv
        handler['xid'] = self.xid
        handler['threeDEnrollment'] = self.threeDEnrollment
        handler['threeDResult'] = self.threeDResult
        handler['signatureStatus'] = self.signatureStatus
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
        
    '''
    Property Eci
    '''
    def eci(self, eci):
        self.__dict__['eci'] = eci
        
    '''
    Property Cavv
    '''
    def cavv(self, cavv):
        self.__dict__['cavv'] = cavv
        
    '''
    Property Xid
    '''
    def xid(self, xid):
        self.__dict__['xid'] = xid
        
    '''
    Property ThreeDEnrolment
    '''
    def threeDEnrollment(self, three_denrollment):
        self.__dict__['threeDEnrollment'] = three_denrollment
        
    '''
    Property ThreeDResult
    '''
    def threeDResult(self, three_dresult):
        self.__dict__['threeDResult'] = three_dresult
        
    '''
    Property Signature Status
    '''
    def signatureStatus(self, signature_status):
        self.__dict__['signatureStatus'] = signature_status
