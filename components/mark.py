from hybrid.element import Element








    

class Mark(Element):
    """Represents the <mark> tag"""
    def __init__(
        self,  
        accesskey, 
        contenteditable, 
        dir, 
        hidden,
        id, 
        ang, 
        spellcheck, 
        style, 
        tabindex, 
        title, 
        translate
        ):
        super().__init__('mark', )