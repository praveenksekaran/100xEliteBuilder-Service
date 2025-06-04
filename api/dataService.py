from datetime import datetime
from pydantic import BaseModel

class Challenge(BaseModel):
    sponsor_id: int
    status_id: int
    title: str
    overview: str
    problem_statement: str       
    start_date: datetime
    close_date: datetime
    scope_exclusions: str
    guidlines: str
    uploads: str
    rewards_id: int
    appType_id: int
    win_declare_date: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

'''status: str = "open"
sponsor_id: Optional[int] = None '''

class Rewards(BaseModel):
    reward_type_id:int
    sponsor_id:int
    description:str
    value:float

class ChallengeAll(BaseModel):
    sponsor_id: int
    status_id: int
    title: str
    overview: str
    problem_statement: str       
    start_date: datetime
    close_date: datetime
    scope_exclusions: str
    guidlines: str
    uploads: str   
    appType_id: int
    win_declare_date: datetime
    reward_type_id:int  
    description:str
    value:float

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
    