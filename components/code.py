from hybrid.element import Element




class Code(Element):
    """Represents the <code> tag"""

    def __init__(self, accesskey=None, class_=None, contenteditable=None, contextmenu=None,
                 dir_=None, draggable=None, dropzone=None, hidden=None, id=None, lang=None,
                 spellcheck=None, style=None, tabindex=None, title=None, translate=None):
        super().__init__('code', accesskey=accesskey, class_=class_, contenteditable=contenteditable,
                         contextmenu=contextmenu, dir_=dir_, draggable=draggable, dropzone=dropzone,
                         hidden=hidden, id=id, lang=lang, spellcheck=spellcheck, style=style,
                         tabindex=tabindex, title=title, translate=translate)
