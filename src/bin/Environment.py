'''
Created on 30-Jan-2015

@author: Asawari.Vaidya
'''

import certifi
from urllib3.connectionpool import HTTPSConnectionPool
from urllib3.util.timeout import Timeout


class Environment:
    '''
    classdocs
    '''
    
    def __init__(self, host_url, max_connections, pool_enable, 
                 connection_timeout, read_timeout):
        '''
        Constructor
        '''
        if connection_timeout is None:
            connection_timeout = 30
        if read_timeout is None:
            read_timeout = 30
        
        
        self._host_url = host_url
        self._pool = HTTPSConnectionPool(host_url, 
                                         maxsize=max_connections, 
                                         block=pool_enable,
                                         timeout=Timeout(
                                                    connect=connection_timeout, 
                                                    read=read_timeout),
                                         retries=False,
                                         cert_reqs='CERT_REQUIRED',
                                         ca_certs=certifi.where())
        
    @classmethod
    def _get_env(self, params_env):
        self._params_env = params_env 
        if self._params_env == 'TEST':
            return environment_url['TEST']
        if self._params_env == 'LIVE':
            return environment_url['LIVE']

# Class Object      
environment_url = dict()
environment_url['TEST'] = Environment('api.test.paysafe.com', 10, True, 
                                      connection_timeout=30, read_timeout=30)
environment_url['LIVE'] = Environment('api.paysafe.com', 10, True, 
                                      connection_timeout=30, read_timeout=30)