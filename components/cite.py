from hybrid.element import Element


class Cite(Element):
    """Represents the <cite> tag"""
    def __init__(self, class_=None, contenteditable=None, contextmenu=None, dir_=None, draggable=None, dropzone=None, hidden=None, id=None, lang=None, spellcheck=None, style=None, tabindex=None, title=None, translate=None):
        super().__init__('cite', class_=class_, contenteditable=contenteditable, contextmenu=contextmenu, dir_=dir_, draggable=draggable, dropzone=dropzone, hidden=hidden, id=id, lang=lang, spellcheck=spellcheck, style=style, tabindex=tabindex, title=title, translate=translate)
