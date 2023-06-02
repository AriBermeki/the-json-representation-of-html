from hybrid.element import Element

class Colgroup(Element):
    """Represents the <colgroup> tag"""
    def __init__(self, span=None):
        super().__init__('colgroup', span=span)
