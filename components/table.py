from hybrid.element import Element



class Table(Element):
    """Represents the <table> tag"""
    def __init__(self, accesskey, border, cellpadding, cellspacing, class_, 
                contenteditable, contextmenu, dir_, draggable, dropzone, hidden, id, lang, 
                spellcheck, style, summary, tabindex, title, translate):
        super().__init__('table', )