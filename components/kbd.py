from hybrid.element import Element





class Kbd(Element):
    """Represents the <kbd> tag"""
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
        super().__init__('kbd', )