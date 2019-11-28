from PythonPaysafeSDK.common.DomainObject import DomainObject
class Profile(DomainObject):
    def __init__(self,obj):
        '''
        Constructor
        '''
        #Handler dictionary
        handler = dict()
        handler['cellphone'] = self.cellphone
        handler['email']=self.email
        handler['phone']=self.phone
      
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
    '''
    Property cellphone
    '''
    def cellphone(self,cellphone):
        self.__dict__['cellphone'] = cellphone

    '''
    Property email
    '''
    def email(self,email):
        self.__dict__['email'] = email

    '''
    Property phone
    '''
    def phone(self,phone):
        self.__dict__['phone'] = phone