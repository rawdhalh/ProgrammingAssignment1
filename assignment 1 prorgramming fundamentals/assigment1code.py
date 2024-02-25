from enum import Enum


class User:
    """Class to represent a user"""

    # Enum for gender
    class Gender(Enum):
        MALE = "Male"
        FEMALE = "Female"

    # Constructor
    def __init__(self, userEmail, userPass, gender, userID, userName):
        self.__userEmail = userEmail
        self.__userPass = userPass
        self.__gender = gender
        self.__userID = userID
        self.__userName = userName

    # Setter and Getter methods for all attributes
    def setUserEmail(self, userEmail):
        self.__userEmail = userEmail

    def getUserEmail(self):
        return self.__userEmail

    def setUserPass(self, userPass):
        self.__userPass = userPass

    def getUserPass(self):
        return self.__userPass

    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender

    def setUserID(self, userID):
        self.__userID = userID

    def getUserID(self):
        return self.__userID

    def setUserName(self, userName):
        self.__userName = userName

    def getUserName(self):
        return self.__userName


class SpecialService:
    """Class to represent a special service"""

    # Enum for serviceType
    class ServiceType(Enum):
        MEAL_PREFERENCE = "Meal Preference"
        WHEELCHAIR = "Wheelchair"
        EXTRA_LEG_ROOM = "Extra Leg Room"
        EXTRA_CARRYON_SPACE = "Extra Carryon Space"

    # Constructor
    def __init__(self, serviceType, additionalDetails, serviceID, serviceName, serviceCost):
        self.__serviceType = serviceType
        self.__additionalDetails = additionalDetails
        self.__serviceID = serviceID
        self.__serviceName = serviceName
        self.__serviceCost = serviceCost

    # Setter and Getter methods for all attributes
    def setServiceType(self, serviceType):
        self.__serviceType = serviceType

    def getServiceType(self):
        return self.__serviceType

    def setAdditionalDetails(self, additionalDetails):
        self.__additionalDetails = additionalDetails

    def getAdditionalDetails(self):
        return self.__additionalDetails

    def setServiceID(self, serviceID):
        self.__serviceID = serviceID

    def getServiceID(self):
        return self.__serviceID

    def setServiceName(self, serviceName):
        self.__serviceName = serviceName

    def getServiceName(self):
        return self.__serviceName

    def setServiceCost(self, serviceCost):
        self.__serviceCost = serviceCost

    def getServiceCost(self):
        return self.__serviceCost


class BoardingPass:
    """Class to represent a boarding pass"""

    # Constructor
    def __init__(self, passName, fromDest, seatNum, gate, date, toDest, flightNum, terminal, boardingTime, seatClass,
                 electronicTicket, arrivalTime):
        self.__passName = passName
        self.__fromDest = fromDest
        self.__seatNum = seatNum
        self.__gate = gate
        self.__date = date
        self.__toDest = toDest
        self.__flightNum = flightNum
        self.__terminal = terminal
        self.__boardingTime = boardingTime
        self.__seatClass = seatClass
        self.__electronicTicket = electronicTicket
        self.__arrivalTime = arrivalTime

    # Setter and Getter methods for all attributes
    def setPassName(self, passName):
        self.__passName = passName

    def getPassName(self):
        return self.__passName

    def setFromDest(self, fromDest):
        self.__fromDest = fromDest

    def getFromDest(self):
        return self.__fromDest

    def setSeatNum(self, seatNum):
        self.__seatNum = seatNum

    def getSeatNum(self):
        return self.__seatNum

    def setGate(self, gate):
        self.__gate = gate

    def getGate(self):
        return self.__gate

    def setDate(self, date):
        self.__date = date

    def getDate(self):
        return self.__date

    def setToDest(self, toDest):
        self.__toDest = toDest

    def getToDest(self):
        return self.__toDest

    def setFlightNum(self, flightNum):
        self.__flightNum = flightNum

    def getFlightNum(self):
        return self.__flightNum

    def setTerminal(self, terminal):
        self.__terminal = terminal

    def getTerminal(self):
        return self.__terminal

    def setBoardingTime(self, boardingTime):
        self.__boardingTime = boardingTime

    def getBoardingTime(self):
        return self.__boardingTime

    def setSeatClass(self, seatClass):
        self.__seatClass = seatClass

    def getSeatClass(self):
        return self.__seatClass

    def setElectronicTicket(self, electronicTicket):
        self.__electronicTicket = electronicTicket

    def getElectronicTicket(self):
        return self.__electronicTicket

    def setArrivalTime(self, arrivalTime):
        self.__arrivalTime = arrivalTime

    def getArrivalTime(self):
        return self.__arrivalTime


class Airport:
    """Class to represent an airport"""

    # Constructor
    def __init__(self, airportName, airportLoc, airportCode, numTerminals, numGates):
        self.__airportName = airportName
        self.__airportLoc = airportLoc
        self.__airportCode = airportCode
        self.__numTerminals = numTerminals
        self.__numGates = numGates

    # Setter and Getter methods for all attributes
    def setAirportName(self, airportName):
        self.__airportName = airportName

    def getAirportName(self):
        return self.__airportName

    def setAirportLoc(self, airportLoc):
        self.__airportLoc = airportLoc

    def getAirportLoc(self):
        return self.__airportLoc

    def setAirportCode(self, airportCode):
        self.__airportCode = airportCode

    def getAirportCode(self):
        return self.__airportCode

    def setNumTerminals(self, numTerminals):
        self.__numTerminals = numTerminals

    def getNumTerminals(self):
        return self.__numTerminals

    def setNumGates(self, numGates):
        self.__numGates = numGates

    def getNumGates(self):
        return self.__numGates

# Create an object for each class

# Create User object
user = User("rawdha@gmail.com", "rawdh128472", User.Gender.FEMALE, "AU18239", "rawdhalh")

# Create SpecialService object
service = SpecialService(SpecialService.ServiceType.MEAL_PREFERENCE, "Vegetarian", "S2718", "Meal Preference", 15.99)

# Create BoardingPass object
boarding_pass = BoardingPass("Rawdha AlHarmoodi", "Abu Dhabi, UAE", "A23", "B4", "2024-02-25", "Milan, Italy", "Fl2894", "Terminal 4", "12:00 AM", "Business", "ET7627", "10:30 PM")

# Create Airport object
airport = Airport("Zayed International Airport", "Abu Dhabi, UAE", "AE", 10, 50)

# Displaying the boarding pass details

print("Boarding Pass Details:")
print("Passenger Name:", boarding_pass.getPassName())
print("From:", boarding_pass.getFromDest())
print("To:", boarding_pass.getToDest())
print("Date:", boarding_pass.getDate())
print("Flight Number:", boarding_pass.getFlightNum())
print("Gate:", boarding_pass.getGate())
print("Terminal:", boarding_pass.getTerminal())
print("Boarding Time:", boarding_pass.getBoardingTime())
print("Seat Class:", boarding_pass.getSeatClass())
print("Electronic Ticket:", boarding_pass.getElectronicTicket())
print("Arrival Time:", boarding_pass.getArrivalTime())
