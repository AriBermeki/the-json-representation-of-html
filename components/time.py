from hybrid.element import Element




class Time(Element):
    """Represents the <time> tag"""
    def __init__(self, datetime):
        super().__init__('time', )