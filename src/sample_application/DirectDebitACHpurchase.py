#!/usr/bin/env python3
'''
Created on 1-June-2016

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.CardPayments.BillingDetails import BillingDetails
from PythonPaysafeSDK.CustomerVault.ACHBankAccount import ACHBankAccount
from PythonPaysafeSDK.CustomerVault.Profile import Profile
from PythonPaysafeSDK.DirectDebit.Purchase import Purchase
from PythonPaysafeSDK.PaysafeApiClient import PaysafeApiClient
from utils.Utils import Utils

from Config import Config
from RandomTokenGenerator import RandomTokenGenerator


optimal_obj = PaysafeApiClient(Config.api_key, Config.api_password, Config.environment, Config.account_number)

purchase_obj = Purchase(None)
purchase_obj.merchantRefNum(RandomTokenGenerator().generateToken())
purchase_obj.amount(100.98 * Config.currency_base_units_multiplier)
purchase_obj.customerIp("192.0.126.111")

achbank_obj = ACHBankAccount (None)
achbank_obj.accountHolderName("XYZ Company")
achbank_obj.accountType("CHECKING")
#achbank_obj.accountNumber(RandomTokenGenerator().generateNumber())
achbank_obj.accountNumber("988948193")
achbank_obj.routingNumber("211589828")
achbank_obj.payMethod("WEB")

profile_obj = Profile(None)
profile_obj.firstName("Joe")
profile_obj.lastName("Smith")
profile_obj.email("Joe.Smith@hotmail.com")

billingdetails_obj = BillingDetails(None)
billingdetails_obj.street("100 Queen Street West")
billingdetails_obj.city("Los Angeles")
billingdetails_obj.state("CA")
billingdetails_obj.country("US")
billingdetails_obj.zip("90210")
billingdetails_obj.phone("3102649010")

purchase_obj.profile(profile_obj)
purchase_obj.billingDetails(billingdetails_obj)
purchase_obj.ach(achbank_obj)

response_object = optimal_obj.direct_debit_service_handler().submit_purchase(purchase_obj)

print ("\nResponse Values ==========> ")
Utils.print_response(response_object)

