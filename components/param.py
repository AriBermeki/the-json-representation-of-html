from hybrid.element import Element



class Param(Element):
    """Represents the <param> tag"""
    def __init__(self, name,value):
        super().__init__('param', )
