'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''


class DomainObject(dict):

    def __init__(self):
        '''
        constructor
        '''
    
    def setProperties(self, obj, handler=None):
        for key in obj.keys():
            try:
                if isinstance(obj[key], dict):
                    handler[key](obj[key])
                elif isinstance(obj[key], list):
                    handler[key](obj[key])
                else:
                    self.__dict__[key] = obj[key]
            except KeyError:
                # Set key as None
                print("Keyerror for key =", key)
                self.__dict__[key] = None
                continue
            except AttributeError:
                print("AttributeError for key =", key)
                # Set key as None
                self.__dict__[key] = None
                continue