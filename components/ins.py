from hybrid.element import Element




class Ins(Element):
    """Represents the <ins> tag"""
    def __init__(
            self, 
            cite, 
            datetime
        ):
        super().__init__('ins', )