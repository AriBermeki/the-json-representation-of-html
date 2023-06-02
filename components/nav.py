from hybrid.element import Element




class Nav(Element):
    """Represents the <nav> tag"""

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
        super().__init__('nav', )