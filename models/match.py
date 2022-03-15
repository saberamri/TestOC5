from pydantic import BaseModel, validator
from datetime import date
from pydantic.types import PositiveInt


class Match(BaseModel):
    player1_id: PositiveInt
    player2_id: PositiveInt
    score_player1: float = None

    @property
    def score_player2(self):
	"""
		c'est comme un Attribut: C'est un getter qu'on devra le mettre pendant l'initialisation de la classe
		et qui permet d'accéder et d'afficher l'attribut en lecture seule. il est calculé automatiquement en 
		fonction de score_player1 mais n'est pas du tout stoké. 
    """
        return 1.0 - self.score_player1

    @score_player2.setter
    def score_player2(self, value):
        self.score_player1 = 1.0 - value