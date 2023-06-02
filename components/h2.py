from hybrid.element import Element




class H2(Element):
    """Represents the <h2> tag"""
    def __init__(self,accesskey, class_, contenteditable, dir_, hidden, id, lang, spellcheck, style, tabindex, title, translate ):
        super().__init__('h2', accesskey, class_, contenteditable, dir_, hidden, id, lang, spellcheck, style, tabindex, title, translate)