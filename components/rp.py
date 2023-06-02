from hybrid.element import Element





class Rp(Element):
    """Represents the <rp> tag"""

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
        super().__init__('rp', )