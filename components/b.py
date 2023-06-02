from hybrid.element import Element






from hybrid.element import Element

class B(Element):
    """Represents the <b> tag"""

    def __init__(self, accesskey, className, contenteditable, dir, hidden, id, lang, style, tabindex, title, translate):
        super().__init__(
            'b', accesskey=accesskey, 
            className=className, 
            contenteditable=contenteditable, 
            dir=dir, hidden=hidden, 
            id=id, lang=lang, 
            style=style, 
            tabindex=tabindex, 
            title=title, 
            translate=translate)