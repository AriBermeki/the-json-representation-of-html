from hybrid.element import Element






class Object(Element):
    """Represents the <object> tag"""
    def __init__(
            self, 
            data, 
            form, 
            height, 
            name, 
            type, 
            width
        ):
        super().__init__('object', )