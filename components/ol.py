from hybrid.element import Element







class Ol(Element):
    """Represents the <ol> tag"""
    def __init__(
            self, 
            reversed, 
            start, 
            type
        ):
        super().__init__('ol', )