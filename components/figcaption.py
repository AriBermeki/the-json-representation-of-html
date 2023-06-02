from hybrid.element import Element




class Figcaption(Element):
    """Represents the <figcaption> tag"""

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
            'figcaption', 
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