from hybrid.element import Element



class H6(Element):
    """Represents the <h6> tag"""
    def __init__(self,accesskey, class_, contenteditable, dir_, hidden, id, lang, spellcheck, style, tabindex, title, translate ):
        super().__init__('h6', accesskey, class_, contenteditable, dir_, hidden, id, lang, spellcheck, style, tabindex, title, translate)