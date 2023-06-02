from hybrid.element import Element









class Select(Element):
    """Represents the <select> tag"""
    def __init__(
            self, 
            autofocus, 
            disabled, 
            form,
            multiple, 
            name, 
            required, 
            size
        ):
        super().__init__('select', )