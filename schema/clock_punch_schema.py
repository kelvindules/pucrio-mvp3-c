from pydantic import BaseModel

class RegisterClockPunchSchema(BaseModel):
    username: str
    token: str

class GetClockPunchesSchema(BaseModel):
    username: str

class DeleteClockPunchSchema(BaseModel):
    id: int