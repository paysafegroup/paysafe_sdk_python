'''
Created on 11-Apr-2016

@author: Murali.Mohan
'''
import inspect

from PythonPaysafeSDK import DirectDebit
from PythonPaysafeSDK import common


class DirectDebitService(object):
    '''
    classdocs
    '''
    # Define URL paths for Purchase  
    _MONITOR_PATH = '/directdebit/monitor'
    _URI = '/directdebit/v1'
    _PURCHASE_PATH = '/purchases'
    _URI_SEPARATOR = '/'
    _STANDALONE_PATH = '/standalonecredits'
    
    _MERCHANT_REF_NUM = "?merchantRefNum="
    _LIMIT = "&limit="
    _OFFSET = "&offset="
    _START_DATE = "&startDate="
    _END_DATE = "&endDate="    
    _ACCOUNTS="/accounts/"
    
    def __init__(self, optimal_object):
        '''
        Constructor
        '''
        self.optimal_object = optimal_object
        self._account_no = optimal_object._account_number
        
    '''
    Prepare URL for process request
    @param: Chunks of paths
    @return: Complete URL for Processing Request
    '''
    def _prepare_uri(self, path):
        return self._URI + path    
        
    '''
    Process the response from the Server
    @param: response object, class name
    @return: object of class
    '''
    def _process_response(self, response, class_name):
        if isinstance(response, int):
            response_status = class_name(None)
            response_status.status = response
            return (response_status)
        elif response is None:
            return class_name(None)
        elif isinstance(response, common.Error.Error):
            return self.prepare_error(class_name, response.code, 
                                                  response.message)
        else:
            return (class_name(response))
            
    '''
    Prepare Error Response
    @param: response object, class name
    @return: object of class
    '''    
    def prepare_error(self, class_name, error_code, error_message):
        error_object_response = class_name(None)
        error_obj = common.Error.Error(None)
        error_obj.code(error_code)
        error_obj.message(error_message)
        error_object_response.error(error_obj.__dict__)
        return (error_object_response)

    '''
    Monitor
    
    @param: None
    @return: Response Status
    @raise: IOException
    @raise: OptimalException
    '''
    def monitor(self):
        FULL_URL = self._MONITOR_PATH
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET",
                                                url=FULL_URL,
                                                data=None)   
        return (self._process_response(response, DirectDebit.Purchase.Purchase))
        
    '''
    Submit Purchase Request 
    
    @param: Purchase object
    @return: Purchase object
    @raise: IOException
    @raise: OptimalException
    '''
    def submit_purchase(self, data):
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._PURCHASE_PATH +\
                                     self._URI_SEPARATOR)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST",
                                                url=FULL_URL,
                                                data=data)   
        return (self._process_response(response, DirectDebit.Purchase.Purchase))
  
    '''
    Cancel Purchase
    
    @param: Purchase object
    @return: Purchase object
    @raise: IOException
    @raise: OptimalException
    '''
    def cancel_purchase(self, data):
        purchase_id = data.id
        if inspect.ismethod(purchase_id):
            err_msg = "Purchase Id not available"
            return (self.prepare_error(
                                    DirectDebit.Purchase.Purchase, 
                                    "400", 
                                    err_msg))
        del data.id
         
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._PURCHASE_PATH + \
                                     self._URI_SEPARATOR + \
                                     purchase_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="PUT", 
                                                url=FULL_URL, 
                                                data=data)      
        return (self._process_response(response, DirectDebit.Purchase.Purchase))
            
    '''
    Lookup a Purchase using an ID  
    
    @param: purchase id
    @return: Purchase object
    @raise exception: IOException
    @raise exception: OptimalException
    '''
    def lookup_purchase(self, data):
        purchase_id = data.id
        if inspect.ismethod(purchase_id):
            err_msg = "Purchase Id not available"
            return (self.prepare_error(
                                    DirectDebit.Purchase.Purchase, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._PURCHASE_PATH + \
                                     self._URI_SEPARATOR + \
                                     purchase_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)                
        return (self._process_response(response, DirectDebit.Purchase.Purchase))
        
    '''
    Lookup a Purchase using Merchant Reference Number
    
    @param: Merchant Reference Number, Purchase object
    @return: Purchase object
    @raise: IOException
    @raise: OptimalExcetpion
    '''
    def lookup_purchase_with_merchant_no(self, data, pagination_data):
        merchant_ref_no = data.merchantRefNum
        if inspect.ismethod(merchant_ref_no):
            err_msg = "Merchant Reference Number not available"
            return (self.prepare_error(
                    DirectDebit.Purchase.Purchase, 
                    "400", 
                    err_msg))
        del data.merchantRefNum
        
        queryString = self._MERCHANT_REF_NUM + merchant_ref_no
        limit = pagination_data.limit
        offset = pagination_data.offset
        start_date = pagination_data.startDate
        end_date = pagination_data.endDate
        
        if (pagination_data is not None):
            if inspect.ismethod(limit):
                pass
            else:
                queryString = queryString + self._LIMIT + limit
            if inspect.ismethod(offset):
                pass
            else:
                queryString = queryString + self._OFFSET + offset
            if inspect.ismethod(start_date):
                pass
            else:
                queryString = queryString + self._START_DATE + start_date
            if inspect.ismethod(end_date):
                pass
            else:
                queryString = queryString + self._END_DATE + end_date

        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._PURCHASE_PATH + \
                                     queryString)
        
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="GET", 
                                    url=FULL_URL, 
                                    data=None)
        
        return (self._process_response(response, DirectDebit.Purchase.Purchase))
                
    '''
    Submit Standalone Credits Request 
    
    @param: StandaloneCredits object
    @return: StandaloneCredits object
    @raise: IOException
    @raise: OptimalException
    '''
    def submit_standalone(self, data):
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._STANDALONE_PATH +\
                                     self._URI_SEPARATOR)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST",
                                                url=FULL_URL,
                                                data=data)   
        return (self._process_response(response, DirectDebit.StandaloneCredits.StandaloneCredits))

    '''
    Cancel Standalone Credit
    
    @param: StandaloneCredits object
    @return: StandaloneCredits object
    @raise: IOException
    @raise: OptimalException
    '''
    def cancel_standalone(self, data):
        standalone_id = data.id
        if inspect.ismethod(standalone_id):
            err_msg = "StandaloneCredits Id not available"
            return (self.prepare_error(
                                    DirectDebit.StandaloneCredits.StandaloneCredits, 
                                    "400", 
                                    err_msg))
        del data.id
         
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._STANDALONE_PATH + \
                                     self._URI_SEPARATOR + \
                                     standalone_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="PUT", 
                                                url=FULL_URL, 
                                                data=data)      
        return (self._process_response(response, DirectDebit.StandaloneCredits.StandaloneCredits))
        
    '''
    Lookup a Standalone Credit using an ID  
    
    @param: standalonecredit id
    @return: StandaloneCredits object
    @raise exception: IOException
    @raise exception: OptimalException
    '''
    def lookup_standalone(self, data):
        standalone_id = data.id
        if inspect.ismethod(standalone_id):
            err_msg = "StandaloneCredits Id not available"
            return (self.prepare_error(
                                    DirectDebit.StandaloneCredits.StandaloneCredits, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._STANDALONE_PATH + \
                                     self._URI_SEPARATOR + \
                                     standalone_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)                
        return (self._process_response(response, DirectDebit.StandaloneCredits.StandaloneCredits))
        
    '''
    Lookup a Standalone Credit using Merchant Reference Number
    
    @param: Merchant Reference Number, StandaloneCredits object
    @return: StandaloneCredits object
    @raise: IOException
    @raise: OptimalExcetpion
    '''
    def lookup_standalone_with_merchant_no(self, data, pagination_data):
        merchant_ref_no = data.merchantRefNum
        if inspect.ismethod(merchant_ref_no):
            err_msg = "Merchant Reference Number not available"
            return (self.prepare_error(
                    DirectDebit.StandaloneCredits.StandaloneCredits, 
                    "400", 
                    err_msg))
        del data.merchantRefNum
        
        queryString = self._MERCHANT_REF_NUM + merchant_ref_no
        limit = pagination_data.limit
        offset = pagination_data.offset
        start_date = pagination_data.startDate
        end_date = pagination_data.endDate
        
        if (pagination_data is not None):
            if inspect.ismethod(limit):
                pass
            else:
                queryString = queryString + self._LIMIT + limit
            if inspect.ismethod(offset):
                pass
            else:
                queryString = queryString + self._OFFSET + offset
            if inspect.ismethod(start_date):
                pass
            else:
                queryString = queryString + self._START_DATE + start_date
            if inspect.ismethod(end_date):
                pass
            else:
                queryString = queryString + self._END_DATE + end_date

        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._STANDALONE_PATH + \
                                     queryString)
        
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="GET", 
                                    url=FULL_URL, 
                                    data=None)
        
        return (self._process_response(response, DirectDebit.StandaloneCredits.StandaloneCredits))
