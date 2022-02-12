

from pydantic import BaseModel, validator
from datetime import datetime
from pydantic.types import PositiveInt, constr
from typing import List
from enum import Enum

from models.round import Round


class TimeControl(Enum):
    Blitz = 1
    Bullet = 2
    Fast = 3


class Tournament(BaseModel):
    number_of_rounds: PositiveInt = 4
    players: List[PositiveInt]
    description: constr(strict=True, max_length=50) = ""
    name: constr(strict=True, max_length=20, min_length=6)
    start_date: datetime = datetime.today()
    end_date: datetime = None
    place: constr(strict=True, max_length=50, min_length=3)
    time_control: TimeControl
    rounds: List[Round] = []