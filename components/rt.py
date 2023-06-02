from hybrid.element import Element







class Rt(Element):
    """Represents the <rt> tag"""
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
        super().__init__('rt', )