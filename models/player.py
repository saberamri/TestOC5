
from pydantic import BaseModel, validator
from datetime import date, timedelta
from pydantic.types import (
    PositiveInt,
    conint,
    constr
)


from datetime import date
from enum import Enum


class Gender(Enum):
	"""
	Gender est une classe qui hérite de la classe Eum.
	Enum est un module python de base intégré au language
	elle va énumérer les valeurs de la variable gender.

	"""
    Male = 'H'
    Female = 'F'


class Player(BaseModel):
	"""
	La classe Player() hérite de la classe BaseModel()
	Cette classe contient les attributs et méthodes de l'utilisateur joueur.

	"""
    id: PositiveInt
    rank: conint(strict=True, gt=0, le=3000)
    last_name: constr(strict=True, min_length=2, max_length=20)
    birth_date: date
    first_name: constr(strict=True, min_length=2, max_length=20)
    gender: Gender

    @validator('birth_date')
    def check_age(cls, v):
    	"""vérifier l'age légale du joueur"""
        age = (date.today() - v) // timedelta(days=365.2425)
        if age < 18:
            raise ValueError('age must be > 18')
        return v