#!/usr/bin/env python3
'''
Created on 1-Apr-2015

@author: Asawari.Vaidya
'''
import cgi
import cgitb

from PythonPaysafeSDK.CustomerVault.Card import Card
from PythonPaysafeSDK.CustomerVault.Profile import Profile
from PythonPaysafeSDK.PaysafeApiClient import PaysafeApiClient
from PythonPaysafeSDK.common.CardExpiry import CardExpiry

from Config import Config


cgitb.enable()


form = cgi.FieldStorage()
profile_id = form.getvalue('profileId')
card_num = form.getvalue('cardNumber')

optimal_obj = PaysafeApiClient(Config.api_key, Config.api_password, Config.environment, Config.account_number)

card_obj = Card(None)
card_obj.nickName("John's corporate Visa")
card_obj.holderName("MR. JOHN SMITH")
card_obj.cardNum(card_num)
#card_obj.cardNum("4510150000000321")
card_obj.defaultCardIndicator("true")
card_exp_obj = CardExpiry(None)
card_exp_obj.month("12")
card_exp_obj.year("2019")
profile_obj = Profile(None)
profile_obj.id(profile_id)
#profile_obj.id("e17871ed-5430-4234-a6fb-f3c9ccf995cf")
card_obj.profile(profile_obj)
card_obj.cardExpiry(card_exp_obj)

response_object = optimal_obj.customer_vault_service_handler().create_card(card_obj)

print ('Content-Type: text/html')
print ()
print ('<html>')
print ('<head><title>Customer Vault - Create Customer Card</title></head>')
print ('<body>')
print (response_object.__dict__)
print ('</body></html>')
