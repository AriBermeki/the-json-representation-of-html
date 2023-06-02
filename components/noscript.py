from hybrid.element import Element

class NoScript(Element):
    """Represents the <noscript> tag"""
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
        super().__init__('noscript', )
