from hybrid.element import Element




class Portal(Element):
    """Represents the <portal> tag"""
    def __init__(self, disabled):
        super().__init__('portal', )