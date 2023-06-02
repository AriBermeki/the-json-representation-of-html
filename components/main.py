from hybrid.element import Element





class Main(Element):
    """Represents the <main> tag"""
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
        super().__init__('main', )