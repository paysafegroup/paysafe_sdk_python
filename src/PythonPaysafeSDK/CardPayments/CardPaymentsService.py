'''
Created on 30-Jan-2015

@author: Asawari.Vaidya
'''
import inspect

from PythonPaysafeSDK import CardPayments, common


class CardPaymentsService(object):
    '''
    classdocs
    '''

    # Define URL paths for Authorization, Authorization Reversal, 
    # Refund, Settlement, Verification
    _MONITOR_PATH = '/cardpayments/monitor'
    _URI = '/cardpayments/v1'
    _AUTH_PATH = '/auths'
    _AUTH_REVERSAL_PATH = '/voidauths'
    _SETTLEMENT_PATH = '/settlements'
    _REFUND_PATH = '/refunds'
    _VERIFY_PATH = '/verifications'
    _URI_SEPARATOR = '/'
    
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
            return self.prepare_error(class_name, response.code, response.message)
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
        return (self._process_response(
                                    response, 
                                    CardPayments.Authorization.Authorization))

    '''
    Create Authorization or Purchase
    
    @param: Authorization object
    @return: Authorization object
    @raise: IOException
    @raise: OptimalExcetpion
    '''
    def create_authorization(self, data):
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._AUTH_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="POST", 
                                    url=FULL_URL, 
                                    data=data)
    
        return (self._process_response(
                                    response, 
                                    CardPayments.Authorization.Authorization))
    
    '''
    Update an Authorization : Complete a Held Authorization
    
    @param: Authorization Id, Authoirzation object
    @return: Authorization object
    @raise: IOException
    @raise: OptimalException
    '''    
    def update_authorization(self, data):
        auth_id = data.id
        if inspect.ismethod(auth_id):
            err_msg = "Authorization Id not available"
            return (self.prepare_error(
                                    CardPayments.Authorization.Authorization, 
                                    "400", 
                                    err_msg))
        del data.id
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._AUTH_PATH + \
                                     self._URI_SEPARATOR + \
                                     auth_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="PUT", 
                                    url=FULL_URL, 
                                    data=data)
        return (self._process_response(
                                    response,
                                    CardPayments.Authorization.Authorization))

    '''
    Settle an Authorization
    
    @param: Authorization Id, Authorization object
    @return: Authorization object
    @raise: IOException
    @raise: OptimalException
    '''
    def settle_authorization(self, data):
        auth_id = data.id
        if inspect.ismethod(auth_id):
            err_msg = "Authorization Id not available"
            return (self.prepare_error(
                                    CardPayments.Authorization.Authorization, 
                                    "400", 
                                    err_msg))
        del data.id
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._AUTH_PATH + \
                                     self._URI_SEPARATOR + \
                                     auth_id + \
                                     self._SETTLEMENT_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="POST", 
                                    url=FULL_URL, 
                                    data=data)
        return (self._process_response(
                                    response,
                                    CardPayments.Authorization.Authorization))
    
    '''
    Get an Authorization
    
    @param: Authorization Id, Authorization object
    @return: Authorization object
    @raise: IOException
    @raise: OptimalException
    '''
    def lookup_authorization_with_id(self, data):
        auth_id = data.id
        if inspect.ismethod(auth_id):
            err_msg = "Authorization Id not available"
            return (self.prepare_error(
                                    CardPayments.Authorization.Authorization, 
                                    "400", 
                                    err_msg))
        del data.id
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._AUTH_PATH + \
                                     self._URI_SEPARATOR + \
                                     auth_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="GET", 
                                    url=FULL_URL, 
                                    data=None)
        return (self._process_response(
                                    response,
                                    CardPayments.Authorization.Authorization))

    '''
    Get an Authorization
    
    @param: Authorization Id, Merchant Reference Number, Authorization Object
    @return: Authorization object
    @raise: IOException
    @raise: OptimalException
    '''
    def lookup_authorization_with_merchant_no(self, data, pagination_data):
        merchant_ref_no = data.merchantRefNum
        if inspect.ismethod(merchant_ref_no):
            err_msg = "Merchant Reference Number Id not available"
            return (self.prepare_error(CardPayments.Authorization.Authorization, 
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
                                     self._AUTH_PATH + \
                                     queryString)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="GET", 
                                    url=FULL_URL, 
                                    data=None)
        return (self._process_response(
                                    response,
                                    CardPayments.Authorization.Authorization))

    
    '''
    Authorize request with Payment Token
    
    @param: Authorization object
    @return: Authorization object
    @raise: IOException
    @raise: OptimalException
    '''
    def authorize_request_with_payment_token(self, data):
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._AUTH_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="POST", 
                                    url=FULL_URL, 
                                    data=data)
        return (self._process_response(
                                    response,
                                    CardPayments.Authorization.Authorization))

    '''
    Cancel a Held Authorization
    
    @param: Authorization Id, Authorization object
    @return: Authorization object
    @raise: IOExcetpion
    @raise: OptimalException
    '''
    def cancel_held_authorization(self, data):
        auth_id = data.id
        if inspect.ismethod(auth_id):
            err_msg = "Authorization Id not available"
            return (self.prepare_error(CardPayments.Authorization.Authorization, 
                                       "400", 
                                       err_msg))
        del data.id
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._AUTH_PATH + \
                                     self._URI_SEPARATOR + \
                                     auth_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="PUT", 
                                    url=FULL_URL, 
                                    data=data)
        return (self._process_response(
                                    response,
                                    CardPayments.Authorization.Authorization))

    '''
    Get an Authorization Reversal
    
    @param: Void Authorization Id, AuthorizationReversal object
    @return: AuthorizationReversal object
    @raise: IOException
    @raise: OptimalExcetpion
    '''
    def lookup_authorization_reversal_with_id(self, data):
        void_auth_id = data.id
        if inspect.ismethod(void_auth_id):
            err_msg = "Void Authorization Id not available"
            return (self.prepare_error(
                    CardPayments.AuthorizationReversal.AuthorizationReversal, 
                    "400",
                    err_msg))
        del data.id
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._AUTH_REVERSAL_PATH + \
                                     self._URI_SEPARATOR + \
                                     void_auth_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="GET", 
                                    url=FULL_URL, 
                                    data=None)
        return (self._process_response(
                    response,
                    CardPayments.AuthorizationReversal.AuthorizationReversal))

    '''
    Get an Authorization Reversal
    
    @param: Merchant Reference Number, Void Authorization Id, 
            AuthorizationReversal object
    @return: AuthorizationReversal object
    @raise: IOException
    @raise: OptimalExcetpion
    '''
    def lookup_authorization_reversal_with_merchant_no(self, data, pagination_data):
        merchant_ref_no = data.merchantRefNum
        if inspect.ismethod(merchant_ref_no):
            err_msg = "Merchant Reference Number not available"
            return (self.prepare_error(
                    CardPayments.AuthorizationReversal.AuthorizationReversal, 
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
                                     self._AUTH_REVERSAL_PATH + \
                                     queryString)
        
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="GET", 
                                    url=FULL_URL, 
                                    data=None)
        return (self._process_response(
                    response,
                    CardPayments.AuthorizationReversal.AuthorizationReversal))
                    
    '''
    Reverse an Authorization using Merchant Reference Number
    
    @param: Merchant Reference Number, AuthorizationReversal Object
    @return: AuthorizationReversal object
    @raise: IOException
    @raise: OptimalExcetpion
    '''
    def reverse_authorization_using_merchant_no(self, data):
        auth_id = data.authorization.id
        if inspect.ismethod(auth_id):
            err_msg = "Authorization Id not available"
            return (self.prepare_error(
                    CardPayments.AuthorizationReversal.AuthorizationReversal, 
                    "400", 
                    err_msg))
        del data.authorization
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._AUTH_PATH + \
                                     self._URI_SEPARATOR + \
                                     auth_id + \
                                     self._AUTH_REVERSAL_PATH)    
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="POST", 
                                    url=FULL_URL, 
                                    data=data)        
        return (self._process_response(
                    response,
                    CardPayments.AuthorizationReversal.AuthorizationReversal))
 
    '''
    Duplicate Authorization Reversal Response
    
    @param: Authorization Id, AuthorizationReversal object
    @return: AuthorizationReversal object
    @raise: IOException
    @raise: OptimalException
    '''
    def duplicate_authorization_reversal_response(self, data):
        auth_id = data.id
        if inspect.ismethod(auth_id):
            err_msg = "Authorization Id not available"
            return (self.prepare_error(
                    CardPayments.AuthorizationReversal.AuthorizationReversal, 
                    "400", 
                    err_msg))
        del data.id
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no  + \
                                     self._AUTH_PATH + \
                                     self._URI_SEPARATOR + \
                                     auth_id + \
                                     self._AUTH_REVERSAL_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="POST", 
                                    url=FULL_URL, 
                                    data=data) 
        return (self._process_response(
                    response,
                    CardPayments.AuthorizationReversal.AuthorizationReversal))
 
    '''
    Get a Settlement
    
    @param: Settlement Id, Settlement object
    @return: Settlement object
    @raise: IOException
    @raise: OptimalException
    '''
    def lookup_settlement_with_id(self, data):
        settlement_id = data.id
        if inspect.ismethod(settlement_id):
            err_msg = "Settlement Id not available"
            return (self.prepare_error(
                                    CardPayments.Settlement.Settlement, 
                                    "400", 
                                    err_msg))
        del data.id
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no +  \
                                     self._SETTLEMENT_PATH + \
                                     self._URI_SEPARATOR + \
                                     settlement_id)
        # print ("Communicating to ", FULL_URL)             
        response = self.optimal_object.process_request(
                                    req_method="GET",
                                    url=FULL_URL, 
                                    data=data)
        return (self._process_response(
                                    response,
                                    CardPayments.Settlement.Settlement))

    '''
    Get a Settlement
    
    @param: Merchant Reference Number, Settlement Id, Settlement object
    @return: Settlement object
    @raise: IOException
    @raise: OptimalException
    '''
    def lookup_settlement_with_merchant_no(self, data, pagination_data):
        merchant_ref_no = data.merchantRefNum
        if inspect.ismethod(merchant_ref_no):
            err_msg = "Merchant Reference Number not available"
            return (self.prepare_error(
                                    CardPayments.Settlement.Settlement, 
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
                                     self._SETTLEMENT_PATH + \
                                     queryString)
        
        # print ("Communicating to ", FULL_URL)             
        response = self.optimal_object.process_request(
                                    req_method="GET", 
                                    url=FULL_URL, 
                                    data=data)
        return (self._process_response(
                                    response,
                                    CardPayments.Settlement.Settlement))

        
    '''
    Cancel a Settlement
    
    @param: Settlement Id, Settlement object
    @return: Settlement object
    @raise: IOException
    @raise: OptimalException
    '''
    def cancel_settlement(self, data):
        settlement_id = data.id
        if inspect.ismethod(settlement_id):
            err_msg = "Settlement Id not available"
            return (self.prepare_error(
                                    CardPayments.Settlement.Settlement, 
                                    "400", 
                                    err_msg))
        del data.id
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no  + \
                                     self._SETTLEMENT_PATH + \
                                     self._URI_SEPARATOR + \
                                     settlement_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="PUT", 
                                    url=FULL_URL, 
                                    data=data)        
        return (self._process_response(
                                    response,
                                    CardPayments.Settlement.Settlement))

    '''
    Create a refund
    
    @param: Settlement Id, Refund object
    @return: Refund object
    @raise: IOException
    @raise:  OptimalException
    '''
    def create_refund(self, data):
        settlement_id = data.settlements.id
        if inspect.ismethod(settlement_id):
            err_msg = "Settlement Id not available"
            return (self.prepare_error(
                                    CardPayments.Settlement.Settlement, 
                                    "400", 
                                    err_msg))
        del data.settlements
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no  + \
                                     self._SETTLEMENT_PATH + \
                                     self._URI_SEPARATOR + \
                                     settlement_id + \
                                     self._REFUND_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="POST", 
                                    url=FULL_URL, 
                                    data=data)
        return (self._process_response(
                                    response,
                                    CardPayments.Refund.Refund))
    
    '''
    Get a Refund
    
    @param: Refund Id, Refund object
    @return: Refund object
    @raise: IOException
    @raise: OptimalException
    '''
    def lookup_refund_with_id(self, data):
        refund_id = data.id
        if inspect.ismethod(refund_id):
            err_msg = "Settlement Id not available"
            return (self.prepare_error(
                                    CardPayments.Refund.Refund, 
                                    "400", 
                                    err_msg))
        del data.id
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no +\
                                     self._REFUND_PATH + \
                                     self._URI_SEPARATOR + \
                                     refund_id)
        # print ("Communicating to ", FULL_URL)        
        response = self.optimal_object.process_request(
                                    req_method="GET", 
                                    url=FULL_URL, 
                                    data=data)
        return (self._process_response(
                                    response,
                                    CardPayments.Refund.Refund))
  
    '''
    Get a Refund
    
    @param: Merchant Reference Number, Refund Id, Refund object
    @return: Refund object
    @raise: IOException
    @raise: OptimalException
    '''
    def lookup_refund_with_merchant_no(self, data, pagination_data):
        merchant_ref_no = data.merchantRefNum
        if inspect.ismethod(merchant_ref_no):
            err_msg = "Merchant Reference Number not available"
            return (self.prepare_error(
                                    CardPayments.Refund.Refund, 
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
                                     self._REFUND_PATH + \
                                     queryString)
        
        # print ("Communicating to ", FULL_URL)        
        response = self.optimal_object.process_request(
                                    req_method="GET", 
                                    url=FULL_URL, 
                                    data=data)  
        return (self._process_response(
                                    response,
                                    CardPayments.Refund.Refund))

    
    '''
    Cancel a Refund
    
    @param: Refund Id, Refund object
    @return: Refund object 
    @raise: IOException
    @raise: OptimalException
    '''
    def cancel_refund(self, data):
        refund_id = data.id
        if inspect.ismethod(refund_id):
            err_msg = "Settlement Id not available"
            return (self.prepare_error(
                                    CardPayments.Refund.Refund, 
                                    "400", 
                                    err_msg))
        del data.id
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._REFUND_PATH + \
                                     self._URI_SEPARATOR + \
                                     refund_id)
        # print ("Communicating to ", FULL_URL)       
        response = self.optimal_object.process_request(
                                    req_method="PUT", 
                                    url=FULL_URL, 
                                    data=data)
        return (self._process_response(
                                    response,
                                    CardPayments.Refund.Refund))

    '''
    Verify a Card

    @param: Verification Object
    @return: Verification Object
    @raise: IOException
    @raise: OptimalException
    '''
    def verify_card(self, data):
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._VERIFY_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="POST",
                                    url=FULL_URL,
                                    data=data)
        return (self._process_response(
                                    response,
                                    CardPayments.Verification.Verification))

    '''
    Lookup a Verification using a Verification Id

    @param: Verification Id
    @return: Verification Object
    @raise: IOException
    @raise: OptimalException
    '''
    def lookup_verification_using_id(self, data):
        verification_id = data.id
        if inspect.ismethod(verification_id):
            err_msg = "Verification Id not available"
            return (self.prepare_error(
                                    CardPayments.Verification.Verification, 
                                    "400", 
                                    err_msg))
        del data.id

        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._VERIFY_PATH +\
                                     self._URI_SEPARATOR +\
                                     verification_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="GET",
                                    url=FULL_URL,
                                    data=data)
        return (self._process_response(
                                    response,
                                    CardPayments.Verification.Verification))

    '''
    Lookup a Verification using a Merchant Reference Number

    @param: Merchant Reference Number
    @return: Verification Object
    @raise: IOException
    @raise: OptimalException
    '''
    def lookup_verification_using_merchant_ref_num(self, data, pagination_data):
        merchant_ref_no = data.merchantRefNum
        if inspect.ismethod(merchant_ref_no):
            err_msg = "Merchant Reference Number not available"
            return (self.prepare_error(
                                    CardPayments.Verification.Verification, 
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
                                     self._VERIFY_PATH + \
                                     queryString)
        
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                    req_method="GET",
                                    url=FULL_URL,
                                    data=data)
        return (self._process_response(
                                    response,
                                    CardPayments.Verification.Verification))
