from hybrid.element import Element




class Details(Element):
    """Represents the <details> tag"""
    def __init__(self, open=None):
        super().__init__('details', open=open)
