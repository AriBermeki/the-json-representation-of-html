from hybrid.element import Element








class Span(Element):
    """Represents the <span> tag"""
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
        super().__init__('span', )