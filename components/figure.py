from hybrid.element import Element






class Figure(Element):
    """Represents the <figure> tag"""
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
        super().__init__(
            'figure', 
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
            )