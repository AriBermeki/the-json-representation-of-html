from hybrid.element import Element




class S(Element):
    """Represents the <s> tag"""
    def __init__(
            self,  
            accesskey,
            contenteditable,
            dir,
            hidden,
            id,
            lang,
            spellcheck,
            style,
            tabindex,
            title,
            translate
        ):
        super().__init__('s', )
