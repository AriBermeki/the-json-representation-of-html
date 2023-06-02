from hybrid.element import Element







class Map(Element):
    """Represents the <map> tag"""
    def __init__(
        self, 
        name
        ):
        super().__init__('map',)