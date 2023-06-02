from hybrid.element import Element


class Canvas(Element):
    """Represents the <canvas> tag"""

    def __init__(self, height, width, accesskey=None, className=None, contenteditable=None, dir=None, hidden=None, id=None, lang=None, style=None, tabindex=None, title=None, translate=None):
        super().__init__('canvas', accesskey=accesskey, className=className, contenteditable=contenteditable, dir=dir, hidden=hidden, id=id, lang=lang, style=style, tabindex=tabindex, title=title, translate=translate)
        self.height = height
        self.width = width
