from pydantic import BaseModel

class Observation(BaseModel):
    title: str
    code: str
    goal: str
