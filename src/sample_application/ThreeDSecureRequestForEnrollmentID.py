#!/usr/bin/env python3
'''
Created on 1-June-2016

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.CardPayments.Card import Card
from PythonPaysafeSDK.CardPayments.CardExpiry import CardExpiry
from PythonPaysafeSDK.PaysafeApiClient import PaysafeApiClient
from PythonPaysafeSDK.ThreeDSecure.EnrollmentChecks import EnrollmentChecks
from utils.Utils import Utils

from Config import Config
from RandomTokenGenerator import RandomTokenGenerator


optimal_obj = PaysafeApiClient(Config.api_key, Config.api_password, Config.environment, Config.account_number)
enrollment_Obj = EnrollmentChecks(None)
enrollment_Obj.merchantRefNum(RandomTokenGenerator().generateToken())
enrollment_Obj.amount(50 * Config.currency_base_units_multiplier)
enrollment_Obj.currency(Config.currency_code)
enrollment_Obj.customerIp("172.0.0.1")
enrollment_Obj.userAgent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36")
enrollment_Obj.acceptHeader("text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
enrollment_Obj.merchantUrl("https://www.merchant.com")
            
card_Obj = Card(None)
card_Obj.cardNum("4107857757053670")
            
card_Expiry_Obj = CardExpiry(None)
card_Expiry_Obj.month("10")
card_Expiry_Obj.year("2020")
            
card_Obj.cardExpiry(card_Expiry_Obj)
enrollment_Obj.card(card_Obj)
            
response_object = optimal_obj.three_d_secure_service_handler().submit_purchase_enrollment(enrollment_Obj)

print ("\nResponse Values ==========> ")
Utils.print_response(response_object)

