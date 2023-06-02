from hybrid.element import Element



class Fieldset(Element):
    """Represents the <fieldset> tag"""
    def __init__(
            self, 
            disabled, 
            form, 
            name
        ):
        super().__init__('fieldset',disabled, 
            form, 
            name )
