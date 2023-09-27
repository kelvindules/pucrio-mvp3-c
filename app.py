from flask import request, jsonify
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag

from datetime import datetime

from schema.clock_punch_schema import *

from service import auth, clock_punch_service

app_info = Info(title="Clock Punch API", version="1.0.0")
app = OpenAPI(__name__, info=app_info)
CORS(app)

clock_punch_tag = Tag(name="Clock Punch", description="User's Clock Punch Flows")


def str_to_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").date()


@app.post("/clock-punches", tags=[clock_punch_tag])
def post_clock_punch():
    form = request.get_json()
    username = form["username"]
    token = form["token"]

    token_validation = auth.get_token_validation(token)

    if auth.validate_token(username, token_validation):
        return clock_punch_service.register(
            RegisterClockPunchSchema(username=username, token=token)
        )
    else:
        return {"message": "Bad username/token combination"}, 401


@app.get("/clock-punches/<string:username>", tags=[clock_punch_tag])
def get_clock_punches(path: GetClockPunchesSchema):
    token = request.headers["Authorization"].split(" ")[0]
    now = datetime.now()
    today = datetime(now.year, now.month, now.day)

    from_date = request.args.get("fromDate", default=today, type=str_to_date)
    to_date = request.args.get("toDate", default=today, type=str_to_date)

    token_validation = auth.get_token_validation(token)

    if auth.validate_token(path.username, token_validation):
        punches = clock_punch_service.get_clock_punches(path.username, from_date, to_date)
        return jsonify(punches)
    else:
        return {"message": "Bad username/token combination"}, 401


@app.delete("/clock-punches/<int:id>", tags=[clock_punch_tag])
def delete_clock_punch(path: DeleteClockPunchSchema):
    token = request.headers["Authorization"].split(" ")[0]
    token_validation = auth.get_token_validation(token)

    clock_punch = clock_punch_service.get_clock_punch(path.id)

    if clock_punch is None:
        return {"message": "Clock punch not found"}, 404

    if auth.validate_token(clock_punch.username, token_validation):
        return clock_punch_service.delete_clock_punch(path.id)
    else:
        return {"message": "You can't perform this action"}, 401
