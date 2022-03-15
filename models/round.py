
from pydantic import BaseModel, validator
from datetime import datetime
from pydantic.types import PositiveInt, constr
from typing import List
from models.match import Match


class Round(BaseModel):
    name: constr(strict=True, min_length=2, max_length=10)
    start_date: datetime = datetime.today()
    end_date: datetime = None
    matchs: List[Match] = []     