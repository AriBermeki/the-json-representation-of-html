from hybrid.element import Element



class Dt(Element):
    """Represents the <dt> tag"""
    def __init__(self, accesskey=None, class_=None, contenteditable=None, dir_=None, hidden=None, id=None, lang=None, spellcheck=None, style=None, tabindex=None, title=None, translate=None):
        super().__init__('dt', accesskey=accesskey, class_=class_, contenteditable=contenteditable, dir_=dir_, hidden=hidden, id=id, lang=lang, spellcheck=spellcheck, style=style, tabindex=tabindex, title=title, translate=translate)
