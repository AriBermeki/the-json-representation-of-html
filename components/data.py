from hybrid.element import Element


class Data(Element):
    """Represents the <data> tag"""
    def __init__(self, value=None):
        super().__init__('data', value=value)
