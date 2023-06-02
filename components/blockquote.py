from hybrid.element import Element

class Blockquote(Element):
    """Represents the <blockquote> tag"""
    def __init__(self, accesskey, cite, className, contenteditable, dir_attr, hidden, id_attr, lang, style, tabindex, title, translate):
        super().__init__('blockquote', accesskey=accesskey, cite=cite, className=className, contenteditable=contenteditable, dir=dir_attr, hidden=hidden, id=id_attr, lang=lang, style=style, tabindex=tabindex, title=title, translate=translate)
