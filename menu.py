from typing import List
from view import View


class Menu(View):
    """The Menu class contains two attrributes:
    - title
    - options  
    and contain a show class method overloaded from the parent class view().

    Args:
        View (class): parent class
    """
    
    def __init__(self, title:str, options:List[str]):
        """constructor
        Args:
            title (str): title
            options (List[str]): options list
        """
        content = "\n".join([f"{i}. {option}"for i, option in enumerate(options, start=1)])
        self.options = options
        super().__init__(title= title, content=content)

    def show(self):
        """
        - show title
        - ask the user to enter a numeric choice between 1 and len(options)
        Returns:
            choice(int): choice returned by the user
        """
        while True:
            super().show()
            choice = int(input(": "))
            if choice in range(1,len(self.options) + 1):
                try:
                    return choice
                except ValueError:
                    print("renouvelez votre choix de nouveau")