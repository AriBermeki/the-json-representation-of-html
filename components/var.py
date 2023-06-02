from hybrid.element import Element




class Var(Element):
    """Represents the <var> tag"""
    def __init__(self, accesskey, class_, contenteditable, dir, hidden, id, lang, spellcheck, style, tabindex, title, translate):
        super().__init__('var', )
