from hybrid.element import Element










class Slot(Element):
    """Represents the <slot> tag"""
    def __init__(
            self,
            name,
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
        super().__init__('slot', )