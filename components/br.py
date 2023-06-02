from hybrid.element import Element

class Br(Element):
    """Represents the <br> tag"""
    def __init__(self, accesskey=None, class_attr=None, contenteditable=None, dir_attr=None, hidden=None, id_attr=None, lang=None, style=None, tabindex=None, title=None, translate=None):
        super().__init__('br', accesskey=accesskey, class_attr=class_attr, contenteditable=contenteditable, dir_attr=dir_attr, hidden=hidden, id_attr=id_attr, lang=lang, style=style, tabindex=tabindex, title=title, translate=translate)
