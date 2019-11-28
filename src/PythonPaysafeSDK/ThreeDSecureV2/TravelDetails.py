from PythonPaysafeSDK.common.DomainObject import DomainObject
class TravelDetails(DomainObject):
    '''
    classdocs
    '''
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['isAirTravel'] = self.isAirTravel
        handler['departureDate'] = self.departureDate
        handler['passengerFirstName']=self.passengerFirstName
        handler['passengerLastName']=self.passengerLastName
        handler['origin']=self.origin
        handler['destination']=self.destination
        handler['airlineCarrier']=self.airlineCarrier
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
    '''
    Property isAirTravel
    '''
    def isAirTravel(self,isAirTravel):
        self.__dict__['isAirTravel'] = isAirTravel

    '''
    Property departureDate
    '''
    def departureDate(self,departureDate):
        self.__dict__['departureDate'] = departureDate

    '''
    Property passengerFirstName
    '''
    def passengerFirstName(self,passengerFirstName):
        self.__dict__['passengerFirstName'] = passengerFirstName

    '''
    Property passengerLastName
    '''
    def passengerLastName(self,passengerLastName):
        self.__dict__['passengerLastName'] = passengerLastName

    '''
    Property origin
    '''
    def origin(self,origin):
        self.__dict__['origin'] = origin

    '''
    Property destination
    '''
    def destination(self,destination):
        self.__dict__['destination'] = destination

    '''
    Property airlineCarrier
    '''
    def airlineCarrier(self,airlineCarrier):
        self.__dict__['airlineCarrier'] = airlineCarrier