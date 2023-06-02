from hybrid.element import Element








class Section(Element):
    """Represents the <section> tag"""
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
        super().__init__('section', )