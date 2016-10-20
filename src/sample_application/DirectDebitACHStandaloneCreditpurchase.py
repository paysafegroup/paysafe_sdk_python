#!/usr/bin/env python3
'''
Created on 1-June-2016

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.CardPayments.BillingDetails import BillingDetails
from PythonPaysafeSDK.CustomerVault.ACHBankAccount import ACHBankAccount
from PythonPaysafeSDK.CustomerVault.Profile import Profile
from PythonPaysafeSDK.DirectDebit.StandaloneCredits import StandaloneCredits
from PythonPaysafeSDK.PaysafeApiClient import PaysafeApiClient
from utils.Utils import Utils

from Config import Config
from RandomTokenGenerator import RandomTokenGenerator


optimal_obj = PaysafeApiClient(Config.api_key, Config.api_password, Config.environment, Config.account_number)
standalone_Obj = StandaloneCredits(None)
standalone_Obj.merchantRefNum(RandomTokenGenerator().generateToken())
standalone_Obj.amount(100.98 * Config.currency_base_units_multiplier)
standalone_Obj.customerIp("192.0.126.111")

achbank_Obj = ACHBankAccount(None)
achbank_Obj.accountHolderName("XYZ Company")
achbank_Obj.accountType("CHECKING")
achbank_Obj.accountNumber("988758392")
achbank_Obj.routingNumber("211589828")
achbank_Obj.payMethod("PPD")

profile_Obj = Profile(None)
profile_Obj.firstName("Joe")
profile_Obj.lastName("Smith")
profile_Obj.email("Joe.Smith@hotmail.com")

billingdetails_Obj = BillingDetails(None)
billingdetails_Obj.street("100 Queen Street West")
billingdetails_Obj.city("Los Angeles")
billingdetails_Obj.state("CA")
billingdetails_Obj.country("US")
billingdetails_Obj.zip("90210")
billingdetails_Obj.phone("3102649010")

standalone_Obj.profile(profile_Obj)
standalone_Obj.billingDetails(billingdetails_Obj)
standalone_Obj.ach(achbank_Obj)

response_object = optimal_obj.direct_debit_service_handler().submit_standalone(standalone_Obj)

print ("\nResponse Values ==========> ")
Utils.print_response(response_object)

