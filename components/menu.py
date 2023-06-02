from hybrid.element import Element



class Menu(Element):
    """Represents the <menu> tag"""
    def __init__(
            self, 
            accesskey,
            contenteditable,
            dir_,
            hidden,
            id,
            lang,
            spellcheck,
            style,
            tabindex,
            title,
            translate
        ):
        super().__init__('menu', )