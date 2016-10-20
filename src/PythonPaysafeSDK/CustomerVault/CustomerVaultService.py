'''
Created on 30-Jan-2015

@author: Asawari.Vaidya
'''
import inspect

from PythonPaysafeSDK import CustomerVault
from PythonPaysafeSDK import common


class CustomerVaultService(object):
    '''
    classdocs
    '''
    # Define URL paths for Customer Profile, Address and Card
    _MONITOR_PATH = '/customervault/monitor'
    _URI = '/customervault/v1'
    _PROFILE_PATH = '/profiles/'
    _ADDRESS_PATH = '/addresses/'
    _CARD_PATH = '/cards/'
    _ACH_BANK_PATH = '/achbankaccounts/'
    _BACS_BANK_PATH = '/bacsbankaccounts/'
    _EFT_BANK_PATH = '/eftbankaccounts/'
    _SEPA_BANK_PATH = '/sepabankaccounts/'
    _MANDATES_PATH = '/mandates'
    _URI_SEPARATOR = '/'

    def __init__(self, optimal_object):
        '''
        Constructor
        '''
        self.optimal_object = optimal_object
        
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
        return (self._process_response(response, CustomerVault.Profile.Profile))
    
    '''
    Create a Customer Profile
    
    @param: Profile object
    @return: Profile object
    @raise: IOException
    @raise: OptimalException
    '''
    def create_profile(self, data):
        FULL_URL = self._prepare_uri(self._PROFILE_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST",
                                                url=FULL_URL,
                                                data=data)   
        return (self._process_response(response, CustomerVault.Profile.Profile))
    
    '''
    Lookup a Customer Profile
    
    @param: Profile Id
    @return: Profile object
    @raise exception: IOException
    @raise exception: OptimalException
    '''
    def lookup_profile(self, data):
        profile_id = data.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Profile.Profile, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)                
        return (self._process_response(response, CustomerVault.Profile.Profile))       

    '''
    Lookup a Customer Profile with Subcomponents [NEW]
    
    @param: Profile Id
    @param: is_ddresses indicate whether to include addresses in response
    @param: is_ards indicate whether to include cards in response 
    @return: Profile object
    @raise: IOException
    @raise: OptimalException
    '''
    def lookup_profile_subcomponents(self, data, is_addresses, is_cards, 
                                    is_achbankaccounts, is_bacsbankaccounts, 
                                    is_eftbankaccounts, is_sepabankaccounts):
        _subcomponents = '?fields='
        _subcomponent_card = 'cards'
        _subcomponent_address = 'addresses'
        _subcomponent_ach = 'achbankaccounts'
        _subcomponent_bacs = 'bacsbankaccounts'
        _subcomponent_eft = 'eftbankaccounts'
        _subcomponent_sepa = 'sepabankaccounts'
        _comma_separator = ','
        _ampersand_separator = '&'
        
        to_include = []
        query_str = ''
        
        profile_id = data.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Profile.Profile, 
                                    "400", 
                                    err_msg))
        del data.id

        if(is_addresses is True):
            to_include.append(_subcomponent_address)
        if(is_cards is True):
            if(to_include.__len__() > 0):
                to_include += _comma_separator
            to_include.append(_subcomponent_card)
        if(is_achbankaccounts is True):
            if(to_include.__len__() > 0):
                to_include += _comma_separator
            to_include.append(_subcomponent_ach)
        if(is_bacsbankaccounts is True):
            if(to_include.__len__() > 0):
                to_include += _comma_separator
            to_include.append(_subcomponent_bacs)
        if(is_eftbankaccounts is True):
            if(to_include.__len__() > 0):
                to_include += _comma_separator
            to_include.append(_subcomponent_eft)
        if(is_sepabankaccounts is True):
            if(to_include.__len__() > 0):
                to_include += _comma_separator
            to_include.append(_subcomponent_sepa)            

        if(to_include.__len__() > 0):
            query_str += _subcomponents
            for count in range(0, to_include.__len__()):
                query_str += to_include[count]
                
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + profile_id + query_str)

        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)  
        return (self._process_response(response, CustomerVault.Profile.Profile))  
        
    '''
    Update a Customer Profile
    
    @param: Profile Id, Profile object
    @return: Profile object
    @raise: IOException
    @raise: OptimalException
    '''
    def update_profile(self, data):
        profile_id = data.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Profile.Profile, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="PUT", 
                                                url=FULL_URL, 
                                                data=data)      
        return (self._process_response(response, CustomerVault.Profile.Profile))
    
    '''
    Delete a Customer Profile
    
    @param: Profile Id
    @return: Response Status
    @raise: IOException
    @raise: OptimalException
    '''
    def delete_profile(self, data):
        profile_id = data.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Profile.Profile, 
                                    "400", 
                                    err_msg))
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="DELETE", 
                                                url=FULL_URL, 
                                                data=None)   
        return (self._process_response(response, CustomerVault.Profile.Profile))
    
    '''
    Create an Address
    
    @param: Profile Id, Addresses object
    @return: Addresses object
    @raise: IOException
    @raise: OptimalException
    '''
    def create_address(self, data):
        profile_id = data.profile.id 
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Addresses.Address, 
                                    "400", 
                                    err_msg))   
        del data.profile

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._ADDRESS_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST", 
                                                url=FULL_URL, 
                                                data=data)      
        return (self._process_response(response, 
                                    CustomerVault.Addresses.Address))
        
    '''
    Lookup an Address
    
    @params: Profile Id, Address Id, Addresses object
    @return: Addresses object
    @raise: IOException
    @raise: OptimalException
    '''
    def lookup_address(self, data):
        profile_id = data.profile.id    
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Addresses.Address, 
                                    "400", 
                                    err_msg))
        del data.profile
        address_id = data.id
        if inspect.ismethod(address_id):
            err_msg = "Address Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._ADDRESS_PATH + \
                                    address_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)      
        return (self._process_response(response, 
                                    CustomerVault.Addresses.Address))
    
    '''
    Update an Address
    
    @param: Profile Id, Address Id, Addresses object
    @return: Addresses object
    @raise: IOException
    @raise: OptimalException
    '''
    def update_address(self, data):
        profile_id = data.profile.id  
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                    "400", 
                                    err_msg)) 
        del data.profile
        address_id = data.id
        if inspect.ismethod(address_id):
            err_msg = "Address Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                    "400", 
                                    err_msg))
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._ADDRESS_PATH + \
                                    address_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="PUT", 
                                                url=FULL_URL, 
                                                data=data)        
        return (self._process_response(response, 
                                    CustomerVault.Addresses.Address))
    
    '''
    Delete an Address
    
    @param: Profile Id, Address Id
    @return: Response Status
    @raise: IOException
    @raise: OptimalException
    '''
    def delete_address(self, data):
        profile_id = data.profile.id 
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                    "400", 
                                    err_msg))       
        del data.profile
        address_id = data.id
        if inspect.ismethod(address_id):
            err_msg = "Address Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                    "400", 
                                    err_msg)) 
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._ADDRESS_PATH + \
                                    address_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="DELETE", 
                                                url=FULL_URL, 
                                                data=None)
        return (self._process_response(response, 
                                    CustomerVault.Addresses.Address))
    
    '''
    Create a Card
    
    @param: Profile Id, Card object
    @return: Card object
    @raise: IOException
    @raise: OptimalException
    '''
    def create_card(self, data):
        profile_id = data.profile.id  
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.Card.Card, 
                                    "400", 
                                    err_msg))  
        del data.profile
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._CARD_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST", 
                                                url=FULL_URL, 
                                                data=data)    
        return (self._process_response(response, 
                                    CustomerVault.Card.Card))
    
    '''
    Lookup a Card
    
    @param: Profile Id, Card Id, Card object
    @return: Card object
    @raise: IOException
    @raise: OptimalException
    '''
    def lookup_card(self, data):
        profile_id = data.profile.id 
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.Card.Card, 
                                    "400", 
                                    err_msg))      
        del data.profile
        card_id = data.id
        if inspect.ismethod(card_id):
            err_msg = "Card Id not available"
            return (self.prepare_error(CustomerVault.Card.Card, 
                                    "400", 
                                    err_msg))
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._CARD_PATH + \
                                    card_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)     
        return (self._process_response(response, 
                                    CustomerVault.Card.Card))
    
    '''
    Update a Card
    
    @param: Profile Id, Card Id, Card object
    @return: Card object
    @raise: IOException
    @raise: OptimalException
    '''
    def update_card(self, data):
        profile_id = data.profile.id   
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.Card.Card, 
                                    "400", 
                                    err_msg))       
        del data.profile
        card_id = data.id
        if inspect.ismethod(card_id):
            err_msg = "Card Id not available"
            return (self.prepare_error(CustomerVault.Card.Card, 
                                    "400", 
                                    err_msg))   
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._CARD_PATH + \
                                    card_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="PUT", 
                                                url=FULL_URL, 
                                                data=data)      
        return (self._process_response(response,
                                    CustomerVault.Card.Card))
    
    '''
    Delete a Card
    
    @param: Profile Id, Card Id
    @return: Response Status
    @raise: IOException
    @raise: OptimalException
    '''
    def delete_card(self, data):
        profile_id = data.profile.id  
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.Card.Card, 
                                    "400", 
                                    err_msg))         
        del data.profile
        card_id = data.id
        if inspect.ismethod(card_id):
            err_msg = "Card Id not available"
            return (self.prepare_error(CustomerVault.Card.Card, 
                                    "400", 
                                    err_msg))
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._CARD_PATH + \
                                    card_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="DELETE", 
                                                url=FULL_URL, 
                                                data=None) 
        return (self._process_response(response, 
                                    CustomerVault.Card.Card))
                                    
    '''
    Create ACH Bank Account
    
    @param: ACHBankAccount Object
    @return: ACHBankAccount Object
    @raise: IOException
    @raise: OptimalException
    '''
    def create_ach_bank_account(self,data):
        profile_id = data.profile.id  
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            
            return (self.prepare_error(CustomerVault.ACHBankAccount.ACHBankAccount, 
                                    "400", 
                                    err_msg))         
        del data.profile
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._ACH_BANK_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST",
                                                url=FULL_URL,
                                                data=data)   
        return (self._process_response(response, CustomerVault.ACHBankAccount.ACHBankAccount))
    
    '''
    Lookup a ACH Bank Account
    
    @param: ACHBankAccount 
    @return: ACHBankAccount object
    @raise exception: IOException
    @raise exception: OptimalException
    '''
    def lookup_ach_bank_account(self, data):
        profile_id = data.profile.id  
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.ACHBankAccount.ACHBankAccount, 
                                    "400", 
                                    err_msg))         
        del data.profile
        
        ach_bank_id = data.id
        if inspect.ismethod(ach_bank_id):
            err_msg = "ACH Bank Account Id not available"
            return (self.prepare_error(
                                    CustomerVault.ACHBankAccount.ACHBankAccount, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._ACH_BANK_PATH + \
                                    ach_bank_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)                
        return (self._process_response(response, CustomerVault.ACHBankAccount.ACHBankAccount))
        
    '''
    Update ACHBankAccount
    @param: ACHBankAccount object
    @return: ACHBankAccount object
    @raise: IOException
    @raise: OptimalException
    '''
    def update_ach_bank_account(self, data):
        profile_id = data.profile.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.ACHBankAccount.ACHBankAccount, 
                                    "400", 
                                    err_msg))
        del data.profile
        
        ach_bank_id = data.id
        if inspect.ismethod(ach_bank_id):
            err_msg = "ACH Bank Account Id not available"
            return (self.prepare_error(
                                    CustomerVault.ACHBankAccount.ACHBankAccount, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._ACH_BANK_PATH +\
                                    ach_bank_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="PUT", 
                                                url=FULL_URL, 
                                                data=data)      
        return (self._process_response(response, CustomerVault.ACHBankAccount.ACHBankAccount))        
        
    '''
    Delete a ACHBankAccount
    
    @param: ACHBankAccount 
    @return: Response Status
    @raise: IOException
    @raise: OptimalException
    '''
    
    def delete_ach_bank_account(self, data):
        profile_id = data.profile.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.ACHBankAccount.ACHBankAccount, 
                                    "400", 
                                    err_msg))
        del data.profile
        
        ach_bank_id = data.id
        if inspect.ismethod(ach_bank_id):
            err_msg = "ACH Bank Account Id not available"
            return (self.prepare_error(
                                    CustomerVault.ACHBankAccount.ACHBankAccount, 
                                    "400", 
                                    err_msg))
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._ACH_BANK_PATH +\
                                    ach_bank_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="DELETE", 
                                                url=FULL_URL, 
                                                data=None)   
        return (self._process_response(response, CustomerVault.ACHBankAccount.ACHBankAccount))
        
    '''
    Create BACS Bank Account
    
    @param: BACSBankAccount Object
    @return: BACSBankAccount Object
    @raise: IOException
    @raise: OptimalException
    '''
    def create_bacs_bank_account(self, data):
        profile_id = data.profile.id  
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.BACSBankAccount.BACSBankAccount, 
                                    "400", 
                                    err_msg))         
        del data.profile
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._BACS_BANK_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST",
                                                url=FULL_URL,
                                                data=data)   
        return (self._process_response(response, CustomerVault.BACSBankAccount.BACSBankAccount))

    '''
    Lookup a BACS Bank Account
    
    @param: BACSBankAccount Id
    @return: BACSBankAccount object
    @raise exception: IOException
    @raise exception: OptimalException
    '''
    def lookup_bacs_bank_account(self, data):
        profile_id = data.profile.id  
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.BACSBankAccount.BACSBankAccount, 
                                    "400", 
                                    err_msg))         
        del data.profile
        
        bacs_bank_id = data.id
        if inspect.ismethod(bacs_bank_id):
            err_msg = "BACS Bank Account Id not available"
            return (self.prepare_error(
                                    CustomerVault.BACSBankAccount.BACSBankAccount, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._BACS_BANK_PATH + \
                                    bacs_bank_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)                
        return (self._process_response(response, CustomerVault.BACSBankAccount.BACSBankAccount))
        
    '''
    Update BACSBankAccount
    @param: BACSBankAccount object
    @return: BACSBankAccount object
    @raise: IOException
    @raise: OptimalException
    '''
    def update_bacs_bank_account(self, data):
        profile_id = data.profile.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.BACSBankAccount.BACSBankAccount, 
                                    "400", 
                                    err_msg))
        del data.profile
        
        bacs_bank_id = data.id
        if inspect.ismethod(bacs_bank_id):
            err_msg = "BACS Bank Account Id not available"
            return (self.prepare_error(
                                    CustomerVault.BACSBankAccount.BACSBankAccount, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._BACS_BANK_PATH +\
                                    bacs_bank_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="PUT", 
                                                url=FULL_URL, 
                                                data=data)      
        return (self._process_response(response, CustomerVault.BACSBankAccount.BACSBankAccount))         

    '''
    Delete a BACSBankAccount
    
    @param: BACSBankAccount 
    @return: Response Status
    @raise: IOException
    @raise: OptimalException
    '''
    def delete_bacs_bank_account(self, data):
        profile_id = data.profile.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.BACSBankAccount.BACSBankAccount, 
                                    "400", 
                                    err_msg))
        del data.profile
        
        bacs_bank_id = data.id
        if inspect.ismethod(bacs_bank_id):
            err_msg = "BACS Bank Account Id not available"
            return (self.prepare_error(
                                    CustomerVault.BACSBankAccount.BACSBankAccount, 
                                    "400", 
                                    err_msg))
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._BACS_BANK_PATH +\
                                    bacs_bank_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="DELETE", 
                                                url=FULL_URL, 
                                                data=None)   
        return (self._process_response(response, CustomerVault.BACSBankAccount.BACSBankAccount))

    '''
    Create EFT Bank Account
    
    @param: EFTBankAccount Object
    @return: EFTBankAccount Object
    @raise: IOException
    @raise: OptimalException
    '''
    
    def create_eft_bank_account(self, data):
        profile_id = data.profile.id  
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.EFTBankAccount.EFTBankAccount, 
                                    "400", 
                                    err_msg))         
        del data.profile
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._EFT_BANK_PATH)        
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST",
                                                url=FULL_URL,
                                                data=data)   
        return (self._process_response(response, CustomerVault.EFTBankAccount.EFTBankAccount))

    '''
    Lookup a EFT Bank Account
    
    @param: EFTBankAccount Id
    @return: EFTBankAccount object
    @raise exception: IOException
    @raise exception: OptimalException
    '''
    def lookup_eft_bank_account(self, data):
        profile_id = data.profile.id  
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.EFTBankAccount.EFTBankAccount, 
                                    "400", 
                                    err_msg))         
        del data.profile
        
        eft_bank_id = data.id
        if inspect.ismethod(eft_bank_id):
            err_msg = "EFT Bank Account Id not available"
            return (self.prepare_error(
                                    CustomerVault.EFTBankAccount.EFTBankAccount, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._EFT_BANK_PATH + \
                                    eft_bank_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)                
        return (self._process_response(response, CustomerVault.EFTBankAccount.EFTBankAccount))
    
    '''
    Update EFTBankAccount
    @param: EFTBankAccount object
    @return: EFTBankAccount object
    @raise: IOException
    @raise: OptimalException
    '''
    
    def update_eft_bank_account(self, data):
        profile_id = data.profile.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.EFTBankAccount.EFTBankAccount, 
                                    "400", 
                                    err_msg))
        del data.profile
        
        eft_bank_id = data.id
        if inspect.ismethod(eft_bank_id):
            err_msg = "EFT Bank Account Id not available"
            return (self.prepare_error(
                                    CustomerVault.EFTBankAccount.EFTBankAccount, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._EFT_BANK_PATH +\
                                    eft_bank_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="PUT", 
                                                url=FULL_URL, 
                                                data=data)      
        return (self._process_response(response, CustomerVault.EFTBankAccount.EFTBankAccount))
    
    '''
    Delete a EFTBankAccount
    
    @param: EFTBankAccount 
    @return: Response Status
    @raise: IOException
    @raise: OptimalException
    '''
    
    def delete_eft_bank_account(self, data):
        profile_id = data.profile.id
        eft_bank_id = data.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.EFTBankAccount.EFTBankAccount, 
                                    "400", 
                                    err_msg))
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._EFT_BANK_PATH +\
                                    eft_bank_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="DELETE", 
                                                url=FULL_URL, 
                                                data=None)   
        return (self._process_response(response, CustomerVault.EFTBankAccount.EFTBankAccount))
    
    '''
    Create SEPA Bank Account
    
    @param: SEPABankAccount Object
    @return: SEPABankAccount Object
    @raise: IOException
    @raise: OptimalException
    '''
    
    def create_sepa_bank_account(self, data):
        profile_id = data.profile.id  
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.SEPABankAccount.SEPABankAccount, 
                                    "400", 
                                    err_msg))         
        del data.profile
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._SEPA_BANK_PATH)   
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST",
                                                url=FULL_URL,
                                                data=data)   
        return (self._process_response(response, CustomerVault.SEPABankAccount.SEPABankAccount))   
        
    '''
    Lookup a SEPA Bank Account
    
    @param: SEPABankAccount Id
    @return: SEPABankAccount object
    @raise exception: IOException
    @raise exception: OptimalException
    '''
    def lookup_sepa_bank_account(self, data):
        profile_id = data.profile.id  
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.SEPABankAccount.SEPABankAccount, 
                                    "400", 
                                    err_msg))         
        del data.profile
        
        sepa_bank_id = data.id
        if inspect.ismethod(sepa_bank_id):
            err_msg = "SEPA Bank Account Id not available"
            return (self.prepare_error(
                                    CustomerVault.SEPABankAccount.SEPABankAccount, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._SEPA_BANK_PATH + \
                                    sepa_bank_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)                
        return (self._process_response(response, CustomerVault.SEPABankAccount.SEPABankAccount))

    '''
    Update SEPABankAccount
    @param: SEPABankAccount object
    @return: SEPABankAccount object
    @raise: IOException
    @raise: OptimalException
    '''
    def update_sepa_bank_account(self, data):
        profile_id = data.profile.id
        sepa_bank_id = data.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.SEPABankAccount.SEPABankAccount, 
                                    "400", 
                                    err_msg))
        del data.profile
        
        if inspect.ismethod(sepa_bank_id):
            err_msg = "SEPA Bank Account Id not available"
            return (self.prepare_error(
                                    CustomerVault.SEPABankAccount.SEPABankAccount, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._SEPA_BANK_PATH +\
                                    sepa_bank_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="PUT", 
                                                url=FULL_URL, 
                                                data=data)      
        return (self._process_response(response, CustomerVault.SEPABankAccount.SEPABankAccount))

    '''
    Delete a SEPABankAccount
    
    @param:  SEPABankAccount 
    @return: Response Status
    @raise: IOException
    @raise: OptimalException
    '''
    
    def delete_sepa_bank_account(self, data):
        profile_id = data.profile.id
        sepa_bank_id = data.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.SEPABankAccount.SEPABankAccount, 
                                    "400", 
                                    err_msg))
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._SEPA_BANK_PATH +\
                                    sepa_bank_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="DELETE", 
                                                url=FULL_URL, 
                                                data=None)   
        return (self._process_response(response, CustomerVault.SEPABankAccount.SEPABankAccount))

    '''
    Create Mandates for BACS Bank Account
    
    @param: Mandates Object
    @return: Mandates Object
    @raise: IOException
    @raise: OptimalException
    '''
    def create_mandates_bacs_bank(self, data):
        profile_id = data.profile.id
        bacs_bank_id = data.bacs.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Mandates.Mandates, 
                                    "400", 
                                    err_msg))
        del data.profile
        
        if inspect.ismethod(bacs_bank_id):
            err_msg = "BACS Bank Account Id not available"
            return (self.prepare_error(
                                    CustomerVault.Mandates.Mandates, 
                                    "400", 
                                    err_msg))
        del data.bacs
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH +\
                                    profile_id +\
                                    self._BACS_BANK_PATH +\
                                    bacs_bank_id +\
                                    self._MANDATES_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST",
                                                url=FULL_URL,
                                                data=data)   
        return (self._process_response(response, CustomerVault.Mandates.Mandates))
    
    '''
    Create Mandates for SEPA Bank Account
    
    @param: Mandates Object
    @return: Mandates Object
    @raise: IOException
    @raise: OptimalException
    '''
    def create_mandates_sepa_bank(self, data):
        profile_id = data.profile.id
        sepa_bank_id = data.sepa.id
        
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Mandates.Mandates, 
                                    "400", 
                                    err_msg))
        del data.profile
        
        if inspect.ismethod(sepa_bank_id):
            err_msg = "SEPA Bank Account Id not available"
            return (self.prepare_error(
                                    CustomerVault.Mandates.Mandates, 
                                    "400", 
                                    err_msg))
        del data.sepa
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH +\
                                    profile_id +\
                                    self._SEPA_BANK_PATH +\
                                    sepa_bank_id +\
                                    self._MANDATES_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST",
                                                url=FULL_URL,
                                                data=data)  
        
        return (self._process_response(response, CustomerVault.Mandates.Mandates))
        
    '''
    Lookup a Mandates
    
    @param: Mandates 
    @return: Mandates object
    @raise exception: IOException
    @raise exception: OptimalException
    '''
    def lookup_mandates(self, data):
        profile_id = data.profile.id      
        mandates_id = data.id
        if inspect.ismethod(mandates_id):
            err_msg = "Mandates Id not available"
            return (self.prepare_error(
                                    CustomerVault.Mandates.Mandates, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH +\
                                    profile_id +\
                                    self._MANDATES_PATH + \
                                    self._URI_SEPARATOR +\
                                    mandates_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)                
        return (self._process_response(response, CustomerVault.Mandates.Mandates))
        
    '''
    Update a Mandates
    
    @param: Mandates object
    @return: Mandates object
    @raise: IOException
    @raise: OptimalException
    '''
    def update_mandates(self, data):
        profile_id = data.profile.id
        mandates_id = data.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Mandates.Mandates, 
                                    "400", 
                                    err_msg))
        del data.profile
        
        if inspect.ismethod(mandates_id):
            err_msg = "Mandates Id not available"
            return (self.prepare_error(
                                    CustomerVault.Mandates.Mandates, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._MANDATES_PATH +\
                                    self._URI_SEPARATOR +\
                                    mandates_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="PUT", 
                                                url=FULL_URL, 
                                                data=data)      
        return (self._process_response(response, CustomerVault.Mandates.Mandates))
        
    '''
    Delete a Mandates
    
    @param:  Mandates 
    @return: Response Status
    @raise: IOException
    @raise: OptimalException
    '''
    def delete_mandates(self, data):
        profile_id = data.profile.id
        mandates_id = data.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Mandates.Mandates, 
                                    "400", 
                                    err_msg))
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                    profile_id + \
                                    self._MANDATES_PATH +\
                                    self._URI_SEPARATOR +\
                                    mandates_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="DELETE", 
                                                url=FULL_URL, 
                                                data=None)   
        return (self._process_response(response, CustomerVault.Mandates.Mandates))