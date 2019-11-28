from PythonPaysafeSDK.common.DomainObject import DomainObject
class PriorThreeDSAuthentication(DomainObject):
    def __init__(self, obj):
        '''
        Constructor
        '''
        #Handler dictionary
        handler = dict()
        handler['data'] = self.data
        handler['method']=self.method
        handler['time']=self.time
        handler['id']=self.id
        
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
    Property method
    '''
    def method(self,method):
        self.__dict__['method'] = method

    '''
    Property time
    '''
    def time(self,time):
        self.__dict__['time'] = time

    '''
    Property Id
    '''
    def id(self,id):
        self.__dict__['id'] = id 
