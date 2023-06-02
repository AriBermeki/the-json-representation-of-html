from hybrid.element import Element



class H1(Element):
    """Represents the <h1> tag"""
    def __init__(self,accesskey, class_, contenteditable, dir_, hidden, id, lang, spellcheck, style, tabindex, title, translate ):
        super().__init__('h1', accesskey, class_, contenteditable, dir_, hidden, id, lang, spellcheck, style, tabindex, title, translate)