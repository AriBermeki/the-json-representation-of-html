from hybrid.element import Element


class Math(Element):
    """Represents the <math> tag"""
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
            translate,
        ):
        super().__init__('math', )