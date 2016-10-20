'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.common.DomainObject import DomainObject


class AcquirerResponse(DomainObject):
    '''
    classdocs
    '''

    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['code'] = self.code
        handler['responseCode'] = self.responseCode
        handler['avsCode'] = self.avsCode
        handler['balanceResponse'] = self.balanceResponse
        handler['batchNumber'] = self.batchNumber
        handler['effectiveDate'] = self.effectiveDate
        handler['financingType'] = self.financingType
        handler['gracePeriod'] = self.gracePeriod
        handler['plan'] = self.plan
        handler['seqNumber'] = self.seqNumber
        handler['term'] = self.term
        handler['terminalId'] = self.terminalId
        handler['responseId'] = self.responseId
        handler['requestId'] = self.requestId
        handler['description'] = self.description
        handler['authCode'] = self.authCode
        handler['txnDateTime'] = self.txnDateTime
        handler['referenceNbr'] = self.referenceNbr
        handler['responseReasonCode'] = self.responseReasonCode
        handler['cvv2Result'] = self.cvv2Result
        handler['mid'] = self.mid
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
        
    '''
    Property Code
    '''
    def code(self, code):
        self.__dict__['code'] = code
        
    '''
    Property Response  Code
    '''
    def responseCode(self, response_code):
        self.__dict__['responseCode'] = response_code
        
    '''
    Property Avs Code
    '''
    def avsCode(self, avs_code):
        self.__dict__['avsCode'] = avs_code
        
    '''
    Property Balance Response
    '''
    def balanceResponse(self, balance_response):
        self.__dict__['balanceResponse'] = balance_response
        
    '''
    Property Batch Number
    '''
    def batchNumber(self, batch_number):
        self.__dict__['batchNumber'] = batch_number
        
    '''
    Property Effective Date
    '''
    def effectiveDate(self, effective_date):
        self.__dict__['effectiveDate'] = effective_date
        
    '''
    Property Financing Type
    '''
    def financingType(self, financing_type):
        self.__dict__['financingType'] = financing_type
        
    '''
    Property Grace Period
    '''
    def gracePeriod(self, grace_period):
        self.__dict__['gracePeriod'] = grace_period
        
    '''
    Property Plan
    '''
    def plan(self, plan):
        self.__dict__['plan']=plan
    
    '''
    Property Sequence Number
    '''
    def seqNumber(self, seq_number):
        self.__dict__['seqNumber'] = seq_number
        
    '''
    Property Term
    '''
    def term(self, term):
        self.__dict__['term'] = term 
    
    '''
    Property Terminal Id
    '''
    def terminalId(self, terminal_id):
        self.__dict__['terminalId'] = terminal_id
    
    '''
    Property Response Id
    '''
    def responseId(self, response_id):
        self.__dict__['responseId'] = response_id
       
    '''
    Property Request Id
    '''
    def requestId(self, request_id):
        self.__dict__['requestId'] = request_id
        
    '''
    Property Description
    '''
    def description(self, description):
        self.__dict__['description'] = description
    
    '''
    Property Auth Code
    '''
    def authCode(self, auth_code):
        self.__dict__['authCode'] = auth_code
        
    '''
    Property Txn Date Time
    '''
    def txnDateTime(self, txn_date_time):
        self.__dict__['txnDateTime'] = txn_date_time
        
    '''
    Property Reference Number
    '''
    def referenceNbr(self, reference_nbr):
        self.__dict__['referenceNbr'] = reference_nbr
        
    '''
    Property Response Reason Code
    '''
    def responseReasonCode(self, response_reason_code):
        self.__dict__['responseReasonCode'] = response_reason_code
        
    '''
    Property Cvv2Result
    '''
    def cvv2Result(self, cvv_2_result):
        self.__dict__['cvv2Result'] = cvv_2_result
        
    '''
    Property Mid
    '''
    def mid(self, mid):
        self.__dict__['mid'] = mid
