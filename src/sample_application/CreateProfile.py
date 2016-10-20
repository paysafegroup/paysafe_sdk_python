#!/usr/bin/env python3
'''
Created on 1-Apr-2015

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.CustomerVault.Profile import Profile
from PythonPaysafeSDK.PaysafeApiClient import PaysafeApiClient

from Config import Config
from RandomTokenGenerator import RandomTokenGenerator


optimal_obj = PaysafeApiClient(Config.api_key, Config.api_password, Config.environment, Config.account_number)

profile_obj = Profile(None)
profile_obj.merchantCustomerId(RandomTokenGenerator().generateToken())
profile_obj.locale("en_US")
profile_obj.firstName("John")
profile_obj.lastName("Smith")
profile_obj.email("john.@smith@somedomain.com")
profile_obj.phone("713-444-5555")
           
response_object = optimal_obj.customer_vault_service_handler().create_profile(profile_obj)

print ('Content-Type: text/html')
print ()
print ('<html>')
print ('<head><title>Customer Vault - Create Customer Profile</title></head>')
print ('<body>')
print (response_object.__dict__)
print ('</body></html>')
