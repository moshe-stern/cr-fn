from datetime import datetime

from dateutil.relativedelta import relativedelta

from src.classes.api import API
from src.classes.session import CRSession


def get_appointments(session: CRSession, client_id: int):
    current_date = datetime.now().strftime("%m/%d/%Y")
    current_date_plus_one_year = (datetime.now() + relativedelta(years=1)).strftime(
        "%m/%d/%Y"
    )
    return session.post(
        url=API.SCHEDULE.GET_APPOINTMENTS,
        json={
            "contactId": client_id,
            "viewType": "overview",
            "startDate": current_date,
            "endDate": current_date_plus_one_year,
            "page": 1,
            "pageSize": 20,
            "_utcOffsetMinutes": 300,
        },
    ).json()["items"]


def load_events(course_id):
    print(API.SCHEDULE.LOAD_EVENTS)


def update_events(course_id):
    print(API.SCHEDULE.UPDATE_EVENTS)
