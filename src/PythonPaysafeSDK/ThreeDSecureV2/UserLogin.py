from PythonPaysafeSDK.common.DomainObject import DomainObject
class UserLogin(DomainObject):
    '''
    classdocs
    '''

    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['data'] = self.data
        handler['authenticationMethod'] = self.authenticationMethod
        handler['time'] = self.time
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
    '''
    Property data
    '''
    def data(self,data):
        self.__dict__['data'] = data

    '''
    Property authenticationMethod
    '''
    def authenticationMethod(self,authenticationMethod):
        self.__dict__['authenticationMethod'] = authenticationMethod

    '''
    Property time
    '''
    def time(self,time):
        self.__dict__['time'] = time