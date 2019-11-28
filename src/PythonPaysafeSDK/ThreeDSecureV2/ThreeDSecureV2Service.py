import inspect
from PythonPaysafeSDK import common
from PythonPaysafeSDK import ThreeDSecureV2

class ThreeDSecureV2Service(object):
    '''
    classdocs
    '''
    # Define URL paths for Purchase  
    _URI = '/threedsecure/v2'  
    _ACCOUNTS='/accounts/' 
    _URI_SEPARATOR = '/'
    _AUTHENTICATIONS_PATH = '/authentications'
    _MONITOR_PATH='/threedsecure/monitor'
    
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
        return (self._process_response(response,ThreeDSecureV2.Authentications.Authentications))


    '''
    Submit Authentications Request
    @param: Authentications Object
    @return: Authentications Object
    @raise: IOException
    @raise: OptimalException
    '''

    def submit_authentications_withCardDetails(self,data):
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                    self._account_no + \
                                    self._AUTHENTICATIONS_PATH+\
                                     self._URI_SEPARATOR)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                    req_method="POST",
                                                    url=FULL_URL,
                                                    data=data)   
        return (self._process_response(response, ThreeDSecureV2.Authentications.Authentications))

    '''
    Lookup Authentications by Id
    @return: Authentications object
    @raise exception: IOException
    @raise exception: OptimalException
    '''
    def lookup_authentications(self,data):      
        authentication_id = data.id
        if inspect.ismethod(authentication_id):
            err_msg = "Authentications Id not available"
            return (self.prepare_error(
                                    ThreeDSecureV2.Authentications.Authentications, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                    self._account_no + \
                                    self._AUTHENTICATIONS_PATH + \
                                    self._URI_SEPARATOR + \
                                    authentication_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)                
        return (self._process_response(response, ThreeDSecureV2.Authentications.Authentications))
