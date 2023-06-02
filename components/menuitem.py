from hybrid.element import Element




class MenuItem(Element):
    """Represents the <menuitem> tag"""
    def __init__(
            self, 
            accesskey,
            contenteditable,
            dir,
            hidden,
            id,
            icon,
            label,
            lang,
            spellcheck,
            style,
            tabindex,
            title,
            translate,
            type
        ):
        super().__init__('menuitem', )