'''
Created on 18-Apr-2016

@author: Asawari.Vaidya
'''
import inspect

from PythonPaysafeSDK import ThreeDSecure
from PythonPaysafeSDK import common


class ThreeDSecureService(object):
    '''
    classdocs
    '''
    # Define URL paths for Purchase  
    _MONITOR_PATH = '/threedsecure/monitor'
    _URI = '/threedsecure/v1'
    _ENROLLMENT_PATH = '/enrollmentchecks'
    _URI_SEPARATOR = '/'
    _AUTHENTICATIONS_PATH = '/authentications'
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
        return (self._process_response(response, ThreeDSecure.EnrollmentChecks.EnrollmentChecks))
        
    '''
    Submit Enrollment Request
    @param: EnrollmentChecks Object
    @return: EnrollmentChecks Object
    @raise: IOException
    @raise: OptimalException
    '''
    def submit_purchase_enrollment(self, data):
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._ENROLLMENT_PATH +\
                                     self._URI_SEPARATOR)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST",
                                                url=FULL_URL,
                                                data=data)   
        return (self._process_response(response, ThreeDSecure.EnrollmentChecks.EnrollmentChecks))
    
    '''
    Lookup Enrollment by Id
    @return: EnrollmentChecks object
    @raise exception: IOException
    @raise exception: OptimalException
    '''
    def lookup_enrollment(self, data):
        enrollment_id = data.id
        if inspect.ismethod(enrollment_id):
            err_msg = "EnrollmentChecks Id not available"
            return (self.prepare_error(
                                    ThreeDSecure.EnrollmentChecks.EnrollmentChecks, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._ENROLLMENT_PATH +\
                                     self._URI_SEPARATOR +\
                                     enrollment_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)                
        return (self._process_response(response, ThreeDSecure.EnrollmentChecks.EnrollmentChecks))

    '''
    Submit Authentications Request
    @param: Authentications Object
    @return: Authentications Object
    @raise: IOException
    @raise: OptimalException
    '''
    def submit_purchase_authentications(self, data):
        enrollment_id = data.enrollmentchecks.id
        if inspect.ismethod(enrollment_id):
            err_msg = "EnrollmentChecks Id not available"
            return (self.prepare_error(
                                    ThreeDSecure.Authentications.Authentications, 
                                    "400", 
                                    err_msg))
        del data.enrollmentchecks
                                    
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._ENROLLMENT_PATH + \
									 self._URI_SEPARATOR + \
                                     enrollment_id + \
                                     self._AUTHENTICATIONS_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST",
                                                url=FULL_URL,
                                                data=data)   
        return (self._process_response(response, ThreeDSecure.Authentications.Authentications))      

    '''
    Lookup Authentications by Id
    @return: Authentications object
    @raise exception: IOException
    @raise exception: OptimalException
    '''
    def lookup_authentications(self, data):      
        authentication_id = data.id
        if inspect.ismethod(authentication_id):
            err_msg = "Authentications Id not available"
            return (self.prepare_error(
                                    ThreeDSecure.Authentications.Authentications, 
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
        return (self._process_response(response, ThreeDSecure.Authentications.Authentications))        
        
    '''
    Lookup Authentications and corresponsing Enrollment Check
    @return: Authentications object
    @raise exception: IOException
    @raise exception: OptimalException
    '''
    def lookup_authentications_and_enrollment(self, data):
        _subcomponent_enrollment = '?fields=enrollmentchecks'
        
        authentication_id = data.id
        if inspect.ismethod(authentication_id):
            err_msg = "Authentications Id not available"
            return (self.prepare_error(
                                    ThreeDSecure.Authentications.Authentications, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._ACCOUNTS + \
                                     self._account_no + \
                                     self._AUTHENTICATIONS_PATH + \
                                     self._URI_SEPARATOR + \
                                     authentication_id + \
                                     _subcomponent_enrollment)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)                
        return (self._process_response(response, ThreeDSecure.Authentications.Authentications))     
