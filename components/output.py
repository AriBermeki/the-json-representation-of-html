from hybrid.element import Element


class Output(Element):
    """Represents the <output> tag"""
    def __init__(self,for_, form, name ):
        super().__init__('output', )