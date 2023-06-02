from hybrid.element import Element

class A(Element):
    """Represents the <a> tag"""
    def __init__(self,accesskey, className, contenteditable, dir, hidden, id, lang, style, tabindex, title, translate):
        super().__init__(
            'a', accesskey=accesskey, 
            className=className, 
            contenteditable=contenteditable, 
            dir=dir, hidden=hidden, 
            id=id, lang=lang, style=style, 
            tabindex=tabindex, title=title, translate= translate)
