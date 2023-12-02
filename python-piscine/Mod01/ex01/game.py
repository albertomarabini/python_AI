class GoTCharacter:
    """A class representing a Game of Thrones character."""

    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    @classmethod
    def create_class(cls, family_name, house_words):
        """
        Class factory pattern
        GoTCharacter.create_class("Stark", "Winter is Coming")
        if issubclass(Stark, GoTCharacter): true
        arya = Stark("Arya")
        print(arya.__class__.__name__)
        Stark
        print(arya.__class__.__bases__)
        (<class 'game.GoTCharacter'>,)
        """

        def init(self, first_name=None, is_alive=True):
            GoTCharacter.__init__(self, first_name, is_alive)
            self.family_name = family_name
            self.house_words = house_words

        def print_house_words(self):
            print(self.house_words)

        def die(self):
            self.is_alive = False

        return type(
            family_name,
            (cls,),
            {
                "__doc__": f"A class representing the {family_name} family.",
                "__init__": init,
                "print_house_words": print_house_words,
                "die": die
            }
        )
Stark = GoTCharacter.create_class("Stark", "Winter is Coming")