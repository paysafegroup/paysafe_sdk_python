#!/usr/bin/env python3
'''
Created on 1-Apr-2015

@author: Asawari.Vaidya
'''
import cgi
import cgitb

from PythonPaysafeSDK.CardPayments.Authorization import Authorization
from PythonPaysafeSDK.CardPayments.BillingDetails import BillingDetails
from PythonPaysafeSDK.CardPayments.Card import Card
from PythonPaysafeSDK.CardPayments.CardExpiry import CardExpiry
from PythonPaysafeSDK.PaysafeApiClient import PaysafeApiClient

from Config import Config
from RandomTokenGenerator import RandomTokenGenerator


cgitb.enable()
#from sample_application.RandomTokenGenerator import RandomTokenGenerator
#from sample_application.Config import Config

form = cgi.FieldStorage()
card_num = form.getvalue('cardNumber')

optimal_obj = PaysafeApiClient(Config.api_key, Config.api_password, Config.environment, Config.account_number)

auth_obj = Authorization(None)
card_obj = Card(None)
cardExpiry_obj = CardExpiry(None)
billing_obj = BillingDetails(None)
		
auth_obj.merchantRefNum(RandomTokenGenerator().generateToken())
auth_obj.amount(10 * Config.currency_base_units_multiplier)
auth_obj.settleWithAuth("false")

#card_obj.cardNum("4530910000012345")		
card_obj.cardNum(card_num)
card_obj.cvv("123")
auth_obj.card(card_obj)
		
cardExpiry_obj.month("2")
cardExpiry_obj.year("2017")
card_obj.cardExpiry(cardExpiry_obj)

billing_obj.street("Carlos Pellegrini 551")
billing_obj.city("Buenos Aires")
billing_obj.state("Zulia")
billing_obj.country("AR")
billing_obj.zip("C1009ABK")
auth_obj.billingDetails(billing_obj)

response_object = optimal_obj.card_payments_service_handler().create_authorization(auth_obj)

print ('Content-Type: text/html')
print ()
print ('<html>')
print ('<head><title>Card Payments - Create Authorization</title></head>')
print ('<body>')
print (response_object.__dict__)
print (response_object.error.__dict__)
print ('</body></html>')
