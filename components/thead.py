from hybrid.element import Element



class THead(Element):
    """Represents the <thead> tag"""
    def __init__(self, accesskey, class_, contenteditable, dir, hidden, id, lang, spellcheck, style, tabindex, title, translate):
        super().__init__('thead', )
