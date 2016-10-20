'''
Created on Feb 25, 2015

@author: amol.mithari
'''

class Config(object):
    '''
    classdocs
    '''

    # for example: TEST/ LIVE 
    environment = "TEST"
    
    api_key = 'your-api-key'
    api_password = 'your-api-password'
    account_number = 'your-account-number'

    # for example: CAD 
    currency_code = "your-account-currency-code"
    
    # for example: 100 
    currency_base_units_multiplier = 100