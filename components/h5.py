from hybrid.element import Element



class H5(Element):
    """Represents the <h5> tag"""
    def __init__(self,accesskey, class_, contenteditable, dir_, hidden, id, lang, spellcheck, style, tabindex, title, translate ):
        super().__init__('h5', accesskey, class_, contenteditable, dir_, hidden, id, lang, spellcheck, style, tabindex, title, translate)