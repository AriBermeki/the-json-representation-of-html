from hybrid.element import Element



class Progress(Element):
    """Represents the <progress> tag"""
    def __init__(self, max, value):
        super().__init__('progress', )
