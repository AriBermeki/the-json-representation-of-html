from hybrid.element import Element




class Header(Element):
    """Represents the <header> tag"""
    def __init__(self, accesskey,class_,contenteditable,dir,draggable,hidden,id,lang,spellcheck,style,tabindex,title,translate):
        super().__init__('header', accesskey,class_,contenteditable,dir,draggable,hidden,id,lang,spellcheck,style,tabindex,title,translate)