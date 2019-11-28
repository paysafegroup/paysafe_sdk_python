'''
Created on 30-Jan-2015

@author: Asawari.Vaidya
'''
import json
import urllib.error

from PythonPaysafeSDK.CardPayments.CardPaymentsService import \
                                    CardPaymentsService
from PythonPaysafeSDK.CustomerVault.CustomerVaultService import \
                                    CustomerVaultService
from PythonPaysafeSDK.DirectDebit.DirectDebitService import \
                                    DirectDebitService
from PythonPaysafeSDK.ThreeDSecure.ThreeDSecureService import \
                                    ThreeDSecureService
from PythonPaysafeSDK.ThreeDSecureV2.ThreeDSecureV2Service import \
                                    ThreeDSecureV2Service                                            
from PythonPaysafeSDK.common.DomainObject import DomainObject
from PythonPaysafeSDK.common.Error import Error
from bin.Environment import Environment
import urllib3.exceptions
import urllib3.util


# Global variables to create class objects
customer_vault_obj = None
card_payment_obj = None
direct_debit_obj = None
three_d_secure_obj = None
three_d_secure_v2_obj=None


class PaysafeApiClient(object):
    '''
    classdocs
    '''
    # Set Header
    _HEADERS = {"content-type": "application/json;charset=utf-8"}    
    
    # Response Encoding
    _RESPONSE_ENCODING = "utf-8"
     
     
    def __init__(self, api_key, api_password, env, account_number):
        '''
        Constructor
        '''
        self._api_key = api_key
        self._api_password = api_password
        self._environment = Environment._get_env(env)
        self._account_number = account_number

        
    def _update_env(self, host_url, max_connections, connection_timeout, read_timeout):
        self._environment = Environment(host_url, max_connections, True, connection_timeout, read_timeout)
        
    '''
    CustomerVaultServiceHandler
    '''    
    #customer_vault_obj1 = None
    def customer_vault_service_handler(self):        
        # Instance of class CustomerVaultService
        global customer_vault_obj
        if customer_vault_obj is None:
            customer_vault_obj = CustomerVaultService(self)
            
        return (customer_vault_obj)
    
    '''
    CardPaymentsSeriveHandler
    '''
    def card_payments_service_handler(self):
        #Instance of class CardPaymentsService
        global card_payment_obj
        if card_payment_obj is None:
            card_payment_obj = CardPaymentsService(self) 
            
        return (card_payment_obj)
    
    '''
    DirectDebitServiceHandler
    '''
    def direct_debit_service_handler(self):
        #Instance of class DirectDebitService
        global direct_debit_obj
        if direct_debit_obj is None:
            direct_debit_obj = DirectDebitService(self)
        
        return (direct_debit_obj)

    '''
    ThreeDSecureServiceHandler
    '''
    def three_d_secure_service_handler(self):
        #Instance of class ThreeDSecureService
        global three_d_secure_obj
        if three_d_secure_obj is None:
            three_d_secure_obj = ThreeDSecureService(self)
        
        return (three_d_secure_obj)

    '''
    ThreeDSecureV2ServiceHandler
    '''
    def three_d_secure_v2_service_handler(self):
        #Instance of class ThreeDSecureV2Service
        global three_d_secure_v2_obj 
        if three_d_secure_v2_obj is None:
            three_d_secure_v2_obj = ThreeDSecureV2Service(self)
        
        return(three_d_secure_v2_obj)
 

        
    '''
    Authorization Handler for API
    @return: Authentication object
    '''
    def authorization_header(self):
        authHeader = urllib3.util.make_headers(
                                basic_auth=self._api_key+":"+self._api_password)
        return (authHeader)

    '''
    Convert object to a dictionary
    @param: POJO Object
    @return: Dictionary Object
    '''
    def to_dictionary(self, obj):
        obj_dict = dict()
        for key in obj.__dict__.keys():
            try:
                if(type(obj.__dict__[key]) is list):
                    content = []
                    for count in range(0, obj.__dict__[key].__len__()):
                        if isinstance(obj.__dict__[key][count], DomainObject):
                            content.append(obj.__dict__[key][count].__dict__)
                        else:
                            content.append(self.to_dictionary(obj.__dict__[key][count]))
                    obj_dict[key] = content
                elif(isinstance(obj.__dict__[key], DomainObject)):
                    if isinstance(obj.__dict__[key], list):
                        content = []
                        for count in range(0, obj.__dict__[key].__len__()):
                            if isinstance(obj.__dict__[key][count], DomainObject):
                                content.append(obj.__dict__[key][count].__dict__)
                            else:
                                content.append(self.to_dictionary(obj.__dict__[key][count]))
                        obj_dict[key] = content    
                    else:        
                        obj_dict[key] = self.to_dictionary(obj.__dict__[key])
                else:
                    obj_dict[key] = obj.__dict__[key]
            except KeyError:
                pass
            except AttributeError:
                pass
        return (obj_dict)
        
    '''
    Serializing object
    @param: Dictionary Object
    @return: Serialized data
    '''
    def serialize(self, obj):
        str_serialize = json.dumps(self.to_dictionary(obj))
        # print ("\nserialize======>\n", str_serialize)
        return (str_serialize)

    '''
    De-Serializing object
    @param: Response Object, encoding method
    @return: De-serialized Object
    '''
    def deserialize(self, obj, encoding):
        if encoding:
            encoding = "utf-8"
        jsonStr = obj.decode(encoding)
        if jsonStr:
            str_deserialize = json.loads(obj.decode(encoding))
            # print ("\nde-serialize=======>\n", str_deserialize)
            return (str_deserialize)
        else:
            return ("")
    
    '''
    Prepare Error
    This method is used to Handle HTTP Errors in process_request() method
    @param: Error Code, Error Message
    @return: Error Object
    '''
    def prepare_error(self, error_code, error_msg):
        err_obj = Error(None)
        err_obj.code(error_code)
        err_obj.message(error_msg)
        return (err_obj)
    
    '''
    Process Request
    @param: Request Method, URLm=, Request Data
    @return: Response Data
    '''
    def process_request(self, req_method, url, data):
        try:
            # Make headers for https request and authentication
            self._environment._pool.headers.update(self._HEADERS)
            self._environment._pool.headers.update(self.authorization_header())
            # Request Data is None (i.e. Not Required)

            if data is None:
                response = self._environment._pool.urlopen(req_method, url)
            # Request Data is Required
            else:
                # Print Request
                #print("\nRequest to server ======= > ", self.serialize(data))
                response = self._environment._pool.urlopen(
                                                    req_method, 
                                                    url, 
                                                    body=self.serialize(data))                
            # Request: DELETE (for Customer Vault Service only)
            # Response: Response Status Code 200, if Success
            if req_method is 'DELETE' and response.data.__len__() is 0:
                # Print Response
                # print("PAYSAFE Response =====> ", response.status)
                return (response.status)
            # Request: DELETE (for Card Payment Service)
            # Response: Response Object, if Success
            #           Response Error Object, if Failure
            elif req_method is 'DELETE' and response.data.__len__() > 0:
                # Print Response
                # print("PAYSAFE Response =====> ", response.data)
                return (self.deserialize(response.data,
                                         encoding=self._RESPONSE_ENCODING))
            # Request: GET (for Resend an Order Callback API)
            # Response: Response Status Code 200, if Success
            elif req_method is not 'DELETE' and response.data.__len__() is 0:
                # Print Response
                # print("PAYSAFE Response =====> ", response.status)
                return (response.status)
            # Request: Other Request Methods
            # Response: Response Object, if Success
            #           Response Error Object, if Failure
            else:
                # Print Response
                # print("PAYSAFE Response =====> ", response.data)
                return (self.deserialize(response.data,
                                         encoding=self._RESPONSE_ENCODING))
        # HTTPError from urllib.error
        except urllib.error.HTTPError as e:
            return self.prepare_error("400", e.code + "-[Details: " + \
                                      e.reason + "]")
        # HTTPError from urllib3.exceptions
        except urllib3.exceptions.HTTPError as e:
            return self.prepare_error("400", "Details: HTTP Error for "\
                                       + str(e))

        # KeyError
        except KeyError as e:
            return self.prepare_error("400","Details: Key Error for " + str(e))
        # AttributeError
        except AttributeError as e:
            return self.prepare_error("400", "Details: Attribute Error for " + \
                                      str(e))
