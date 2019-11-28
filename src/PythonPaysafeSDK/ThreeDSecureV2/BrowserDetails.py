from PythonPaysafeSDK.common.DomainObject import DomainObject
class BrowserDetails(DomainObject):
    '''
    classdocs
    '''
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['javaEnabled'] = self.javaEnabled
        handler['javascriptEnabled'] = self.javascriptEnabled
        handler['language'] = self.language
        handler['colorDepthBits']=self.colorDepthBits
        handler['screenHeight']=self.screenHeight
        handler['screenWidth']=self.screenWidth
        handler['timezoneOffset']=self.timezoneOffset
        handler['userAgent']=self.userAgent
        handler['acceptHeader']=self.acceptHeader
        handler['customerIp']=self.customerIp
        
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
    '''
    Property javaEnabled
    '''
    def javaEnabled(self,javaEnabled):
        self.__dict__['javaEnabled'] = javaEnabled
    
    '''
    Property javascriptEnabled
    '''
    def javascriptEnabled(self,javascriptEnabled):
        self.__dict__['javascriptEnabled'] = javascriptEnabled

    '''
    Property language
    '''
    def language(self,language):
        self.__dict__['language'] = language

    '''
    Property colorDepthBits
    '''
    def colorDepthBits(self,colorDepthBits):
        self.__dict__['colorDepthBits'] = colorDepthBits

    '''
    Property screenHeight
    '''
    def screenHeight(self,screenHeight):
        self.__dict__['screenHeight'] = screenHeight

    '''
    Property screenWidth
    '''
    def screenWidth(self,screenWidth):
        self.__dict__['screenWidth'] = screenWidth

    '''
    Property timezoneOffset
    '''
    def timezoneOffset(self,timezoneOffset):
        self.__dict__['timezoneOffset'] = timezoneOffset

    '''
    Property userAgent
    '''
    def userAgent(self,userAgent):
        self.__dict__['userAgent'] = userAgent

    '''
    Property acceptHeader
    '''
    def acceptHeader(self,acceptHeader):
        self.__dict__['acceptHeader'] = acceptHeader

    '''
    Property customerIp
    '''
    def customerIp(self,customerIp):
        self.__dict__['customerIp'] = customerIp   