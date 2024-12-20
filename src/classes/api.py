BASE_URL = "https://members.centralreach.com/api/"


class AuthSettings:
    def __init__(self):
        self.LOAD_SETTINGS = f"{BASE_URL}?resources.loadresourceauthorizationsettings"
        self.LOAD_SETTING = f"{BASE_URL}?resources.loadresourceauthorizationsetting"
        self.DELETE = f"{BASE_URL}?resources.deleteresourceauthorizationsetting"
        self.SET_SETTING = f"{BASE_URL}?resources.setresourceauthorizationsetting"


class ServiceCodes:
    def __init__(self):
        self.GET = f"{BASE_URL}?resources.getservicecodes"
        self.GET_PLACES_OF_SERVICE = (
            "https://members.centralreach.com/crxapieks/placesofservice"
        )


class Authorization:
    def __init__(self):
        self.GET = f"{BASE_URL}?resources.setresourceauthorization"
        self.LOAD_AUTHS_CODES = f"{BASE_URL}?scheduling.loadauthsandcodes"


class Schedule:
    def __init__(self):
        self.GET_EVENT = f"{BASE_URL}?scheduling.loadevent"
        self.UPDATE_EVENT = f"{BASE_URL}?scheduling.updateevent"
        self.GET_APPOINTMENTS = f"{BASE_URL}?contacts.loadcontactappointments"


class API:
    AUTH_SETTINGS = AuthSettings()
    SERVICE_CODES = ServiceCodes()
    AUTHORIZATION = Authorization()
    SCHEDULE = Schedule()
