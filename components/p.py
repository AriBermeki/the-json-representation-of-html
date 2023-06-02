from hybrid.element import Element




class P(Element):
    """Represents the <p> tag"""
    def __init__(self,accesskey,contenteditable,dir,hidden,id,lang,spellcheck,style,tabindex,title,translate):
        super().__init__('p', )