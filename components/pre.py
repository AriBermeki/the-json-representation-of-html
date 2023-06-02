from hybrid.element import Element




class Pre(Element):
    """Represents the <pre> tag"""
    def __init__(self, accesskey,contenteditable,dir,hidden,id,lang,spellcheck,style,tabindex,title,translate):
        super().__init__('pre', )