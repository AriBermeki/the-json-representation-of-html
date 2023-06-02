from hybrid.element import Element






class Samp(Element):
    """Represents the <samp> tag"""
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
        super().__init__('samp', )
