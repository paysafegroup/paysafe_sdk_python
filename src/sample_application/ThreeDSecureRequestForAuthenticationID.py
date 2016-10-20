#!/usr/bin/env python3
'''
Created on 1-June-2016

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.CardPayments.Card import Card
from PythonPaysafeSDK.CardPayments.CardExpiry import CardExpiry
from PythonPaysafeSDK.PaysafeApiClient import PaysafeApiClient
from PythonPaysafeSDK.ThreeDSecure.Authentications import Authentications
from PythonPaysafeSDK.ThreeDSecure.EnrollmentChecks import EnrollmentChecks
from utils.Utils import Utils

from Config import Config
from RandomTokenGenerator import RandomTokenGenerator


optimal_obj = PaysafeApiClient(Config.api_key, Config.api_password, Config.environment, Config.account_number)
# Submit Enrollment Request
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

# Submit Authentications Request
authentications_Obj = Authentications(None)
authentications_Obj.merchantRefNum(RandomTokenGenerator().generateToken())
authentications_Obj.paRes("eJxVUstuwjAQ/BXEvbGd+JGgxVJaDgUJREtbtVyi4FgQtQngJDz+vnYI0N52PJ717Kzhb"+\
"WO0Hi20aoyWMNVVla51L8+GffN9xh72SKJW6+pgihqThFAeUCyikCZC+IGfEE76Eubxq95LOGhT5dtSEivzAV2h7WrU"+\
"Ji1rCanaP45nkkZ+hDGgDkKhzXgkeUjCiFrhBUKZFlpm+qB0WRv9QCgJOYtCLqhgzKpbHtS2sfRZhj4HdAXQmB+5qetdN"+\
"UDoeDx6RWfBU9sCkGMB3W3NG1dVttspz+SXPylVsDyvPl+O00W8VrN39kGXkziOh4DcDcjSWksfE44Z4T1CByQYYAq"+\
"oPYe0cDYks/G5IS8Idu6R+Eo55u8J2AUYXSo7CLXUDYE+7balTUDaYG41oLvlp2eXq6ptZJRgETIhmMAs4KJNuCVcl9zmY"+\
"i3jto0DgJwUdctD3e5t9e9P/AK4GK/3")
                
enrollment_Obj2 = EnrollmentChecks(None)
enrollment_Obj2.id(response_object.id)
authentications_Obj.enrollmentchecks(enrollment_Obj2)

response_object2 = optimal_obj.three_d_secure_service_handler().submit_purchase_authentications(authentications_Obj)



print ("\nResponse Values ==========> ")
Utils.print_response(response_object2)

