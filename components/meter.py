from hybrid.element import Element




class Meter(Element):
    """Represents the <meter> tag"""
    def __init__(
            self, 
            form, 
            high, 
            low,
            max, 
            min, 
            optimum, 
            value 
        ):
        super().__init__('meter', )