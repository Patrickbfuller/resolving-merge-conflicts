class Snake:
    """A dangerous and/or harmless serpent."""
    pass


class Cobra(Snake):
    """Definitely dangerous, yup."""
    
    def__init__(self, fang_size):
        self.fang_size = fang_size
    
    def bite(self, other):
        """Deliver a dose of venom."""
        
        other.injury += self.fang_size

    
class BoaConstrictor(Snake):
    """This one gives really good hugs."""
    
    def squeeze(self, other):
        """Give a hug. Seems innocent at first..."""
        if self.size:
            other.injury += self.size

    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""

    def __init__(self):
        """Create a new BoatConstrictor"""
        super().__init__()
        self.size = "enormous"
