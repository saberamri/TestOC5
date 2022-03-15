from typing import List, Tuple
from view import View


class Form(View):
    """
    enter the equivalent data of a model: player, match, tournaments
    Args:
        View (class): parent class
    """
    def __init__(self, title: str, fields: List[Tuple[str, str]]):
        """constructor
        Args:
        - title (str): form title
        - fields (List[Tuple[str, str]]): list of fields to  fill:  tuple of two: 
        the description (desc) of the field in French (value given by the  user in input)  
        and  the  name of the field (field) stored in the database.
        """
        self.fields = fields
        super().__init__(title)

    def show(self):
        """
        - show title
        - ask for fields to fill in
        Returns:
            data(dict): data dictionary filled with their real fields 
            stored in the database
        """
        data = {}
        super().show()
        for desc, field in self.fields:
            data[field] = input(desc + " ? ")
        return data
