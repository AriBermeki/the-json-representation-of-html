from hybrid.element import Element







class Q(Element):
    """Represents the <q> tag"""
    def __init__(
            self,    
            cite,
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
        super().__init__('q', )
