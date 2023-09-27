from schema.clock_punch_schema import RegisterClockPunchSchema
from model import Session, ClockPunch
from datetime import timedelta


def register(punch_request: RegisterClockPunchSchema):
    try:
        clock_punch = ClockPunch(punch_request.username, punch_request.token)

        session = Session()
        session.add(clock_punch)
        session.commit()
        return {"message": "Clock punched successfully"}, 200
    except Exception as e:
        print(e)
        return {"message": "There was a problem trying to punch the clock"}, 400


def get_clock_punches(username, from_date, to_date):
    try:
        session = Session()

        return (
            session.query(ClockPunch)
            .filter(
                ClockPunch.username == username,
                ClockPunch.created_at >= from_date,
                ClockPunch.created_at <= to_date + timedelta(hours=23, minutes=59, seconds=59, milliseconds=59),
            )
            .all()
        )
    except Exception as e:
        print(e)

def get_clock_punch(id) -> ClockPunch:
    try:
        session = Session()
        return session.query(ClockPunch).filter(ClockPunch.id == id).first()
    except Exception as e:
        print(e)

def delete_clock_punch(id):
    try:
        session = Session()
        session.query(ClockPunch).filter(ClockPunch.id == id).delete()
        session.commit()
        return {"message": f"Clock punch #{id} deleted"}, 200
    except Exception as e:
        print(e)