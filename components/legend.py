from hybrid.element import Element






class Legend(Element):
    """Represents the <legend> tag"""
    def __init__(
            self,  
            accesskey, 
            contenteditable, 
            dir_, 
            hidden, 
            id, 
            lang, 
            spellcheck, 
            style, 
            tabindex, 
            title, 
            translate
        ):
        super().__init__('legend', )