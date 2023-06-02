from hybrid.element import Element


class Col(Element):
    """Represents the <col> tag"""

    def __init__(self, span=None):
        super().__init__('col', span=span)
