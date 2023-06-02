from hybrid.element import Element

class Del_(Element):
    """Represents the <del_> tag"""
    def __init__(self, cite=None, datetime=None):
        super().__init__('del_', cite=cite, datetime=datetime)
