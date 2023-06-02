from hybrid.element import Element

class Caption(Element):
    """Represents the <caption> tag"""

    def __init__(self, accesskey=None, class_attr=None, contenteditable=None, contextmenu=None, dir_attr=None,
                 draggable=None, dropzone=None, hidden=None, id=None, lang=None, spellcheck=None, style=None,
                 tabindex=None, title=None, translate=None):
        super().__init__('caption', accesskey=accesskey, class_attr=class_attr, contenteditable=contenteditable,
                         contextmenu=contextmenu, dir_attr=dir_attr, draggable=draggable, dropzone=dropzone,
                         hidden=hidden, id=id, lang=lang, spellcheck=spellcheck, style=style, tabindex=tabindex,
                         title=title, translate=translate)