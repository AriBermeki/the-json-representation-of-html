from hybrid.element import Element


class I(Element):
    """Represents the <i> tag"""
    def __init__(self, accesskey,class_,contenteditable,dir,draggable,hidden,id,lang,spellcheck,style,tabindex,title,translate):
        super().__init__('i', accesskey,class_,contenteditable,dir,draggable,hidden,id,lang,spellcheck,style,tabindex,title,translate)
