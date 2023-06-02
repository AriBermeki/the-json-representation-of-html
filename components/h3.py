from hybrid.element import Element



class H3(Element):
    """Represents the <h3> tag"""
    def __init__(self,accesskey, class_, contenteditable, dir_, hidden, id, lang, spellcheck, style, tabindex, title, translate ):
        super().__init__('h3', accesskey, class_, contenteditable, dir_, hidden, id, lang, spellcheck, style, tabindex, title, translate)