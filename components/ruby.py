from hybrid.element import Element



class Ruby(Element):
    """Represents the <ruby> tag"""
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
        super().__init__('ruby', )