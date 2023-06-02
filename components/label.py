from hybrid.element import Element







class Label(Element):
    """Represents the <label> tag"""
    def __init__(
            self, 
            for_
        ):
        super().__init__('label', )
